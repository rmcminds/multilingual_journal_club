# 📚 Documentation Index

Welcome! This document helps you find the right documentation for your needs.

## For Contributors (Language Learners)

**Start here:** [CONTRIBUTING.md](CONTRIBUTING.md)
- Complete guide for all skill levels
- Step-by-step instructions
- Web interface walkthrough
- Working with partners
- GitHub basics explained

**Quick reference:**
- Main README: [README.md](README.md)
- Example submissions: [000_example/](000_example/)
- Topic index: [topics.md](topics.md)

## For Maintainers and Administrators

**Architecture & Planning:** [ARCHITECTURE.md](ARCHITECTURE.md)
- Complete architectural plan
- Integration strategy (GitHub Actions)
- Repository structure
- Content workflow
- Future enhancements

**Blog Integration Setup:** [BLOG_SETUP.md](BLOG_SETUP.md)
- Step-by-step setup for The Cnidae Gritty blog
- Personal Access Token configuration
- Jekyll template installation
- Testing procedures
- Troubleshooting guide

**Implementation Details:** [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)
- Overview of all deliverables
- Technical features
- Testing results
- Next steps for deployment

## For Developers

**GitHub Workflows:** [.github/README.md](.github/README.md)
- Workflow documentation
- Script descriptions
- Testing instructions
- Security best practices

**Sync Script:** [.github/scripts/sync_content.py](.github/scripts/sync_content.py)
- Python content processing script
- Metadata extraction
- Jekyll frontmatter generation
- Error handling

**Example Templates:** [docs/blog-templates/](docs/blog-templates/)
- Jekyll layout examples
- Landing page template
- CSS styling
- Installation instructions

## Quick Links by Task

### "I want to contribute content"
→ [CONTRIBUTING.md](CONTRIBUTING.md)

### "I need to set up the blog integration"
→ [BLOG_SETUP.md](BLOG_SETUP.md)

### "I want to understand the overall architecture"
→ [ARCHITECTURE.md](ARCHITECTURE.md)

### "I need to modify the sync workflow"
→ [.github/README.md](.github/README.md)

### "I want to see what was implemented"
→ [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)

## Document Overview

| Document | Audience | Purpose | Length |
|----------|----------|---------|--------|
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contributors | How to contribute content | ~600 lines |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Maintainers | Complete architectural plan | ~425 lines |
| [BLOG_SETUP.md](BLOG_SETUP.md) | Blog developers | Blog integration setup | ~365 lines |
| [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) | All | Overview of deliverables | ~350 lines |
| [.github/README.md](.github/README.md) | Developers | Workflows documentation | ~100 lines |
| [docs/blog-templates/README.md](docs/blog-templates/README.md) | Blog developers | Template installation | ~60 lines |

## Support

- **Issues**: Use [GitHub Issues](https://github.com/rmcminds/multilingual_journal_club/issues) for problems
- **Discussions**: Use [GitHub Discussions](https://github.com/rmcminds/multilingual_journal_club/discussions) for questions
- **Email**: r.mcminds@thecnidaegritty.org

## Repository Structure

```
multilingual_journal_club/
├── CONTRIBUTING.md              ← Start here for contributors
├── ARCHITECTURE.md              ← Complete architectural plan
├── BLOG_SETUP.md               ← Blog integration setup
├── IMPLEMENTATION_SUMMARY.md   ← Overview of deliverables
├── DOCS_INDEX.md               ← This file
├── README.md                   ← Main repository documentation
├── .github/
│   ├── README.md               ← Workflows documentation
│   ├── workflows/
│   │   └── sync-to-blog.yml    ← Automated sync workflow
│   └── scripts/
│       └── sync_content.py     ← Content processing script
├── docs/
│   └── blog-templates/         ← Jekyll template examples
│       ├── _layouts/
│       ├── pages/
│       └── assets/css/
├── prompts/                    ← Content organized by year/language
└── 000_example/                ← Example submissions
```

---

*Last Updated: 2026-02-14*
