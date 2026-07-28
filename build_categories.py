import os, glob, re, shutil

root = r"C:\Users\lajit\.gemini\antigravity\scratch\sivakasi-fireworks-authority"

# Category Data Dictionary
CATEGORIES = {
    "rockets": {
        "title": "Rocket Fireworks | Buy Sivakasi Sky Rockets Online 2026",
        "h1": "Rocket Fireworks — Sky Rockets & Aerial Shots",
        "desc": "Complete guide to Sivakasi sky rockets. Compare multi-shot rockets, whistling rockets, color bursting rockets, and safety rules for Diwali 2026.",
        "image": "article_rockets.jpg",
        "color": "deep blue",
        "intro": "Rocket fireworks are the classic high-flying highlights of Diwali celebrations. Sivakasi manufacturers produce a wide variety of rockets ranging from single-burst color rockets to whistling rockets and multi-stage sky shells."
    },
    "sparklers": {
        "title": "Sparklers Online | Best Sivakasi Sparklers for Diwali 2026",
        "h1": "Sparklers — Electric, Wire & Color Sparklers",
        "desc": "Buy Sivakasi sparklers online. Guide to electric sparklers, wire sparklers, color sparklers, lollipop sparklers, and kid-safe fireworks for Diwali 2026.",
        "image": "article_sparklers.jpg",
        "color": "gold",
        "intro": "Sparklers are beloved by families across India. From classic 10cm electric sparklers to massive 50cm multi-color sparklers, discover safe ways to light up your festival night."
    },
    "flower-pots": {
        "title": "Flower Pots Fireworks | Sivakasi Fountain Crackers Guide 2026",
        "h1": "Flower Pots & Fountains Fireworks",
        "desc": "Complete guide to flower pots (Anars) and fountain crackers from Sivakasi. Types, heights, colors, safety ratings, and online prices for Diwali 2026.",
        "image": "article_flower_pots.jpg",
        "color": "emerald green",
        "intro": "Flower pots (Anars) erupt into spectacular showers of golden, silver, and multi-colored sparks. Perfect for ground displays during family celebrations."
    },
    "ground-chakkars": {
        "title": "Ground Chakkars | Spinning Wheel Fireworks Guide 2026",
        "h1": "Ground Chakkars — Spinning Wheel Fireworks",
        "desc": "Guide to ground chakkars and spinning wheel fireworks from Sivakasi. Learn how they work, safety surfaces, color varieties, and best prices for Diwali 2026.",
        "image": "article_sparklers.jpg",
        "color": "orange",
        "intro": "Ground chakkars spin rapidly on flat surfaces to create mesmerizing rings of fire and color. Discover ground spinners, red/green chakkars, and whistling chakkars."
    },
    "fancy-fireworks": {
        "title": "Fancy Fireworks | Premium Sivakasi Fancy Crackers Guide 2026",
        "h1": "Fancy Fireworks — Peacocks, Helicopters & Novelties",
        "desc": "Complete guide to fancy fireworks from Sivakasi — peacocks, aerial butterflies, spinning helicopters, color smoke, and novelty crackers for Diwali 2026.",
        "image": "banner_types.jpg",
        "color": "purple",
        "intro": "Fancy fireworks bring unique novelty visual effects to your festival. From spinning helicopters that soar skyward to peacock-tail fountains and color smoke."
    },
    "atom-bombs": {
        "title": "Atom Bombs & Sound Crackers | Sivakasi Bomb Crackers Guide 2026",
        "h1": "Atom Bombs & Sound Crackers",
        "desc": "Guide to atom bombs and sound crackers from Sivakasi — sound levels, decibel ratings, safety distances, legal guidelines, and eco alternatives for Diwali 2026.",
        "image": "banner_buying_guide.jpg",
        "color": "dark navy",
        "intro": "Atom bombs and sound crackers deliver classic booming festival sounds. Learn about decibel safety limits, PESO guidelines, and safe distance lighting rules."
    },
    "garlands": {
        "title": "Garland Crackers | Serial Cracker Strings Guide 2026",
        "h1": "Garland Crackers — Serial Strings & Laris",
        "desc": "Guide to garland crackers and serial strings from Sivakasi. 100-shot, 1000-shot, 5000-shot garlands, safety hanging rules, and buying tips for Diwali 2026.",
        "image": "banner_festival.jpg",
        "color": "maroon",
        "intro": "Garland crackers (Laris) create continuous rhythmic bursts. Learn how to safely hang and light serial strings for grand festival openings."
    },
    "gift-boxes": {
        "title": "Fireworks Gift Boxes | Sivakasi Combo Packs Guide 2026",
        "h1": "Fireworks Gift Boxes & Family Combo Packs",
        "desc": "Guide to fireworks gift boxes and combo packs from Sivakasi. Compare ₹500, ₹1000, ₹3000, and ₹5000 gift boxes with factory-direct pricing for Diwali 2026.",
        "image": "article_gift_box.jpg",
        "color": "crimson red",
        "intro": "Gift boxes combine sparklers, flower pots, chakkars, rockets, and novelties into convenient pre-assorted packages, offering the best overall value."
    },
    "kids-fireworks": {
        "title": "Kids Fireworks | Safe Sivakasi Crackers for Children 2026",
        "h1": "Kids Fireworks — Safe Festival Fun for Children",
        "desc": "Complete guide to safe fireworks for children — sparklers, snake tablets, pop-pops, color smoke, and parent supervision guidelines for Diwali 2026.",
        "image": "banner_kids_safety.jpg",
        "color": "pink",
        "intro": "Children deserve safe, magical festival memories. Explore low-smoke, non-exploding, age-appropriate fireworks designed specifically for young ones under supervision."
    },
    "premium-fireworks": {
        "title": "Premium Fireworks Collection | Sivakasi Sky Shots 2026",
        "h1": "Premium Fireworks — Multi-Shot Sky Cakes & Shells",
        "desc": "Guide to premium fireworks and multi-shot aerial cakes from Sivakasi — 12-shot, 30-shot, 60-shot, 100-shot sky displays for Diwali 2026.",
        "image": "hero_fireworks.jpg",
        "color": "royal gold",
        "intro": "Premium fireworks cakes launch single-ignition multi-burst aerial shows, bringing professional display standards right to your private backyard."
    },
    "festival-packs": {
        "title": "Festival Packs | Sivakasi Fireworks Packages 2026",
        "h1": "Festival Fireworks Packs & Bulk Assortments",
        "desc": "Complete guide to festival fireworks packs — family packs, budget packs, mega celebration packs from Sivakasi with factory-direct delivery for Diwali 2026.",
        "image": "article_sivakasi_factory.jpg",
        "color": "teal",
        "intro": "Festival packs assemble curated cracker sets suited for small family gatherings up to large community events, delivering maximum variety at discounted rates."
    },
    "aerial-fireworks": {
        "title": "Aerial Fireworks | Sivakasi Sky Shots & Shells Guide 2026",
        "h1": "Aerial Fireworks — Sky Shots, Rockets & Shells",
        "desc": "Guide to aerial fireworks from Sivakasi — sky shots, repeating multi-tube cakes, aerial repeaters, and launch safety guidelines for Diwali 2026.",
        "image": "hero_fireworks.jpg",
        "color": "deep purple",
        "intro": "Aerial fireworks illuminate the night sky with brilliant bursts of colors, palm trees, chrysanthemums, and brocade crowns."
    }
}

# Alias Map
ALIASES = {
    "chakkars": "ground-chakkars",
    "fancy": "fancy-fireworks",
    "bombs": "atom-bombs",
    "kids-crackers": "kids-fireworks",
    "kids-safe": "kids-fireworks",
    "premium": "premium-fireworks",
    "premium-collection": "premium-fireworks"
}

def generate_category_html(slug, data):
    return f'''<!DOCTYPE html>
<html lang="en-IN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>{data['title']}</title>
  <meta name="description" content="{data['desc']}">
  <meta name="keywords" content="{slug} fireworks, Sivakasi {slug}, buy {slug} online, Diwali {slug} 2026">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <link rel="canonical" href="https://sivakasi-fireworks.in/category/{slug}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{data['title']}">
  <meta property="og:description" content="{data['desc']}">
  <meta property="og:url" content="https://sivakasi-fireworks.in/category/{slug}">
  <meta property="og:image" content="https://sivakasi-fireworks.in/images/{data['image']}">
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
    "@type": "CollectionPage",
    "name": "{data['h1']}",
    "description": "{data['desc']}",
    "url": "https://sivakasi-fireworks.in/category/{slug}"
  }}
  </script>
</head>
<body>
<div class="announcement-bar" role="marquee" aria-label="Latest updates">
  <div class="announcement-bar__track" aria-hidden="true">
    <span class="announcement-bar__item">&#128293; Diwali 2026 Crackers Guide Now Live</span>
    <span class="announcement-bar__item">&#127878; 100+ Expert Safety Guides for Festival Season</span>
    <span class="announcement-bar__item">&#9989; Trusted by 50,000+ Families Across India</span>
    <span class="announcement-bar__item">&#128722; Buy Sivakasi Crackers Online &mdash; Up to 80% Discount</span>
  </div>
</div>

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
        <li class="primary-nav__item"><a href="/blog/index.html" class="primary-nav__link">Blog</a></li>
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
  </ul>
  <div class="mobile-nav__footer"><a href="https://redcrackers.net" target="_blank" rel="noopener" class="btn btn-primary btn-block">Buy Crackers Online</a></div>
</nav>

<main id="main-content">
  <!-- Page Banner -->
  <section class="page-banner">
    <img src="/images/{data['image']}" alt="{data['h1']}" class="page-banner__bg" loading="lazy">
    <div class="page-banner__overlay" style="background: rgba(8,11,20,0.85);"></div>
    <div class="container page-banner__content">
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <a href="/index.html">Home</a>
        <span class="breadcrumb__sep" aria-hidden="true">&rsaquo;</span>
        <a href="/fireworks-types.html">Categories</a>
        <span class="breadcrumb__sep" aria-hidden="true">&rsaquo;</span>
        <span class="breadcrumb__current" aria-current="page">{data['h1']}</span>
      </nav>
      <span class="section-eyebrow">Category Guide</span>
      <h1>{data['h1']}</h1>
      <p class="page-banner__subtitle">{data['desc']}</p>
    </div>
  </section>

  <!-- Category Content -->
  <section class="container" style="padding-top:3rem;padding-bottom:4rem">
    <div style="max-width:840px;margin-bottom:3rem">
      <h2 class="section-title" style="font-size:1.8rem;margin-bottom:1rem">Overview of {data['h1']}</h2>
      <p style="font-size:1.05rem;line-height:1.75;color:var(--clr-text-2);margin-bottom:1.25rem">{data['intro']}</p>
      <p style="font-size:1rem;line-height:1.7;color:var(--clr-text-3)">When ordering {slug.replace('-', ' ')} online from Sivakasi, always verify PESO licensing, store items in cool dry locations, and maintain prescribed safety distances during lighting.</p>
    </div>

    <!-- Buying CTA Card -->
    <div style="background:linear-gradient(135deg,var(--clr-dark-2),var(--clr-dark-3));padding:2.5rem;border-radius:var(--r);color:#fff;margin-bottom:4rem;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1.5rem">
      <div>
        <h3 style="font-size:1.5rem;color:#fff;margin-bottom:.5rem">Looking for Factory Direct {data['h1']}?</h3>
        <p style="color:rgba(255,255,255,.75);margin:0">Get up to 80% discount when ordering genuine Sivakasi fireworks online.</p>
      </div>
      <a href="https://redcrackers.net" target="_blank" rel="noopener noreferrer" class="btn btn-accent btn-lg">Buy Online at RedCrackers.net</a>
    </div>

    <!-- Category FAQ Section -->
    <h2 class="section-title" style="font-size:1.6rem;margin-bottom:1.5rem">Frequently Asked Questions</h2>
    <div class="faq-list">
      <div class="faq-item">
        <button class="faq-question" aria-expanded="false" aria-controls="cat-faq-1">
          How to select the best quality {slug.replace('-', ' ')}?
          <span class="faq-toggle" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></span>
        </button>
        <div class="faq-answer" id="cat-faq-1" aria-hidden="true" role="region">
          <div class="faq-answer__inner">
            <p>Look for genuine Sivakasi manufacturer labels, valid PESO registration numbers, intact dry packaging, and purchase through trusted online stores.</p>
          </div>
        </div>
      </div>
      <div class="faq-item">
        <button class="faq-question" aria-expanded="false" aria-controls="cat-faq-2">
          What is the recommended safety distance for {slug.replace('-', ' ')}?
          <span class="faq-toggle" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></span>
        </button>
        <div class="faq-answer" id="cat-faq-2" aria-hidden="true" role="region">
          <div class="faq-answer__inner">
            <p>Maintain at least 15 to 25 feet for ground fireworks and 30 to 50 feet for aerial and sound fireworks. Always keep a water bucket nearby.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>

<footer class="site-footer" aria-label="Site footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="footer-logo"><div class="footer-logo__icon">&#127878;</div><div class="footer-logo__text">Sivakasi<span>Fireworks</span></div></div>
        <p class="footer-brand__desc">India's most trusted fireworks education platform.</p>
      </div>
      <div class="footer-col">
        <h3 class="footer-col__title">Buying Guides</h3>
        <ul class="footer-links">
          <li><a href="/crackers-buying-guide.html" class="footer-link">Buy Crackers Online</a></li>
          <li><a href="/blog/crackers-price-list-2026.html" class="footer-link">Price List 2026</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3 class="footer-col__title">Safety</h3>
        <ul class="footer-links">
          <li><a href="/safety-guide.html" class="footer-link">Safety Guide</a></li>
          <li><a href="/kids-safety.html" class="footer-link">Kids Safety</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3 class="footer-col__title">Legal</h3>
        <ul class="footer-links">
          <li><a href="/privacy-policy.html" class="footer-link">Privacy Policy</a></li>
          <li><a href="/terms-of-service.html" class="footer-link">Terms</a></li>
        </ul>
      </div>
    </div>
  </div>
</footer>
<script src="/js/main.js" defer></script>
</body>
</html>'''

# Create Category Pages
cat_base_dir = os.path.join(root, "category")
os.makedirs(cat_base_dir, exist_ok=True)

for slug, data in CATEGORIES.items():
    html_content = generate_category_html(slug, data)
    
    # 1. category/slug.html
    flat_file = os.path.join(cat_base_dir, f"{slug}.html")
    with open(flat_file, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    # 2. category/slug/index.html
    nested_dir = os.path.join(cat_base_dir, slug)
    os.makedirs(nested_dir, exist_ok=True)
    with open(os.path.join(nested_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"Created category page: /category/{slug}")

# Create Aliases
for alias_slug, target_slug in ALIASES.items():
    target_data = CATEGORIES[target_slug]
    html_content = generate_category_html(alias_slug, target_data)
    
    flat_file = os.path.join(cat_base_dir, f"{alias_slug}.html")
    with open(flat_file, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    nested_dir = os.path.join(cat_base_dir, alias_slug)
    os.makedirs(nested_dir, exist_ok=True)
    with open(os.path.join(nested_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"Created category alias page: /category/{alias_slug} -> /category/{target_slug}")

print("All category pages generated.")
