import urllib.request
import os
import re

base_url = 'https://crystaltaxinc.com'
pages = [
    '/',
    '/about-us',
    '/tax-services',
    '/payroll-services',
    '/accounting-services',
    '/contact-us'
]

save_dir = r'c:\Users\aeyon\crystaltaxinc-clone\_scraped'
os.makedirs(save_dir, exist_ok=True)

all_links = set()
all_images = set()

for page in pages:
    full_url = base_url + page
    filename = 'index.html' if page == '/' else page.strip('/') + '.html'
    filepath = os.path.join(save_dir, filename)
    print(f'Fetching {full_url} -> {filename}...')
    try:
        req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req) as resp:
            content = resp.read()
            with open(filepath, 'wb') as f:
                f.write(content)
            html = content.decode('utf-8', errors='ignore')
            
            # Extract links
            links = re.findall(r'href=["\']([^"\']+)["\']', html)
            for l in links:
                all_links.add(l)
                
            # Extract images
            imgs = re.findall(r'src=["\']([^"\']+)["\']', html)
            for img in imgs:
                if any(ext in img.lower() for ext in ['.jpg', '.jpeg', '.png', '.webp', '.gif', '.svg', 'isteam']):
                    all_images.add(img)
            
            bg_imgs = re.findall(r'url\([\'"]?([^\'")]+)[\'"]?\)', html)
            for bg in bg_imgs:
                if any(ext in bg.lower() for ext in ['.jpg', '.jpeg', '.png', '.webp', '.gif', '.svg', 'isteam']):
                    all_images.add(bg)
                    
            print(f'  Saved {filename} ({len(content)} bytes)')
    except Exception as e:
        print(f'Failed {full_url}: {e}')

print('\n--- ALL FOUND INTERNAL LINKS ---')
for l in sorted(list(all_links)):
    if l.startswith('/') or 'crystaltaxinc.com' in l:
        print('Internal link:', l)

print(f'\nTotal unique images found: {len(all_images)}')
for img in sorted(list(all_images)):
    print('  Image:', img)

