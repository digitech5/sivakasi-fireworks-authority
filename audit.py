import os, glob, re

root = r"C:\Users\lajit\.gemini\antigravity\scratch\sivakasi-fireworks-authority"
html_files = glob.glob(os.path.join(root, "**", "*.html"), recursive=True)

href_set = set()
href_file_map = {}

for f in html_files:
    rel_f = os.path.relpath(f, root).replace("\\", "/")
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()
        matches = re.findall(r'href=["\'](/[^"\'#?]+)["\']', content)
        for m in matches:
            href_set.add(m)
            href_file_map.setdefault(m, []).append(rel_f)

print("TOTAL UNIQUE ABSOLUTE HREFS:", len(href_set))
cat_hrefs = [h for h in href_set if "/category/" in h or h.startswith("/category")]
print("\nCATEGORY HREFS FOUND IN CODEBASE:")
for h in sorted(cat_hrefs):
    print(" ", h, "-> count:", len(href_file_map[h]))

missing_files = []
for h in href_set:
    # Skip assets like .css, .js, .png, .jpg, .webmanifest, .xml
    if any(h.endswith(ext) for ext in [".css", ".js", ".png", ".jpg", ".jpeg", ".svg", ".webmanifest", ".xml"]):
        continue
    target_path = os.path.normpath(os.path.join(root, h.lstrip("/")))
    
    # Check exact match, .html match, or directory index match
    exists = os.path.isfile(target_path) or os.path.isfile(target_path + ".html") or (os.path.isdir(target_path) and os.path.isfile(os.path.join(target_path, "index.html")))
    
    if not exists:
        missing_files.append(h)

print("\nMISSING HREFS (404s):")
for m in sorted(missing_files):
    print(f"  {m} (in {len(href_file_map[m])} files, e.g. {href_file_map[m][0]})")
