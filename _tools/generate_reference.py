import os
import re

save_dir = r'c:\Users\aeyon\crystaltaxinc-clone\_scraped'

pages = [
    ('index.html', 'Home'),
    ('about-us.html', 'About Us'),
    ('tax-services.html', 'Tax Services'),
    ('payroll-services.html', 'Payroll Services'),
    ('accounting-services.html', 'Accounting Services'),
    ('contact-us.html', 'Contact Us')
]

full_doco = []

for fn, name in pages:
    path = os.path.join(save_dir, fn)
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    full_doco.append(f"# {name} ({fn})\n")
    
    # Title
    t_m = re.search(r'<title>(.*?)</title>', html)
    full_doco.append(f"**Title**: {t_m.group(1) if t_m else ''}\n")
    
    # Meta description
    d_m = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)["\']', html)
    if not d_m:
        d_m = re.search(r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+name=["\']description["\']', html)
    full_doco.append(f"**Meta Description**: {d_m.group(1) if d_m else ''}\n\n")

    # Clean body
    body_m = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL)
    if not body_m:
        continue
    body = body_m.group(1)
    body = re.sub(r'<script[^>]*>.*?</script>', '', body, flags=re.DOTALL)
    body = re.sub(r'<style[^>]*>.*?</style>', '', body, flags=re.DOTALL)
    body = re.sub(r'<svg[^>]*>.*?</svg>', '', body, flags=re.DOTALL)

    # Find text blocks
    tags = re.findall(r'<(h[1-6]|p|li|button|a)[^>]*>(.*?)</\1>', body, flags=re.DOTALL)
    seen = set()
    for tag, content in tags:
        clean = re.sub(r'<[^>]+>', ' ', content)
        clean = ' '.join(clean.split())
        clean = clean.replace('&amp;', '&').replace('&nbsp;', ' ').replace('&#39;', "'").replace('&quot;', '"')
        if len(clean) > 3 and clean not in seen:
            seen.add(clean)
            full_doco.append(f"- **[{tag}]**: {clean}\n")
    full_doco.append("\n---\n\n")

with open(r'c:\Users\aeyon\crystaltaxinc-clone\SITE_TEXT_REFERENCE.md', 'w', encoding='utf-8') as f:
    f.writelines(full_doco)

print("Generated SITE_TEXT_REFERENCE.md")
