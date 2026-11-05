import re
import json

with open(r'c:\Users\aeyon\crystaltaxinc-clone\_scraped\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

social_svgs = {}
matches = re.findall(r'<a[^>]+data-aid="FOOTER_([A-Z]+)_LINK"[^>]*>([\s\S]*?)</a>', html)
for platform, content in matches:
    svg_m = re.search(r'<svg[\s\S]*?</svg>', content)
    if svg_m:
        social_svgs[platform.lower()] = svg_m.group(0)

print("Found platforms:", list(social_svgs.keys()))
with open(r'c:\Users\aeyon\crystaltaxinc-clone\social_svgs.json', 'w', encoding='utf-8') as f:
    json.dump(social_svgs, f, indent=2)
