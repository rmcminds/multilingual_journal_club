# Setup Guide for The Cnidae Gritty Blog Integration

This document provides instructions for setting up The Cnidae Gritty Jekyll blog to receive and display content from the Multilingual Journal Club repository.

## Prerequisites

- The Cnidae Gritty blog repository (Jekyll-based)
- Admin access to both repositories
- GitHub Personal Access Token with `repo` scope

## Setup Steps

### 1. Create Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Name: "Journal Club Sync Token"
4. Scopes: Select `repo` (full control of private repositories)
5. Click "Generate token"
6. **Copy the token immediately** (you won't see it again)

### 2. Configure Repository Secrets (Multilingual Journal Club)

In the Multilingual Journal Club repository:

1. Go to Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Add two secrets:

   **Secret 1:**
   - Name: `BLOG_REPO_NAME`
   - Value: `owner/repository` (e.g., `rmcminds/thecnidaegritty`)
   
   **Secret 2:**
   - Name: `BLOG_SYNC_TOKEN`
   - Value: [Your Personal Access Token from step 1]

### 3. Create Directory Structure (The Cnidae Gritty)

In your blog repository, create these directories:

```bash
mkdir -p _data/journal_club
mkdir -p _layouts
mkdir -p _includes/journal_club
mkdir -p pages
```

### 4. Create Jekyll Layout (The Cnidae Gritty)

Create `_layouts/journal_club_post.html`:

```html
---
layout: default
---

<article class="journal-club-post">
  <header class="post-header">
    <h1>{{ page.title }}</h1>
    <div class="post-meta">
      <span class="author">by {{ page.author }}</span>
      <span class="date">{{ page.date | date: "%B %-d, %Y" }}</span>
      <span class="language">{{ page.language }}</span>
    </div>
    
    {% if page.prompt_id %}
    <div class="prompt-info">
      <strong>Prompt:</strong> {{ page.prompt_id }} 
      ({{ page.source_language }} → {{ page.language }})
    </div>
    {% endif %}
  </header>

  <div class="post-content">
    {{ content }}
  </div>

  <footer class="post-footer">
    <p class="source-info">
      This post is part of the 
      <a href="/journal-club/">Multilingual Journal Club</a> series.
    </p>
    
    <div class="tags">
      {% for tag in page.tags %}
        <span class="tag">{{ tag }}</span>
      {% endfor %}
    </div>
  </footer>
</article>
```

### 5. Create Landing Page (The Cnidae Gritty)

Create `pages/journal-club.md`:

```markdown
---
layout: page
title: Multilingual Journal Club
permalink: /journal-club/
---

# Multilingual Journal Club

Welcome to our multilingual journal club! Here, scientists practice language and communication skills by reading peer-reviewed articles and writing summaries in various languages.

## Browse by Language

{% assign languages = site.data.journal_club | map: "language" | uniq %}
{% for language in languages %}
- [{{ language }}](#{{ language | slugify }})
{% endfor %}

## Recent Posts

{% assign all_posts = site.data.journal_club %}
{% for year_data in all_posts %}
  {% for lang_data in year_data[1] %}
    {% for post in lang_data[1] %}
### {{ post.title }}
**Author:** {{ post.author }} | **Language:** {{ post.language }} | **Date:** {{ post.date }}

[Read more]({{ post.url }})

---
    {% endfor %}
  {% endfor %}
{% endfor %}

## About the Journal Club

The Multilingual Journal Club helps participants:
1. Foster a sense of community
2. Discuss the latest science
3. Improve language and communication skills
4. Communicate science to the public
5. Learn version control and GitHub collaboration

[Visit the Journal Club Repository](https://github.com/rmcminds/multilingual_journal_club) to participate!
```

### 6. Add CSS Styling (Optional)

Add to your `assets/css/main.css` or equivalent:

```css
/* Journal Club Post Styles */
.journal-club-post .post-meta {
  display: flex;
  gap: 1rem;
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.journal-club-post .prompt-info {
  background: #f5f5f5;
  padding: 0.75rem;
  border-left: 3px solid #007bff;
  margin-bottom: 1.5rem;
}

.journal-club-post .tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 1rem;
}

.journal-club-post .tag {
  background: #e9ecef;
  padding: 0.25rem 0.75rem;
  border-radius: 3px;
  font-size: 0.85rem;
}
```

### 7. Configure Jekyll (The Cnidae Gritty)

Add to `_config.yml`:

```yaml
# Journal Club Integration
collections:
  journal_club:
    output: true
    permalink: /journal-club/:year/:month/:day/:title/

# Data files
defaults:
  - scope:
      path: "_data/journal_club"
    values:
      layout: "journal_club_post"
      category: "journal-club"
```

### 8. Test the Integration

1. **Trigger the workflow manually:**
   - In Multilingual Journal Club repo
   - Go to Actions → Sync Content to The Cnidae Gritty Blog
   - Click "Run workflow"

2. **Verify content was synced:**
   - Check The Cnidae Gritty repo
   - Look in `_data/journal_club/` for synced files
   - Check the commit log for "Sync journal club content"

3. **Build Jekyll site locally:**
   ```bash
   cd your-blog-repo
   bundle exec jekyll serve
   ```
   - Visit http://localhost:4000/journal-club/
   - Verify content displays correctly

### 9. Set Up Automatic Jekyll Build (Optional)

If your blog uses GitHub Pages, it will rebuild automatically.

If using a custom deployment, add this workflow to The Cnidae Gritty repo:

Create `.github/workflows/jekyll-build.yml`:

```yaml
name: Build and Deploy Jekyll

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.1'
          bundler-cache: true
      
      - name: Build site
        run: bundle exec jekyll build
      
      - name: Deploy
        # Add your deployment steps here
        run: echo "Deploy to your hosting"
```

## Verification Checklist

- [ ] Personal Access Token created
- [ ] Repository secrets configured
- [ ] Directory structure created in blog repo
- [ ] Jekyll layout created
- [ ] Landing page created
- [ ] CSS styling added
- [ ] Jekyll configuration updated
- [ ] Manual workflow test successful
- [ ] Content displays correctly on blog
- [ ] Automatic sync tested (push to main)

## Troubleshooting

### Workflow fails with "Permission denied"
- Check that `BLOG_SYNC_TOKEN` is correctly set
- Verify token has `repo` scope
- Confirm `BLOG_REPO_NAME` matches exactly: `owner/repo`

### Content syncs but doesn't appear on blog
- Check Jekyll `_config.yml` configuration
- Verify Jekyll build completes without errors
- Check file paths in `_data/journal_club/`
- Look for Jekyll build errors in console

### Workflow doesn't trigger automatically
- Verify workflow file is in `.github/workflows/`
- Check workflow syntax with `yamllint`
- Ensure changes are pushed to `main` branch
- Check that changed files are in `prompts/**` path

### Content appears incorrectly formatted
- Check frontmatter in synced files
- Verify Jekyll layout exists
- Review CSS styling
- Check for markdown syntax issues

## Maintenance

### Updating the Sync Script

To modify content processing:
1. Edit `.github/scripts/sync_content.py` in Multilingual Journal Club repo
2. Test locally if possible
3. Push changes and monitor workflow runs

### Rotating Access Token

Every 90 days (or as needed):
1. Generate new Personal Access Token
2. Update `BLOG_SYNC_TOKEN` secret
3. Test workflow runs successfully

### Monitoring Sync Health

Check regularly:
- GitHub Actions workflow success rate
- Time between content push and blog update
- Error logs in workflow runs
- Blog build logs

## Advanced Configuration

### Custom Content Filtering

Edit `sync_content.py` to add custom filters:

```python
def should_skip_file(filepath):
    # Add your custom logic
    if 'exclude_me' in str(filepath):
        return True
    return False
```

### Multi-Repository Sync

To sync to multiple blogs:
1. Duplicate the workflow with different names
2. Add additional secret sets for each blog
3. Adjust target repository in each workflow

### Content Transformation

Modify `create_jekyll_frontmatter()` to:
- Add custom metadata
- Generate different URL structures
- Apply content filters
- Add SEO metadata

## Support

For issues with:
- **Sync workflow**: Check Multilingual Journal Club repo Issues
- **Blog display**: Check The Cnidae Gritty repo Issues
- **Jekyll configuration**: Consult [Jekyll documentation](https://jekyllrb.com/docs/)
- **GitHub Actions**: Consult [Actions documentation](https://docs.github.com/en/actions)

## References

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub PAT Documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [Multilingual Journal Club ARCHITECTURE.md](../ARCHITECTURE.md)

---

*Last Updated: 2026-02-14*
