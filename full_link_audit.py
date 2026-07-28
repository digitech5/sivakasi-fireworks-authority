import os, glob, re

root = r"C:\Users\lajit\.gemini\antigravity\scratch\sivakasi-fireworks-authority"
html_files = glob.glob(os.path.join(root, "**", "*.html"), recursive=True)

href_map = {}

for f in html_files:
    rel_f = os.path.relpath(f, root).replace("\\", "/")
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()
        matches = re.findall(r'href=["\'](/[^"\'#?]+)["\']', content)
        for m in matches:
            href_map.setdefault(m, []).append(rel_f)

print("=== AUDIT OF ALL ABSOLUTE HREFS IN HTML FILES ===")
missing_count = 0
for href in sorted(href_map.keys()):
    if any(href.endswith(ext) for ext in [".css", ".js", ".png", ".jpg", ".jpeg", ".svg", ".webmanifest", ".xml"]):
        continue
    
    clean_href = href.lstrip("/")
    target_path = os.path.normpath(os.path.join(root, clean_href))
    
    exists_exact = os.path.isfile(target_path)
    exists_html = os.path.isfile(target_path + ".html")
    exists_dir_index = os.path.isdir(target_path) and os.path.isfile(os.path.join(target_path, "index.html"))
    
    ok = exists_exact or exists_html or exists_dir_index
    status = "OK" if ok else "MISSING 404"
    if not ok:
        missing_count += 1
    print(f"{status:11s} | {href:45s} | count: {len(href_map[href]):2d} | ex: {href_map[href][0]}")

print(f"\nTotal missing targets: {missing_count}")
