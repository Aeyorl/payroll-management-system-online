import os
import re
import json

save_dir = r'c:\Users\aeyon\crystaltaxinc-clone\_scraped'
site_data = {}

for fn in sorted(os.listdir(save_dir)):
    if fn.endswith('.html'):
        page_name = fn.replace('.html', '')
        path = os.path.join(save_dir, fn)
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
        
        # Extract title
        title = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
        title = title.group(1) if title else ''
        
        # Extract meta description
        desc = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)["\']', html, re.IGNORECASE)
        if not desc:
            desc = re.search(r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+name=["\']description["\']', html, re.IGNORECASE)
        description = desc.group(1) if desc else ''
        
        # Find sections or widget containers
        # In GoDaddy Website Builder, sections often have data-ux or id or widget names
        # Let's find all text blocks and images
        
        # Let's extract all images with their alt and src
        img_tags = re.findall(r'<img[^>]+>', html, re.IGNORECASE)
        page_images = []
        for img in img_tags:
            src = re.search(r'src=["\']([^"\']+)["\']', img, re.IGNORECASE)
            alt = re.search(r'alt=["\']([^"\']*)["\']', img, re.IGNORECASE)
            page_images.append({
                'src': src.group(1) if src else '',
                'alt': alt.group(1) if alt else ''
            })
            
        # Let's find all links
        link_tags = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.IGNORECASE | re.DOTALL)
        page_links = []
        for href, text in link_tags:
            clean_txt = ' '.join(re.sub(r'<[^>]+>', ' ', text).split())
            page_links.append({'href': href, 'text': clean_txt})
            
        site_data[page_name] = {
            'title': title,
            'description': description,
            'images': page_images,
            'links': page_links
        }

with open(r'c:\Users\aeyon\crystaltaxinc-clone\site_structure.json', 'w', encoding='utf-8') as f:
    json.dump(site_data, f, indent=2)

print('Extracted site structure summary.')

