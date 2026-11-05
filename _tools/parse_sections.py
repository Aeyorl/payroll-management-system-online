import os
import re

save_dir = r'c:\Users\aeyon\crystaltaxinc-clone\_scraped'

def parse_page_sections(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    print(f'=== SECTIONS IN {os.path.basename(filepath)} ===')
    
    # GoDaddy sections usually have id or data-ux="Section" or <section>
    sections = re.findall(r'<section[^>]*>(.*?)</section>', html, re.DOTALL | re.IGNORECASE)
    if not sections:
        # Check divs with data-widget-type or id
        sections = re.findall(r'<div[^>]*data-widget-type=[^>]*>.*?</div>', html, re.DOTALL | re.IGNORECASE)
    
    print(f'Found {len(sections)} <section> tags')
    for i, s in enumerate(sections):
        # find headings and first 200 chars of text
        h = re.findall(r'<(h[1-6])[^>]*>(.*?)</\1>', s, re.DOTALL | re.IGNORECASE)
        h_clean = [f'{tag}: {" ".join(re.sub(r"<[^>]+>", "", text).split())}' for tag, text in h]
        
        # text
        text_clean = re.sub(r'<[^>]+>', ' ', s)
        text_clean = ' '.join(text_clean.split())
        
        # images
        imgs = re.findall(r'src=["\']([^"\']+)["\']', s, re.IGNORECASE)
        
        print(f'\n--- Section {i+1} ---')
        print(f'  Headings: {h_clean}')
        print(f'  Images: {len(imgs)}')
        for img in imgs[:3]:
            print(f'    Img: {img[:70]}')
        print(f'  Text snippet: {text_clean[:250]}...')

for fn in sorted(os.listdir(save_dir)):
    if fn.endswith('.html'):
        parse_page_sections(os.path.join(save_dir, fn))
