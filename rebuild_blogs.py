"""
Sivakasi Fireworks — Batch Blog Article Updater
Updates all blog stub articles with new production header/footer,
proper CSS links, and real images from /images/ directory.
"""
import os
import re
import glob

PROJECT_ROOT = r"C:\Users\lajit\.gemini\antigravity\scratch\sivakasi-fireworks-authority"
BLOG_DIR = os.path.join(PROJECT_ROOT, "blog")

# Article image pool (rotate through these)
IMAGES = [
    "article_rockets.jpg",
    "article_sparklers.jpg",
    "article_diwali_family.jpg",
    "article_sivakasi_factory.jpg",
    "article_flower_pots.jpg",
    "article_gift_box.jpg",
    "banner_safety.jpg",
    "banner_types.jpg",
    "banner_buying_guide.jpg",
    "banner_festival.jpg",
    "banner_kids_safety.jpg",
    "hero_fireworks.jpg",
]

# Category mapping based on URL slug keywords
def get_category(slug):
    slug = slug.lower()
    if any(k in slug for k in ['safety', 'first-aid', 'burns', 'eye', 'kids', 'children', 'heart', 'asthma', 'pregnancy', 'noise', 'pets', 'senior']):
        return 'Safety'
    if any(k in slug for k in ['buying', 'price', 'cost', 'online', 'wholesale', 'factory', 'discount', 'cheap', 'order', 'delivery', 'shipping', 'gifting', 'gift']):
        return 'Buying Guide'
    if any(k in slug for k in ['rocket', 'sparkler', 'flower', 'chakkar', 'bomb', 'garland', 'fancy', 'fountain', 'pencil', 'star', 'bijli', 'twinkling', 'golden', 'butterfly', 'helicopter', 'sky', 'aerial', 'multi', 'ground', 'snake', 'colourful', 'silent']):
        return 'Fireworks Types'
    if any(k in slug for k in ['diwali', 'festival', 'celebration', 'outdoor', 'navratri', 'pongal', 'onam', 'holi', 'dussera', 'christmas', 'new-year', 'independence', 'corporate', 'wedding', 'birthday']):
        return 'Festival'
    if any(k in slug for k in ['sivakasi', 'history', 'manufacturer', 'factory', 'economy', 'license', 'regulation', 'quality', 'made']):
        return 'Sivakasi'
    if any(k in slug for k in ['eco', 'green', 'carbon', 'pollution', 'ban', 'legal']):
        return 'Eco & Legal'
    if any(k in slug for k in ['storage', 'dispose', 'humidity', 'temperature']):
        return 'Storage'
    return 'Guide'

# Author mapping
AUTHORS = {
    0: {'name': 'Priya Sharma', 'initials': 'PS', 'role': 'Senior Fireworks Editor'},
    1: {'name': 'Arjun Kumar', 'initials': 'AK', 'role': 'Safety & Compliance Expert'},
    2: {'name': 'Kavitha Rajan', 'initials': 'KR', 'role': 'Festival Culture Writer'},
}

SHARED_HEAD = '''<!DOCTYPE html>
<html lang="en-IN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <link rel="canonical" href="https://sivakasi-fireworks.in/blog/{slug}.html">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="https://sivakasi-fireworks.in/blog/{slug}.html">
  <meta property="og:image" content="https://sivakasi-fireworks.in/images/{image}">
  <meta property="og:locale" content="en_IN">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/style.css">
  <link rel="manifest" href="/site.webmanifest">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{title}",
    "description": "{description}",
    "image": "https://sivakasi-fireworks.in/images/{image}",
    "author": {{"@type": "Person", "name": "{author_name}"}},
    "publisher": {{"@type": "Organization", "name": "Sivakasi Fireworks Guide", "url": "https://sivakasi-fireworks.in"}},
    "datePublished": "2026-01-15",
    "dateModified": "2026-07-28",
    "mainEntityOfPage": {{"@type": "WebPage", "@id": "https://sivakasi-fireworks.in/blog/{slug}.html"}}
  }}
  </script>
</head>
<body>'''

ANNOUNCEMENT = '''
<div class="announcement-bar" role="marquee" aria-label="Latest updates">
  <div class="announcement-bar__track" aria-hidden="true">
    <span class="announcement-bar__item">&#128293; Diwali 2026 Crackers Guide Now Live</span>
    <span class="announcement-bar__item">&#127878; 100+ Expert Safety Guides for Festival Season</span>
    <span class="announcement-bar__item">&#9989; Trusted by 50,000+ Families Across India</span>
    <span class="announcement-bar__item">&#128722; Buy Sivakasi Crackers Online &mdash; Up to 80% Discount</span>
    <span class="announcement-bar__item">&#128293; Diwali 2026 Crackers Guide Now Live</span>
    <span class="announcement-bar__item">&#127878; 100+ Expert Safety Guides for Festival Season</span>
    <span class="announcement-bar__item">&#9989; Trusted by 50,000+ Families Across India</span>
    <span class="announcement-bar__item">&#128722; Buy Sivakasi Crackers Online &mdash; Up to 80% Discount</span>
  </div>
</div>'''

HEADER = '''
<header class="site-header" id="siteHeader">
  <div class="container header-inner">
    <a href="/index.html" class="logo" aria-label="Sivakasi Fireworks Guide">
      <div class="logo__icon" aria-hidden="true">&#127878;</div>
      <div class="logo__text">Sivakasi<span>Fireworks</span></div>
    </a>
    <nav class="primary-nav" id="primaryNav" aria-label="Primary navigation">
      <ul class="primary-nav__list" role="list">
        <li class="primary-nav__item"><a href="/index.html" class="primary-nav__link">Home</a></li>
        <li class="primary-nav__item"><a href="/crackers-buying-guide.html" class="primary-nav__link">Buying Guide</a></li>
        <li class="primary-nav__item"><a href="/safety-guide.html" class="primary-nav__link">Safety</a></li>
        <li class="primary-nav__item"><a href="/fireworks-types.html" class="primary-nav__link">Types</a></li>
        <li class="primary-nav__item"><a href="/festival-guide.html" class="primary-nav__link">Festival Guide</a></li>
        <li class="primary-nav__item"><a href="/blog/index.html" class="primary-nav__link is-active">Blog</a></li>
        <li class="primary-nav__item"><a href="/faq.html" class="primary-nav__link">FAQ</a></li>
      </ul>
    </nav>
    <div class="header-actions">
      <button class="header-btn" id="searchToggle" aria-label="Search" aria-expanded="false"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></button>
      <button class="header-btn" id="darkModeToggle" aria-label="Toggle dark mode"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg></button>
      <button class="hamburger" id="hamburger" aria-label="Open navigation" aria-expanded="false" aria-controls="mobileNav"><span class="hamburger__bar"></span><span class="hamburger__bar"></span><span class="hamburger__bar"></span></button>
    </div>
  </div>
</header>
<div class="search-overlay" id="searchOverlay" aria-hidden="true" role="dialog" aria-label="Site search">
  <div class="search-overlay__backdrop"></div>
  <div class="search-overlay__box"><div class="search-overlay__inner">
    <svg class="search-overlay__icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
    <input type="search" class="search-overlay__input" placeholder="Search fireworks guides..." aria-label="Search" id="searchInput">
    <button class="header-btn search-overlay__close" aria-label="Close search"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
  </div><div class="search-overlay__results" id="searchResults" aria-live="polite"></div></div>
</div>
<div class="nav-overlay" id="navOverlay" aria-hidden="true"></div>
<nav class="mobile-nav" id="mobileNav" aria-label="Mobile navigation">
  <div class="mobile-nav__header">
    <div class="logo"><div class="logo__icon">&#127878;</div><div class="logo__text">Sivakasi<span>Fireworks</span></div></div>
    <button class="header-btn mobile-nav__close" aria-label="Close menu"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
  </div>
  <ul class="mobile-nav__list" role="list">
    <li><a href="/index.html" class="mobile-nav__link">Home</a></li>
    <li><a href="/crackers-buying-guide.html" class="mobile-nav__link">Buying Guide</a></li>
    <li><a href="/safety-guide.html" class="mobile-nav__link">Safety Guide</a></li>
    <li><a href="/fireworks-types.html" class="mobile-nav__link">Fireworks Types</a></li>
    <li><a href="/festival-guide.html" class="mobile-nav__link">Festival Guide</a></li>
    <li><a href="/kids-safety.html" class="mobile-nav__link">Kids Safety</a></li>
    <li><a href="/blog/index.html" class="mobile-nav__link">Blog</a></li>
    <li><a href="/faq.html" class="mobile-nav__link">FAQ</a></li>
    <li><a href="/about.html" class="mobile-nav__link">About</a></li>
    <li><a href="/contact.html" class="mobile-nav__link">Contact</a></li>
  </ul>
  <div class="mobile-nav__footer"><a href="https://redcrackers.net" target="_blank" rel="noopener" class="btn btn-primary btn-block">Buy Crackers Online</a></div>
</nav>
<div class="reading-progress" role="progressbar" aria-label="Reading progress"></div>'''

FOOTER = '''
<footer class="site-footer" aria-label="Site footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="footer-logo"><div class="footer-logo__icon">&#127878;</div><div class="footer-logo__text">Sivakasi<span>Fireworks</span></div></div>
        <p class="footer-brand__desc">India's most trusted fireworks education platform. Expert guides to buying Sivakasi crackers online, Diwali celebrations, and festival safety.</p>
        <div class="footer-social">
          <a href="#" class="social-btn" aria-label="Facebook">f</a>
          <a href="#" class="social-btn" aria-label="Instagram">in</a>
          <a href="#" class="social-btn" aria-label="YouTube">&#9654;</a>
        </div>
      </div>
      <div class="footer-col">
        <h3 class="footer-col__title">Buying Guides</h3>
        <ul class="footer-links">
          <li><a href="/crackers-buying-guide.html" class="footer-link">Buy Crackers Online</a></li>
          <li><a href="/blog/crackers-price-list-2026.html" class="footer-link">Price List 2026</a></li>
          <li><a href="/blog/online-crackers-vs-local-shop.html" class="footer-link">Online vs Local</a></li>
          <li><a href="/shipping-guide.html" class="footer-link">Shipping Guide</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3 class="footer-col__title">Safety & Guides</h3>
        <ul class="footer-links">
          <li><a href="/safety-guide.html" class="footer-link">Safety Guide</a></li>
          <li><a href="/kids-safety.html" class="footer-link">Kids Safety</a></li>
          <li><a href="/fireworks-types.html" class="footer-link">Fireworks Types</a></li>
          <li><a href="/faq.html" class="footer-link">FAQ</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3 class="footer-col__title">Company</h3>
        <ul class="footer-links">
          <li><a href="/about.html" class="footer-link">About Us</a></li>
          <li><a href="/contact.html" class="footer-link">Contact</a></li>
          <li><a href="/privacy-policy.html" class="footer-link">Privacy Policy</a></li>
          <li><a href="/sitemap.xml" class="footer-link">Sitemap</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom"><div class="footer-bottom__inner">
      <p class="footer-bottom__copy">&copy; 2026 SivakasiFireworks.in &mdash; All Rights Reserved. Educational content only.</p>
      <div class="footer-bottom__links"><a href="/privacy-policy.html">Privacy</a><a href="/terms-of-service.html">Terms</a><a href="/sitemap.xml">Sitemap</a></div>
    </div></div>
  </div>
</footer>
<button class="scroll-top" aria-label="Scroll to top">
  <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="18 15 12 9 6 15"/></svg>
</button>
<script src="/js/main.js" defer></script>
</body>
</html>'''

def extract_title(html):
    m = re.search(r'<title>(.*?)</title>', html, re.I)
    return m.group(1) if m else ''

def extract_description(html):
    m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.I)
    return m.group(1) if m else ''

def extract_h1(html):
    m = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.I | re.S)
    if m:
        return re.sub(r'<[^>]+>', '', m.group(1)).strip()
    return ''

def extract_body_content(html):
    """Extract everything between <body> and </body> (or main content)"""
    m = re.search(r'<body[^>]*>(.*?)</body>', html, re.I | re.S)
    if m:
        body = m.group(1)
        # Remove old header/footer patterns
        body = re.sub(r'<header[^>]*>.*?</header>', '', body, flags=re.I|re.S)
        body = re.sub(r'<footer[^>]*>.*?</footer>', '', body, flags=re.I|re.S)
        body = re.sub(r'<nav[^>]*class=["\'][^"\']*mobile[^"\']*["\'][^>]*>.*?</nav>', '', body, flags=re.I|re.S)
        body = re.sub(r'<div[^>]*class=["\'][^"\']*announcement[^"\']*["\'][^>]*>.*?</div>', '', body, flags=re.I|re.S)
        body = re.sub(r'<div[^>]*class=["\'][^"\']*overlay[^"\']*["\'][^>]*>.*?</div>', '', body, flags=re.I|re.S)
        body = re.sub(r'<button[^>]*scroll[^>]*>.*?</button>', '', body, flags=re.I|re.S)
        return body.strip()
    return ''

def rebuild_stub(filepath, img_index):
    """Rebuild a stub article file with proper header/footer and image"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
    except Exception as e:
        print(f"ERROR reading {filepath}: {e}")
        return False

    slug = os.path.splitext(os.path.basename(filepath))[0]
    image = IMAGES[img_index % len(IMAGES)]
    category = get_category(slug)
    author_idx = img_index % 3
    author = AUTHORS[author_idx]

    # Extract existing content
    title = extract_title(html)
    description = extract_description(html)
    h1 = extract_h1(html)

    if not title:
        title = slug.replace('-', ' ').title() + ' — Sivakasi Fireworks Guide 2026'
    if not description:
        description = f'Expert guide to {slug.replace("-", " ")} — Sivakasi Fireworks Guide 2026. Diwali crackers, safety tips, and online buying advice.'

    # Build the article content (extract or create minimal content)
    body_content = extract_body_content(html)

    # Build article page structure
    article_html = f'''<!DOCTYPE html>
<html lang="en-IN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <link rel="canonical" href="https://sivakasi-fireworks.in/blog/{slug}.html">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="https://sivakasi-fireworks.in/blog/{slug}.html">
  <meta property="og:image" content="https://sivakasi-fireworks.in/images/{image}">
  <meta property="og:locale" content="en_IN">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/style.css">
  <link rel="manifest" href="/site.webmanifest">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{title}",
    "description": "{description}",
    "image": "https://sivakasi-fireworks.in/images/{image}",
    "author": {{"@type": "Person", "name": "{author['name']}", "jobTitle": "{author['role']}"}},
    "publisher": {{"@type": "Organization", "name": "Sivakasi Fireworks Guide", "url": "https://sivakasi-fireworks.in"}},
    "datePublished": "2026-01-15",
    "dateModified": "2026-07-28",
    "mainEntityOfPage": {{"@type": "WebPage", "@id": "https://sivakasi-fireworks.in/blog/{slug}.html"}}
  }}
  </script>
</head>
<body>
{ANNOUNCEMENT}
{HEADER}

<main id="main-content">
  <!-- Page Banner -->
  <div class="page-banner" style="min-height:360px;">
    <img class="page-banner__bg" src="/images/{image}" alt="{h1 or title}" loading="eager" width="1200" height="630">
    <div class="page-banner__overlay" style="background:linear-gradient(160deg,rgba(8,11,20,.88) 0%,rgba(160,13,36,.6) 100%)"></div>
    <div class="container">
      <div class="page-banner__content">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="/index.html">Home</a>
          <span class="breadcrumb__sep" aria-hidden="true">›</span>
          <a href="/blog/index.html">Blog</a>
          <span class="breadcrumb__sep" aria-hidden="true">›</span>
          <span class="breadcrumb__current" aria-current="page">{category}</span>
        </nav>
        <div class="page-banner__eyebrow">{category}</div>
        <h1>{h1 or title}</h1>
      </div>
    </div>
  </div>

  <div class="container" style="padding-top:2.5rem;padding-bottom:3rem;">
    <div class="article-layout">
      <!-- Main Article -->
      <article class="article-main">
        <div class="article-header">
          <span class="article-cat-badge">{category}</span>
          <div class="article-meta-row">
            <div class="article-author-pill">
              <div class="author-avatar" aria-hidden="true">{author['initials']}</div>
              <span class="author-name">{author['name']}</span>
            </div>
            <div class="article-meta-item">
              <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
              <span>2026</span>
            </div>
            <div class="article-meta-item">
              <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
              <span>8 min read</span>
            </div>
          </div>
        </div>

        <!-- Featured Image -->
        <figure class="article-featured-img">
          <img src="/images/{image}" alt="{h1 or title}" loading="lazy" width="900" height="506">
        </figure>

        <!-- Share Buttons -->
        <div class="share-row">
          <span class="share-row__label">Share:</span>
          <button class="share-btn share-btn--whatsapp" data-share="whatsapp">&#128291; WhatsApp</button>
          <button class="share-btn share-btn--twitter" data-share="twitter">&#120143; Twitter</button>
          <button class="share-btn share-btn--copy" data-share="copy">&#128279; Copy Link</button>
        </div>

        <!-- Article Body -->
        <div class="article-body">
          {body_content}
        </div>

        <!-- Author Box -->
        <div class="author-box">
          <div class="author-box__avatar" aria-hidden="true">{author['initials']}</div>
          <div class="author-box__info">
            <div class="author-box__name">{author['name']}</div>
            <div class="author-box__role">{author['role']}</div>
            <p class="author-box__bio">Expert contributor at Sivakasi Fireworks Guide with years of experience covering Indian fireworks, festival safety, and online crackers buying. Dedicated to helping families celebrate safely and affordably.</p>
          </div>
        </div>

        <!-- Related Articles -->
        <section aria-labelledby="related-heading" style="margin-top:3rem">
          <h2 id="related-heading" class="section-title" style="font-size:1.5rem;margin-bottom:1.5rem">Related Articles</h2>
          <div class="articles-grid articles-grid--3">
            <article class="article-card">
              <div class="article-card__img-wrap">
                <img class="article-card__img" src="/images/banner_safety.jpg" alt="Diwali Safety Guide 2026" loading="lazy">
                <span class="article-card__badge">Safety</span>
              </div>
              <div class="article-card__body">
                <div class="article-card__meta"><span>Arjun Kumar</span><span class="article-card__meta-sep"></span><span>8 min</span></div>
                <h3 class="article-card__title"><a href="/safety-guide.html">Complete Fireworks Safety Guide 2026</a></h3>
                <a href="/safety-guide.html" class="article-card__readmore">Read Guide &#8594;</a>
              </div>
            </article>
            <article class="article-card">
              <div class="article-card__img-wrap">
                <img class="article-card__img" src="/images/article_sivakasi_factory.jpg" alt="Sivakasi Crackers Online Buying" loading="lazy">
                <span class="article-card__badge">Buying</span>
              </div>
              <div class="article-card__body">
                <div class="article-card__meta"><span>Priya Sharma</span><span class="article-card__meta-sep"></span><span>12 min</span></div>
                <h3 class="article-card__title"><a href="/blog/sivakasi-crackers-online-buying-guide.html">Complete Online Buying Guide 2026</a></h3>
                <a href="/blog/sivakasi-crackers-online-buying-guide.html" class="article-card__readmore">Read Guide &#8594;</a>
              </div>
            </article>
            <article class="article-card">
              <div class="article-card__img-wrap">
                <img class="article-card__img" src="/images/banner_kids_safety.jpg" alt="Kids Fireworks Safety" loading="lazy">
                <span class="article-card__badge">Kids</span>
              </div>
              <div class="article-card__body">
                <div class="article-card__meta"><span>Arjun Kumar</span><span class="article-card__meta-sep"></span><span>11 min</span></div>
                <h3 class="article-card__title"><a href="/kids-safety.html">Kids Fireworks Safety Guide</a></h3>
                <a href="/kids-safety.html" class="article-card__readmore">Read Guide &#8594;</a>
              </div>
            </article>
          </div>
        </section>
      </article>

      <!-- Sidebar -->
      <aside class="article-sidebar">
        <!-- TOC Widget -->
        <div class="sidebar-widget">
          <div class="sidebar-widget__header">&#128196; Table of Contents</div>
          <div class="sidebar-widget__body">
            <div class="toc"><div class="toc__list" id="tocList"><!-- Auto-generated by JS --></div></div>
          </div>
        </div>

        <!-- CTA Widget -->
        <div class="sidebar-widget sidebar-cta">
          <div class="sidebar-widget__header">Buy Crackers Online</div>
          <div class="sidebar-widget__body">
            <p>Get up to 80% discount on authentic Sivakasi crackers. Factory-direct delivery across India.</p>
            <a href="https://redcrackers.net" target="_blank" rel="noopener noreferrer" class="btn btn-accent btn-block">Visit RedCrackers.net</a>
          </div>
        </div>

        <!-- Quick Links -->
        <div class="sidebar-widget">
          <div class="sidebar-widget__header">Popular Guides</div>
          <div class="sidebar-widget__body">
            <div class="sidebar-links">
              <a href="/crackers-buying-guide.html" class="sidebar-link"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>Crackers Buying Guide</a>
              <a href="/safety-guide.html" class="sidebar-link"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>Safety Guide</a>
              <a href="/fireworks-types.html" class="sidebar-link"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>Types of Fireworks</a>
              <a href="/kids-safety.html" class="sidebar-link"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>Kids Safety Guide</a>
              <a href="/blog/crackers-price-list-2026.html" class="sidebar-link"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>Price List 2026</a>
              <a href="/faq.html" class="sidebar-link"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>Fireworks FAQ</a>
            </div>
          </div>
        </div>
      </aside>
    </div>
  </div>

  <!-- Newsletter -->
  <section class="newsletter-section" aria-labelledby="nl-heading">
    <div class="container">
      <div class="newsletter-inner">
        <h2 id="nl-heading" class="section-title" style="color:#fff">Get Diwali 2026 Fireworks Guides</h2>
        <p>Join 50,000+ families getting early-bird discounts, safety updates, and expert buying guides.</p>
        <form class="newsletter-form" aria-label="Newsletter signup" onsubmit="return false;">
          <label for="nlEmail-article" class="sr-only">Email address</label>
          <input type="email" id="nlEmail-article" class="newsletter-input" placeholder="Enter your email address" autocomplete="email" required>
          <button type="submit" class="btn btn-accent">Subscribe Free</button>
        </form>
        <p class="newsletter-note">No spam. Unsubscribe anytime.</p>
      </div>
    </div>
  </section>
</main>

{FOOTER}
'''

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(article_html)
        return True
    except Exception as e:
        print(f"ERROR writing {filepath}: {e}")
        return False


def main():
    # Find all blog HTML files
    blog_files = glob.glob(os.path.join(BLOG_DIR, "*.html"))
    
    # Skip files that have already been fully rebuilt (they have article-body class)
    SKIP_FILES = {
        'index.html',
        'sivakasi-crackers-online-buying-guide.html',
        'diwali-safety-tips-complete-guide.html',
    }
    
    updated = 0
    skipped = 0
    errors = 0

    for i, filepath in enumerate(sorted(blog_files)):
        filename = os.path.basename(filepath)
        
        if filename in SKIP_FILES:
            print(f"SKIP: {filename} (already rebuilt)")
            skipped += 1
            continue
        
        # Check if already rebuilt with new design
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            if 'article-layout' in content and 'logo__icon' in content:
                print(f"SKIP: {filename} (already has new design)")
                skipped += 1
                continue
        except:
            pass
        
        if rebuild_stub(filepath, i):
            print(f"UPDATED: {filename}")
            updated += 1
        else:
            errors += 1

    print(f"\n{'='*50}")
    print(f"COMPLETE: {updated} updated, {skipped} skipped, {errors} errors")
    print(f"Total blog files processed: {len(blog_files)}")


if __name__ == '__main__':
    main()
