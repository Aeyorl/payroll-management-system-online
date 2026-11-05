import re
import json

with open(r'c:\Users\aeyon\crystaltaxinc-clone\_scraped\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

nav_svgs = {}
hamb = re.search(r'<svg[^>]*data-ux="IconHamburger"[\s\S]*?</svg>', html)
if hamb:
    nav_svgs['hamburger'] = hamb.group(0)

close = re.search(r'<svg[^>]*data-ux="CloseIcon"[\s\S]*?</svg>', html)
if close:
    nav_svgs['close'] = close.group(0)

phone = re.search(r'<svg[^>]*data-aid="PHONE_ICON"[\s\S]*?</svg>', html)
if not phone:
    # search for telephone svg
    phone = re.search(r'<svg[^>]*>[\s\S]*?(?:M6\.62|phone|tel)[\s\S]*?</svg>', html)
if phone:
    nav_svgs['phone'] = phone.group(0)

print("Found nav icons:", list(nav_svgs.keys()))
with open(r'c:\Users\aeyon\crystaltaxinc-clone\nav_svgs.json', 'w', encoding='utf-8') as f:
    json.dump(nav_svgs, f, indent=2)
