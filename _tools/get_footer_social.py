import re

with open(r'c:\Users\aeyon\crystaltaxinc-clone\_scraped\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

matches = re.findall(r'<a[^>]+data-aid="FOOTER_[^"]+"[^>]*>.*?</a>', html, re.DOTALL)
for m in matches:
    aid = re.search(r'data-aid="([^"]+)"', m).group(1)
    href = re.search(r'href="([^"]+)"', m).group(1)
    svg = re.search(r'<svg.*?</svg>', m, re.DOTALL)
    print(f"{aid} -> {href}")
    if svg:
        print(f"  SVG path: {svg.group(0)[:150]}")
