import os
import re
from html.parser import HTMLParser

save_dir = r'c:\Users\aeyon\crystaltaxinc-clone\_scraped'

for fn in sorted(os.listdir(save_dir)):
    if not fn.endswith('.html'):
        continue
    filepath = os.path.join(save_dir, fn)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    print('===============================================================')
    print(f'PAGE: {fn}')
    print('===============================================================')
    
    # Extract background images from style attributes or CSS
    bg_matches = re.findall(r'background(?:-image)?\s*:\s*[^;]*url\(["\']?([^"\')]+)["\']?\)', html, re.IGNORECASE)
    if bg_matches:
        print('Background images:')
        for bg in set(bg_matches):
            print('  ', bg)
            
    # Extract data-ux elements or sections
    # Let's inspect sections in body
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL | re.IGNORECASE)
    if body_match:
        body = body_match.group(1)
        # Strip script and style
        clean_body = re.sub(r'<script[^>]*>.*?</script>', '', body, flags=re.DOTALL | re.IGNORECASE)
        clean_body = re.sub(r'<style[^>]*>.*?</style>', '', clean_body, flags=re.DOTALL | re.IGNORECASE)
        clean_body = re.sub(r'<svg[^>]*>.*?</svg>', '', clean_body, flags=re.DOTALL | re.IGNORECASE)
        
        # Extract text blocks by tags
        blocks = re.findall(r'<(h[1-6]|p|li|span|a|button)[^>]*>(.*?)</\1>', clean_body, flags=re.DOTALL | re.IGNORECASE)
        print('\nKey Text Content Samples:')
        seen = set()
        for tag, text in blocks:
            txt = re.sub(r'<[^>]+>', ' ', text)
            txt = ' '.join(txt.split())
            if len(txt) > 20 and txt not in seen:
                seen.add(txt)
                print(f'  [{tag}] {txt[:120]}...')

