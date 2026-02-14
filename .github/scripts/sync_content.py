#!/usr/bin/env python3
"""
Content sync script for Multilingual Journal Club to The Cnidae Gritty blog.

This script:
1. Scans the prompts directory for content
2. Filters out drafts and unpublishable content
3. Transforms content to Jekyll-compatible format
4. Adds appropriate frontmatter
5. Organizes content for the blog
"""

import os
import sys
import yaml
import re
from pathlib import Path
from datetime import datetime
import hashlib
import shutil

# Environment variables
SOURCE_DIR = os.getenv('SOURCE_DIR', 'multilingual_journal_club/prompts')
TARGET_DIR = os.getenv('TARGET_DIR', 'blog/_data/journal_club')
COMMIT_SHA = os.getenv('COMMIT_SHA', 'unknown')

def should_skip_file(filepath):
    """Determine if a file should be skipped during sync."""
    path_str = str(filepath)
    
    # Skip drafts
    if '_draft' in path_str or '/_drafts/' in path_str:
        return True
    
    # Skip README files (these are prompts, not writings)
    if filepath.name.upper() == 'README.MD':
        return True
    
    # Skip notes files
    if '0_notes' in filepath.name or '0_notas' in filepath.name:
        return True
    
    # Only process markdown files
    if not filepath.suffix.lower() in ['.md', '.markdown']:
        return True
    
    return False

def extract_metadata_from_path(filepath, source_root):
    """Extract metadata from file path structure."""
    parts = filepath.relative_to(source_root).parts
    
    metadata = {
        'year': None,
        'source_language': None,
        'prompt_id': None,
        'target_language': None,
        'author': None,
        'content_type': None,
    }
    
    # Parse path: {year}/{source_lang}/{prompt_id}/{target_lang}/{author_type_source.md}
    # OR: {year}/{source_lang}/{prompt_id}/{author_type_source.md} (direct in prompt folder)
    if len(parts) >= 5:
        metadata['year'] = parts[0]
        metadata['source_language'] = parts[1]
        metadata['prompt_id'] = parts[2]
        metadata['target_language'] = parts[3]
    elif len(parts) == 4:
        # File is directly in prompt folder (no target language subfolder)
        metadata['year'] = parts[0]
        metadata['source_language'] = parts[1]
        metadata['prompt_id'] = parts[2]
        # Target language same as source for these cases
        metadata['target_language'] = parts[1]
    
    # Parse filename: author_type_source.md
    filename = filepath.stem
    filename_parts = filename.split('_')
    if len(filename_parts) >= 2:
        metadata['author'] = filename_parts[0]
        metadata['content_type'] = filename_parts[1] if len(filename_parts) > 1 else 'writing'
    
    return metadata

def read_prompt_description(prompt_path):
    """Read the prompt README to get context."""
    readme_path = prompt_path / 'README.md'
    if readme_path.exists():
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract first paragraph or heading
            lines = [l.strip() for l in content.split('\n') if l.strip()]
            if lines:
                return lines[0].lstrip('#').strip()
    return "Journal Club Writing"

def create_jekyll_frontmatter(metadata, content, prompt_description):
    """Create Jekyll frontmatter for the content."""
    # Generate a unique ID based on file path
    file_id = hashlib.md5(str(metadata).encode()).hexdigest()[:8]
    
    # Create slug from author and prompt
    slug = f"{metadata.get('author', 'unknown')}_{metadata.get('prompt_id', 'unknown')}"
    slug = re.sub(r'[^a-z0-9_-]', '', slug.lower())
    
    frontmatter = {
        'layout': 'journal_club_post',
        'title': prompt_description,
        'author': metadata.get('author', 'Anonymous'),
        'date': datetime.now().strftime('%Y-%m-%d'),
        'categories': ['journal-club'],
        'tags': [],
        'language': metadata.get('target_language', 'unknown'),
        'source_language': metadata.get('source_language', 'unknown'),
        'year': metadata.get('year'),
        'prompt_id': metadata.get('prompt_id'),
        'content_type': metadata.get('content_type', 'summary'),
        'journal_club_id': file_id,
        'source_commit': COMMIT_SHA,
    }
    
    # Add language tags
    if metadata.get('target_language'):
        frontmatter['tags'].append(f"lang-{metadata['target_language']}")
    if metadata.get('year'):
        frontmatter['tags'].append(metadata['year'])
    
    return frontmatter

def process_content_file(source_file, source_root, target_root):
    """Process a single content file and copy to target."""
    try:
        # Extract metadata
        metadata = extract_metadata_from_path(source_file, source_root)
        
        # Skip if essential metadata is missing
        if not metadata.get('year') or not metadata.get('author'):
            print(f"⚠ Skipping {source_file.relative_to(source_root)}: insufficient metadata")
            return False
        
        # Read original content
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Get prompt description
        prompt_path = source_root / metadata['year'] / metadata['source_language'] / metadata['prompt_id']
        prompt_description = read_prompt_description(prompt_path)
        
        # Create frontmatter
        frontmatter = create_jekyll_frontmatter(metadata, content, prompt_description)
        
        # Create target directory structure
        target_subdir = target_root / metadata['year'] / metadata['target_language']
        target_subdir.mkdir(parents=True, exist_ok=True)
        
        # Create target filename
        target_file = target_subdir / f"{metadata['author']}_{metadata['prompt_id']}.md"
        
        # Write file with frontmatter
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write('---\n')
            yaml.dump(frontmatter, f, default_flow_style=False, allow_unicode=True)
            f.write('---\n\n')
            f.write(content)
        
        print(f"✓ Synced: {source_file.relative_to(source_root)} -> {target_file.relative_to(target_root)}")
        return True
        
    except Exception as e:
        print(f"✗ Error processing {source_file}: {e}", file=sys.stderr)
        return False

def sync_content():
    """Main sync function."""
    source_root = Path(SOURCE_DIR)
    target_root = Path(TARGET_DIR)
    
    if not source_root.exists():
        print(f"Error: Source directory {source_root} does not exist", file=sys.stderr)
        sys.exit(1)
    
    # Create target directory
    target_root.mkdir(parents=True, exist_ok=True)
    
    # Clear existing content (fresh sync each time)
    if target_root.exists():
        for item in target_root.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
    
    # Process all markdown files
    processed = 0
    skipped = 0
    errors = 0
    
    for filepath in source_root.rglob('*.md'):
        if should_skip_file(filepath):
            skipped += 1
            continue
        
        if process_content_file(filepath, source_root, target_root):
            processed += 1
        else:
            errors += 1
    
    # Create index file
    index_data = {
        'sync_date': datetime.now().isoformat(),
        'commit_sha': COMMIT_SHA,
        'files_processed': processed,
        'files_skipped': skipped,
        'files_errored': errors,
    }
    
    with open(target_root / 'sync_info.yml', 'w') as f:
        yaml.dump(index_data, f, default_flow_style=False)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"Sync completed:")
    print(f"  Processed: {processed} files")
    print(f"  Skipped:   {skipped} files")
    print(f"  Errors:    {errors} files")
    print(f"{'='*60}")
    
    return errors == 0

if __name__ == '__main__':
    success = sync_content()
    sys.exit(0 if success else 1)
