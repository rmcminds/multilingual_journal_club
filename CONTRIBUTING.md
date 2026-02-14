# Contributing to Multilingual Journal Club

Welcome! 🌍 We're excited that you want to contribute to the Multilingual Journal Club. This guide will help you get started, whether you're new to GitHub or an experienced contributor.

## Quick Start

**Total beginner?** Don't worry! You can contribute by:
1. Reading articles
2. Writing summaries in your target language
3. Reviewing others' work
4. Participating in discussions

**No technical experience required!** You can do everything through GitHub's web interface.

---

## Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Getting Started](#getting-started)
- [Submitting Your Writing](#submitting-your-writing)
- [Reviewing Others' Work](#reviewing-others-work)
- [Working with Partners](#working-with-partners)
- [Understanding GitHub Workflows](#understanding-github-workflows)
- [Content Guidelines](#content-guidelines)
- [Getting Help](#getting-help)

---

## Ways to Contribute

### 1. Write Article Summaries
- Choose a prompt from `/prompts/{year}/{language}/`
- Read the source material
- Write your summary/analysis in your target language
- Submit via pull request

### 2. Review and Edit
- Find writings that need review
- Provide constructive feedback
- Suggest language improvements
- Help make content more natural

### 3. Create Prompts
- Suggest new articles or topics
- Create writing prompts
- Organize topical discussions

### 4. Improve Documentation
- Fix typos or unclear instructions
- Translate documentation
- Add examples or resources

### 5. Participate in Discussions
- Answer questions in Issues/Discussions
- Share language learning resources
- Organize study groups

---

## Getting Started

### Option 1: Web Interface (Recommended for Beginners)

No installation needed! Use GitHub's website directly:

1. **Create a GitHub Account** (if you don't have one)
   - Go to https://github.com/join
   - Follow the signup process

2. **Navigate to the Repository**
   - Visit: https://github.com/rmcminds/multilingual_journal_club

3. **Request Collaborator Access** (Optional but recommended)
   - Email Dr. McMinds: r.mcminds@thecnidaegritty.org
   - This allows you to approve your partner's pull requests

### Option 2: GitHub Desktop (For Intermediate Users)

1. Download [GitHub Desktop](https://desktop.github.com/)
2. Clone the repository
3. Make changes locally
4. Commit and push

### Option 3: Command Line (For Advanced Users)

```bash
git clone https://github.com/rmcminds/multilingual_journal_club.git
cd multilingual_journal_club
# Make your changes
git add .
git commit -m "Your message"
git push
```

---

## Submitting Your Writing

### Step-by-Step Guide (Web Interface)

#### 1. Choose a Prompt

Browse the `/prompts/` folder:
- Organized by year: `prompts/2024/`
- Then by source language: `prompts/2024/english/`
- Then by prompt number: `prompts/2024/english/prompt_2024_01/`

Each prompt folder contains a `README.md` with:
- The writing prompt
- Link to source material (article, video, etc.)
- Any specific instructions

#### 2. Navigate to Target Language Folder

**If the folder exists:**
- Click into the folder for your target language (e.g., `español/`, `français/`, `english/`)

**If the folder doesn't exist (you're the first!):**
- Don't worry! You'll create it in the next step

#### 3. Create Your File

**Click "Add file" → "Create new file"**

**Name your file:**
- Format: `yourname_type_source.md`
- Examples:
  - `john_summary_Delory2023.md`
  - `maria_resumen_Delory2023.md`
  - `pierre_critique_Delory2023.md`

**If creating a new language folder:**
- Type the folder name before your filename
- Example: `français/pierre_revue_Delory2023.md`
- GitHub automatically creates the folder!

#### 4. Write Your Content

Use markdown format for formatting (optional):

```markdown
# My Summary of [Article Title]

## Main Findings
[Your summary here]

## Analysis
[Your thoughts here]

## Questions
- [Questions you have]
```

**Markdown Quick Reference:**
- `# Heading` - Large heading
- `## Subheading` - Medium heading
- `**bold**` - Bold text
- `*italic*` - Italic text
- `[link text](URL)` - Links
- `- item` - Bullet points

Don't know markdown? Just write plain text! It works fine.

#### 5. Commit Your Changes

At the bottom of the page:

1. **Commit message**: Write a short description
   - Example: "Add my summary of Delory 2023 in Spanish"

2. **Choose "Create a new branch"**
   - Suggested name is fine, or create your own
   - Example: `john-delory-summary`

3. **Click "Propose new file"**

#### 6. Create Pull Request

GitHub will ask you to create a Pull Request:

1. **Title**: Auto-filled, you can edit
2. **Description**: Add context (optional)
   - "This is my first summary!"
   - "Looking for feedback on grammar"
3. **Assign reviewers**: Pick a partner if you have one
4. **Click "Create pull request"**

🎉 **Done!** Your content is now submitted for review.

---

## Reviewing Others' Work

### Finding Work to Review

**Option 1: Open Pull Requests**
- Go to "Pull requests" tab
- Look for PRs labeled "needs review"
- Read the proposed changes

**Option 2: Browse Existing Content**
- Navigate to any writing in the repository
- Click the pencil icon (✏️) to edit
- Suggest improvements

### How to Provide Feedback

#### On Pull Requests (Recommended)

1. **Click on the Pull Request**
2. **Go to "Files changed" tab**
3. **Click the "+" next to lines you want to comment on**
4. **Write your feedback:**
   - Point out grammar issues
   - Suggest better word choices
   - Ask clarifying questions
   - Give encouragement!

5. **Submit review:**
   - "Comment" - Just feedback
   - "Approve" - Looks good!
   - "Request changes" - Needs improvement

**Example Comments:**
- ✅ "Consider using 'discovered' instead of 'found' for a more formal tone"
- ✅ "Great point about the methodology! Could you elaborate?"
- ✅ "Small typo: 'teh' → 'the'"
- ❌ "This is wrong" (Too vague)

#### Direct File Editing

1. **Navigate to the file** on GitHub
2. **Click the pencil icon** (✏️)
3. **Make your edits directly**
4. **Commit changes:**
   - Create new branch
   - Write commit message explaining changes
   - Create pull request

### Best Practices for Reviews

**Be Constructive:**
- Explain *why* a change improves the text
- Offer alternatives, not just criticisms
- Celebrate what works well

**Be Specific:**
- Quote the exact text you're referring to
- Provide concrete examples
- Link to resources if helpful

**Be Kind:**
- Remember: Everyone is learning
- Use encouraging language
- Respect different language levels

---

## Working with Partners

Partners help each other improve! Here's how:

### Finding a Partner

1. **Post in Discussions**: "Looking for Spanish practice partner!"
2. **Check Issues**: See who's working on what
3. **Email Dr. McMinds**: Get matched with someone

### Partner Workflow

**Weekly Cycle (Example):**

**Monday:** Choose a prompt together
**Tuesday-Thursday:** Write independently
**Friday:** Exchange drafts, provide written feedback
**Weekend:** Video call to discuss edits, practice speaking

**Pull Request Workflow:**

1. **Author** creates PR, assigns partner as reviewer
2. **Partner** reviews, comments, suggests changes
3. **Author** addresses feedback, commits updates
4. **Partner** approves
5. **Either person** merges to main branch

### Collaborative Branches

For closer collaboration:

1. **Author** creates branch and PR (don't merge)
2. **Partner** commits directly to that branch
3. Both work together until satisfied
4. **Either person** merges when complete

---

## Understanding GitHub Workflows

### Branches

Think of branches as separate copies where you can work without affecting the main version.

- **`main` branch**: The official, published version
- **Your branch**: Your working copy

### Pull Requests (PRs)

A pull request says: "I have changes I'd like to merge into main."

**PR Lifecycle:**
1. Create (you propose changes)
2. Review (others give feedback)
3. Revise (you address feedback)
4. Approve (reviewer accepts)
5. Merge (changes go to main)

### Commits

Each commit is a saved snapshot of your changes.

**Good commit message:** "Add Spanish summary of Delory 2023"
**Bad commit message:** "Update file" (too vague)

### Protection and Safety

- **Main branch is protected**: Requires approval before merging
- **Version history**: Can always undo changes
- **Mistakes are OK**: Nothing is permanent!

---

## Content Guidelines

### Writing Quality

**We encourage all skill levels!** Focus on:
- Clear communication
- Honest effort
- Openness to feedback

**Suggested structure:**
1. 2-3 sentence summary of findings
2. 2-3 sentences analyzing methods/hypotheses
3. 2-3 sentences suggesting future directions

### Language Use

**Target language practice:**
- Write in the language you're learning
- Natural mistakes are expected
- Accept corrections graciously

**Scientific content:**
- Cite sources properly
- Respect copyright
- Give credit to original authors

### File Naming

**Pattern:** `author_type_source.md`

**Examples:**
- `rmcminds_resumen_Delory2023.md`
- `jsmith_summary_Delory2023.md`
- `acolon_critique_Greenspan2022.md`

### Folder Organization

```
prompts/
  └── 2024/                    # Year
      └── english/             # Source language
          └── prompt_2024_01/  # Prompt number
              ├── README.md    # Prompt description
              ├── español/     # Target language
              ├── français/    # Target language
              └── 中文/         # Target language
```

---

## Content Licensing and Publication

### Important: Content May Be Published

✨ **Your writings may be automatically published on The Cnidae Gritty blog!**

**What this means:**
- Quality content merged to `main` may be synced to the blog
- Your work helps communicate science to the public
- You get credit as the author
- Content is publicly discoverable

**What you should know:**
- By contributing, you agree to share your work publicly
- All content is under the repository's LICENSE
- You can request content removal if needed

### Opting Out

If you don't want specific content published on the blog:
- Add `_draft` to the filename: `author_summary_draft.md`
- Or place in a folder named `_drafts/`
- These are automatically excluded from blog sync

---

## Getting Help

### Resources in This Repository

- **[README.md](README.md)**: Overview and getting started
- **[ARCHITECTURE.md](ARCHITECTURE.md)**: Technical details about blog integration
- **[topics.md](topics.md)**: Index of prompts by topic
- **[000_example/](000_example/)**: Example submissions

### External Resources

**Markdown:**
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)

**GitHub:**
- [GitHub for Scientists](https://osf.io/preprints/metaarxiv/x3p2q/)
- [GitHub Docs](https://docs.github.com/)

**Language Learning:**
- [Linguee](https://www.linguee.com/) - Natural translations
- [Dr. Geoff Lindsey](https://youtube.com/@DrGeoffLindsey) - Phonetics
- [iNatle](https://thecnidaegritty.org/iNatle/) - Multilingual organism names

**Scientific Writing:**
- [The Science of Scientific Writing](https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing)

### Getting Support

**For technical issues:**
- Check [GitHub Issues](https://github.com/rmcminds/multilingual_journal_club/issues)
- Create new issue if your problem isn't listed

**For questions and discussion:**
- Use [GitHub Discussions](https://github.com/rmcminds/multilingual_journal_club/discussions)
- Great for open-ended questions

**For private matters:**
- Email Dr. McMinds: r.mcminds@thecnidaegritty.org

**For urgent problems:**
- Tag @rmcminds in an issue
- Be patient! Community volunteers manage this project

---

## Community Guidelines

### Be Respectful

- **Everyone is learning**: Different skill levels are expected
- **Multiple perspectives**: Value diverse viewpoints
- **Cultural sensitivity**: Respect language and cultural differences

### Be Constructive

- **Focus on improvement**: Make suggestions, not just criticisms
- **Explain your reasoning**: Help others learn why something works better
- **Offer alternatives**: Don't just say what's wrong

### Be Encouraging

- **Celebrate progress**: Acknowledge effort and growth
- **Share resources**: Help others find useful tools
- **Build community**: We're in this together!

### Remember

> "The point of this activity is to offer and accept critique of our language and communication skills. Please do not be afraid to make mistakes, and try not to be offended when critiques are offered! Be friendly, everyone!"

— From the main README

---

## Advanced Topics

### For Maintainers

If you've been granted maintainer access:

**Responsibilities:**
- Review and merge pull requests
- Help answer questions
- Maintain content quality
- Moderate discussions

**Best Practices:**
- Require at least one review before merging
- Check for quality and appropriateness
- Provide constructive feedback
- Be patient with novice contributors

### Creating New Prompts

**Structure:**
```
prompts/{year}/{source_language}/prompt_{year}_{number}/
├── README.md
└── (language folders created by contributors)
```

**README.md should include:**
- Clear writing prompt
- Link to source material
- Any special instructions
- Due date (if applicable)

**Example:**
```markdown
# Prompt 2024-01: Plant-Soil Metabolism

Read the following article and write a summary in your target language:

[Delory, Callaway, & Semchenko 2023](https://doi.org/10.1111/nph.19490)

## Suggested Structure:
1. 2-3 sentences: Main findings
2. 2-3 sentences: Methods analysis
3. 2-3 sentences: Future directions
```

### Using Git Locally

For contributors comfortable with command line:

```bash
# Clone repository
git clone https://github.com/rmcminds/multilingual_journal_club.git
cd multilingual_journal_club

# Create new branch
git checkout -b my-summary

# Add your file
nano prompts/2024/english/prompt_2024_01/español/myname_resumen.md

# Commit changes
git add .
git commit -m "Add Spanish summary of Delory 2023"

# Push to GitHub
git push origin my-summary

# Create PR on GitHub website
```

---

## Frequently Asked Questions

**Q: I'm not comfortable with GitHub. Can I still participate?**
A: Yes! Write your summaries and share with a partner via email. You can still benefit from the language practice.

**Q: How do I know if my content will be published on the blog?**
A: Content merged to the main branch may be published. Files with `_draft` in the name are excluded.

**Q: Can I delete or edit my published work?**
A: Yes! Edit the file and submit a PR, or contact Dr. McMinds for removal.

**Q: What if I make a mistake in GitHub?**
A: Don't worry! The main branch is protected, and all changes are reversible. Mistakes are part of learning!

**Q: How do I find a language partner?**
A: Post in Discussions or email Dr. McMinds to get connected with someone.

**Q: Can I contribute in a language not yet in the repository?**
A: Absolutely! Create a new folder with the language name when you submit your first writing.

**Q: How formal should my writing be?**
A: Aim for clarity. Practice the style you want to improve - informal blog post or formal scientific writing.

**Q: Can I contribute code or technical improvements?**
A: Yes! Check ARCHITECTURE.md for technical details, then submit a PR with your improvements.

---

## Thank You!

Your contributions help build a supportive community for language learning and scientific communication. Whether you're writing your first summary or reviewing your hundredth, you're making a difference!

Happy writing! 📝🌍

---

*Last Updated: 2026-02-14*
*Questions? Contact: r.mcminds@thecnidaegritty.org*
