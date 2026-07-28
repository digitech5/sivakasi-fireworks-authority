import os, glob

root = r"C:\Users\lajit\.gemini\antigravity\scratch\sivakasi-fireworks-authority"
sitemap_path = os.path.join(root, "sitemap.xml")

domain = "https://sivakasi-fireworks.in"

urls = []

# Core pages
core_pages = [
    "",
    "/index.html",
    "/crackers-buying-guide.html",
    "/safety-guide.html",
    "/fireworks-types.html",
    "/festival-guide.html",
    "/kids-safety.html",
    "/faq.html",
    "/about.html",
    "/contact.html",
    "/shipping-guide.html",
    "/festival-checklist.html",
    "/privacy-policy.html",
    "/terms-of-service.html",
    "/disclaimer.html"
]

for p in core_pages:
    urls.append((f"{domain}{p}", "2026-07-28", "daily" if p in ["", "/index.html"] else "weekly", "1.0" if p in ["", "/index.html"] else "0.9"))

# Category clean URLs
categories = [
    "rockets", "sparklers", "flower-pots", "ground-chakkars",
    "fancy-fireworks", "atom-bombs", "garlands", "gift-boxes",
    "kids-fireworks", "premium-fireworks", "festival-packs", "aerial-fireworks"
]

for c in categories:
    urls.append((f"{domain}/category/{c}", "2026-07-28", "weekly", "0.85"))

# Blog pages
blog_files = sorted(glob.glob(os.path.join(root, "blog", "*.html")))
for bf in blog_files:
    fname = os.path.basename(bf)
    rel_path = f"/blog/{fname}"
    urls.append((f"{domain}{rel_path}", "2026-07-28", "monthly", "0.8" if fname == "index.html" else "0.75"))

# Build sitemap XML
xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]

for loc, lastmod, changefreq, priority in urls:
    xml_lines.append('  <url>')
    xml_lines.append(f'    <loc>{loc}</loc>')
    xml_lines.append(f'    <lastmod>{lastmod}</lastmod>')
    xml_lines.append(f'    <changefreq>{changefreq}</changefreq>')
    xml_lines.append(f'    <priority>{priority}</priority>')
    xml_lines.append('  </url>')

xml_lines.append('</urlset>')

sitemap_content = '\n'.join(xml_lines)

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"Updated sitemap.xml with {len(urls)} URLs.")
