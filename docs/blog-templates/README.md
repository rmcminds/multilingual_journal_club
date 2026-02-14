# Blog Template Files

This directory contains example Jekyll template files for The Cnidae Gritty blog to display content from the Multilingual Journal Club.

These files are **reference templates** that should be added to The Cnidae Gritty repository, not this one.

## Files Included

1. **`_layouts/journal_club_post.html`** - Jekyll layout for individual journal club posts
2. **`pages/journal-club.md`** - Landing page listing all journal club content
3. **`_includes/post-card.html`** - Reusable component for post previews
4. **`assets/css/journal-club.css`** - Styling for journal club content

## Installation Instructions

See [BLOG_SETUP.md](../../BLOG_SETUP.md) for complete setup instructions.

### Quick Start

1. Copy these files to your Jekyll blog repository
2. Place them in the appropriate directories (matching the directory names)
3. Update your `_config.yml` as documented
4. Rebuild your Jekyll site

## Customization

These templates can be customized to match your blog's design:

- Modify HTML structure in layout files
- Adjust CSS to match your theme
- Add or remove metadata fields
- Change navigation elements

## Example Usage

After setup, synced content will automatically use the `journal_club_post` layout and appear at URLs like:

```
https://yourblog.com/journal-club/2024/01/15/author-prompt/
```

The landing page will be accessible at:

```
https://yourblog.com/journal-club/
```

## Dependencies

These templates assume your Jekyll blog has:
- A `default` layout
- Basic Jekyll collections configured
- Standard Jekyll variables available

## Support

For questions or issues:
- Check [BLOG_SETUP.md](../../BLOG_SETUP.md) troubleshooting section
- Review [ARCHITECTURE.md](../../ARCHITECTURE.md) for system design
- Open an Issue in the appropriate repository
