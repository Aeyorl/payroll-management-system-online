import os
import re
import urllib.request
import urllib.parse

save_dir = r'c:\Users\aeyon\crystaltaxinc-clone\_scraped'
assets_dir = r'c:\Users\aeyon\crystaltaxinc-clone\assets\images'
os.makedirs(assets_dir, exist_ok=True)

all_img_urls = set()

# Regex to find all wsimg or image urls
for fn in os.listdir(save_dir):
    if fn.endswith('.html'):
        path = os.path.join(save_dir, fn)
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
            
        # img src
        for m in re.finditer(r'src=["\']([^"\']+)["\']', html):
            url = m.group(1)
            if 'wsimg.com' in url or any(url.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.webp', '.svg', '.gif']):
                all_img_urls.add(url)
                
        # url(...) in style or css
        for m in re.finditer(r'url\(["\']?([^"\'\)]+)["\']?\)', html):
            url = m.group(1)
            if 'wsimg.com' in url or any(url.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.webp', '.svg', '.gif']):
                all_img_urls.add(url)

print(f'Total candidate images: {len(all_img_urls)}')

url_map = {}
idx = 0
for u in sorted(list(all_img_urls)):
    full_url = u
    if full_url.startswith('//'):
        full_url = 'https:' + full_url
    elif full_url.startswith('/'):
        full_url = 'https://crystaltaxinc.com' + full_url
        
    # Generate a clean filename
    # Identify key images: logo, hero, service images
    ext = '.jpg'
    if '.png' in full_url.lower():
        ext = '.png'
    elif '.webp' in full_url.lower():
        ext = '.webp'
    elif '.svg' in full_url.lower():
        ext = '.svg'
    elif '.gif' in full_url.lower():
        ext = '.gif'
        
    filename = None
    if 'logo' in full_url.lower():
        filename = f'logo{ext}'
    elif 'index_main' in full_url.lower() or 'businesstaxprep' in full_url.lower():
        filename = f'business_tax_prep{ext}'
    else:
        # stock id or sanitized name
        stock_m = re.search(r'stock/([^/:]+)', full_url)
        if stock_m:
            stock_id = stock_m.group(1)
            # check width or purpose
            w_m = re.search(r'rs=w:(\d+)', full_url)
            w_str = f'_{w_m.group(1)}' if w_m else ''
            filename = f'stock_{stock_id}{w_str}{ext}'
        else:
            ip_m = re.search(r'/([^/:]+)\.(jpg|png|webp|svg|jpeg)', full_url, re.I)
            if ip_m:
                filename = f'{ip_m.group(1)}{ext}'
            else:
                idx += 1
                filename = f'asset_{idx}{ext}'

    dest = os.path.join(assets_dir, filename)
    print(f'Downloading: {full_url[:80]} -> {filename}')
    try:
        req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            with open(dest, 'wb') as f_out:
                f_out.write(data)
            url_map[u] = filename
            print(f'  Success: {len(data)} bytes')
    except Exception as e:
        print(f'  Failed: {e}')

import json
with open(os.path.join(assets_dir, 'image_map.json'), 'w') as f:
    json.dump(url_map, f, indent=2)
print('Done assets download.')

