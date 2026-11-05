import re

with open(r'c:\Users\aeyon\crystaltaxinc-clone\_scraped\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# find header nav
nav_m = re.search(r'<nav[^>]*>([\s\S]*?)</nav>', html)
if nav_m:
    print('Nav HTML:')
    print(nav_m.group(0)[:2000])

links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([\s\S]*?)</a>', nav_m.group(0) if nav_m else '')
print('\nNav Links:')
for href, txt in links:
    clean = ' '.join(re.sub(r'<[^>]+>', ' ', txt).split())
    print(f'  {clean} -> {href}')
