# GitHub Workflows and Scripts

This directory contains GitHub Actions workflows and supporting scripts for the Multilingual Journal Club repository.

## Workflows

### `sync-to-blog.yml`

Automatically synchronizes content from this repository to The Cnidae Gritty Jekyll blog.

**Triggers:**
- Pushes to `main` branch that modify files in `prompts/**`
- Manual workflow dispatch

**What it does:**
1. Checks out both repositories
2. Runs Python sync script to process content
3. Transforms markdown files with Jekyll frontmatter
4. Commits and pushes changes to the blog repository

**Required Secrets:**
- `BLOG_REPO_NAME`: Full repository name (e.g., `rmcminds/thecnidaegritty`)
- `BLOG_SYNC_TOKEN`: GitHub Personal Access Token with `repo` scope

**Excluded from sync:**
- Files/folders with `_draft` in the name
- Files in `_drafts/` directories
- README.md files (prompts only)
- Notes files (0_notes.txt, 0_notas.txt)

## Scripts

### `scripts/sync_content.py`

Python script that processes and syncs content.

**Key features:**
- Scans `prompts/` directory recursively
- Extracts metadata from file paths
- Creates Jekyll-compatible frontmatter
- Organizes content by year and language
- Generates sync information

**Metadata extracted:**
- Year, source language, prompt ID
- Target language, author, content type
- Git commit information

**Output structure:**
```
_data/journal_club/
├── {year}/
│   └── {language}/
│       └── {author}_{prompt_id}.md
└── sync_info.yml
```

## Development

### Testing Locally

To test the sync script locally:

```bash
# Install dependencies
pip install pyyaml python-frontmatter

# Set environment variables
export SOURCE_DIR=prompts
export TARGET_DIR=/tmp/blog/_data/journal_club
export COMMIT_SHA=test

# Run script
python .github/scripts/sync_content.py
```

### Modifying the Workflow

1. Edit the YAML file in `workflows/`
2. Test in a branch first
3. Monitor Actions tab for results
4. Check logs for any issues

### Updating the Sync Script

1. Edit `scripts/sync_content.py`
2. Test locally if possible
3. Update this README if adding features
4. Commit and push changes

## Troubleshooting

### Workflow not triggering

- Check that changes are in `prompts/**` path
- Verify workflow file syntax
- Ensure push is to `main` branch

### Sync failing

- Check workflow logs in Actions tab
- Verify repository secrets are set
- Confirm Personal Access Token is valid
- Check Python script error messages

### Content not appearing on blog

- Verify sync completed successfully
- Check blog repository for new commit
- Ensure Jekyll build is working
- Review blog configuration

## Security

- Never commit Personal Access Tokens
- Use repository secrets for sensitive data
- Limit PAT scope to minimum required (`repo`)
- Rotate tokens periodically

## References

- [Main Architecture Document](../ARCHITECTURE.md)
- [Blog Setup Guide](../BLOG_SETUP.md)
- [Contributing Guide](../CONTRIBUTING.md)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

*For issues or questions, create an Issue or Discussion in this repository.*
