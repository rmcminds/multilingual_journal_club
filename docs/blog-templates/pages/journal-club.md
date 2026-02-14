---
layout: page
title: Multilingual Journal Club
permalink: /journal-club/
---

<div class="journal-club-landing">
  <header class="page-header">
    <h1>Multilingual Journal Club</h1>
    <p class="lead">
      Scientists practicing language and communication skills through peer-reviewed research summaries in multiple languages.
    </p>
  </header>

  <section class="about-section">
    <h2>About the Journal Club</h2>
    <p>
      The Multilingual Journal Club brings together language learners and scientists to read peer-reviewed articles 
      and write summaries in various languages. Participants help each other improve their communication skills 
      while discussing the latest science.
    </p>
    
    <div class="goals">
      <h3>Our Goals</h3>
      <ul>
        <li>Foster a sense of community among learners</li>
        <li>Provide a forum to discuss the latest science</li>
        <li>Improve language and communication skills</li>
        <li>Create content that communicates science to the public</li>
        <li>Familiarize participants with version control and GitHub</li>
      </ul>
    </div>

    <p class="cta">
      <a href="https://github.com/rmcminds/multilingual_journal_club" 
         class="btn btn-primary" 
         target="_blank" 
         rel="noopener">
        Join the Journal Club
      </a>
    </p>
  </section>

  <section class="filter-section">
    <h2>Browse Content</h2>
    
    <div class="filters">
      <div class="filter-group">
        <h3>By Language</h3>
        <ul class="language-filter">
          <li><a href="#english">English</a></li>
          <li><a href="#español">Español</a></li>
          <li><a href="#français">Français</a></li>
          <li><a href="#all">All Languages</a></li>
        </ul>
      </div>

      <div class="filter-group">
        <h3>By Year</h3>
        <ul class="year-filter">
          <li><a href="#2024">2024</a></li>
          <li><a href="#2023">2023</a></li>
          <li><a href="#all-years">All Years</a></li>
        </ul>
      </div>
    </div>
  </section>

  <section class="posts-section">
    <h2>Recent Posts</h2>
    
    {% comment %}
    Note: This assumes content is in site.data.journal_club
    Adjust based on your actual Jekyll configuration
    {% endcomment %}
    
    {% assign all_files = site.data.journal_club | values | map: "values" | compact %}
    
    <div class="posts-grid">
      {% for year_folder in site.static_files %}
        {% if year_folder.path contains '_data/journal_club' and year_folder.extname == '.md' %}
          {% assign post = year_folder %}
          <div class="post-card">
            <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
            <div class="post-meta">
              <span class="author">{{ post.author }}</span>
              <span class="language">{{ post.language }}</span>
              <span class="date">{{ post.date | date: "%Y-%m-%d" }}</span>
            </div>
            <p>{{ post.excerpt | strip_html | truncate: 150 }}</p>
            <a href="{{ post.url }}" class="read-more">Read more →</a>
          </div>
        {% endif %}
      {% endfor %}
    </div>

    {% comment %}
    Alternative if using collections:
    {% for post in site.journal_club reversed %}
      <article class="post-summary">
        <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
        <div class="post-meta">
          <span class="author">{{ post.author }}</span> | 
          <span class="language">{{ post.language }}</span> | 
          <span class="date">{{ post.date | date: "%B %-d, %Y" }}</span>
        </div>
        <p>{{ post.excerpt }}</p>
        <a href="{{ post.url }}">Read more →</a>
      </article>
    {% endfor %}
    {% endcomment %}
  </section>

  <section class="contribute-section">
    <h2>Want to Contribute?</h2>
    <p>
      Join our community of language learners and scientists! Whether you're practicing 
      a second language or improving your scientific communication skills, everyone is welcome.
    </p>
    <p>
      <a href="https://github.com/rmcminds/multilingual_journal_club/blob/main/CONTRIBUTING.md" 
         class="btn btn-secondary"
         target="_blank" 
         rel="noopener">
        Read the Contributing Guide
      </a>
    </p>
  </section>

  <section class="resources-section">
    <h2>Resources</h2>
    <ul>
      <li>
        <a href="https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing" 
           target="_blank" rel="noopener">
          The Science of Scientific Writing
        </a>
      </li>
      <li>
        <a href="https://www.linguee.com/" target="_blank" rel="noopener">
          Linguee - Natural translations in context
        </a>
      </li>
      <li>
        <a href="https://thecnidaegritty.org/iNatle/" target="_blank" rel="noopener">
          iNatle - Learn organism names in multiple languages
        </a>
      </li>
      <li>
        <a href="https://www.markdownguide.org/basic-syntax/" target="_blank" rel="noopener">
          Markdown Guide
        </a>
      </li>
    </ul>
  </section>
</div>
