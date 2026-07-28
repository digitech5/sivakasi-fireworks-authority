import os, glob, re

root = r"C:\Users\lajit\.gemini\antigravity\scratch\sivakasi-fireworks-authority"
html_files = glob.glob(os.path.join(root, "**", "*.html"), recursive=True)

# Replacements map for links
REPLACEMENTS = {
    # Category links format consistency (BUG 10: /category/sparklers NOT /category/sparklers.html)
    r'href=["\']/category/atom-bombs(?:\.html)?["\']': 'href="/category/atom-bombs"',
    r'href=["\']/category/bombs(?:\.html)?["\']': 'href="/category/atom-bombs"',
    r'href=["\']/category/chakkars(?:\.html)?["\']': 'href="/category/ground-chakkars"',
    r'href=["\']/category/ground-chakkars(?:\.html)?["\']': 'href="/category/ground-chakkars"',
    r'href=["\']/category/fancy(?:\.html)?["\']': 'href="/category/fancy-fireworks"',
    r'href=["\']/category/fancy-fireworks(?:\.html)?["\']': 'href="/category/fancy-fireworks"',
    r'href=["\']/category/flower-pots(?:\.html)?["\']': 'href="/category/flower-pots"',
    r'href=["\']/category/garlands(?:\.html)?["\']': 'href="/category/garlands"',
    r'href=["\']/category/gift-boxes(?:\.html)?["\']': 'href="/category/gift-boxes"',
    r'href=["\']/category/kids-crackers(?:\.html)?["\']': 'href="/category/kids-fireworks"',
    r'href=["\']/category/kids-safe(?:\.html)?["\']': 'href="/category/kids-fireworks"',
    r'href=["\']/category/kids-fireworks(?:\.html)?["\']': 'href="/category/kids-fireworks"',
    r'href=["\']/category/premium(?:\.html)?["\']': 'href="/category/premium-fireworks"',
    r'href=["\']/category/premium-collection(?:\.html)?["\']': 'href="/category/premium-fireworks"',
    r'href=["\']/category/premium-fireworks(?:\.html)?["\']': 'href="/category/premium-fireworks"',
    r'href=["\']/category/rockets(?:\.html)?["\']': 'href="/category/rockets"',
    r'href=["\']/category/sparklers(?:\.html)?["\']': 'href="/category/sparklers"',
    r'href=["\']/category/festival-packs(?:\.html)?["\']': 'href="/category/festival-packs"',
    r'href=["\']/category/aerial-fireworks(?:\.html)?["\']': 'href="/category/aerial-fireworks"',
}

updated_files_count = 0

for f in html_files:
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()
    
    new_content = content
    for pattern, repl in REPLACEMENTS.items():
        new_content = re.sub(pattern, repl, new_content)
        
    if new_content != content:
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(new_content)
        updated_files_count += 1

print(f"Updated category links to clean URL format in {updated_files_count} HTML files.")
