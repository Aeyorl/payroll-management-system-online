import os
import re

save_dir = r'c:\Users\aeyon\crystaltaxinc-clone\_scraped'

def extract_page_details(fn):
    filepath = os.path.join(save_dir, fn)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    print(f"\n=======================================================")
    print(f"DETAILS FOR: {fn}")
    print(f"=======================================================")
    
    # Remove script, style, svg
    body = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL | re.IGNORECASE)
    if not body:
        return
    text = body.group(1)
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<svg[^>]*>.*?</svg>', '', text, flags=re.DOTALL | re.IGNORECASE)
    
    # Find all sections or major blocks
    sections = re.findall(r'<section[^>]*>(.*?)</section>', text, flags=re.DOTALL | re.IGNORECASE)
    for s_idx, sec in enumerate(sections):
        print(f"\n--- SECTION {s_idx+1} ---")
        # Extract images
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', sec, flags=re.IGNORECASE)
        if imgs:
            print("  Images:")
            for img in imgs:
                print(f"    - {img[:80]}")
        # Extract headings & paragraphs & buttons
        elements = re.findall(r'<(h[1-6]|p|li|a|button)[^>]*>(.*?)</\1>', sec, flags=re.DOTALL | re.IGNORECASE)
        seen = set()
        for tag, content in elements:
            cleaned = re.sub(r'<[^>]+>', ' ', content)
            cleaned = ' '.join(cleaned.split())
            # decode common entities
            cleaned = cleaned.replace('&amp;', '&').replace('&nbsp;', ' ').replace('&#39;', "'").replace('&quot;', '"')
            if cleaned and len(cleaned) > 2 and cleaned not in seen:
                # filter out pure navigation repeating
                seen.add(cleaned)
                print(f"  [{tag.upper()}] {cleaned}")

for page in ['index.html', 'about-us.html', 'tax-services.html', 'payroll-services.html', 'accounting-services.html', 'contact-us.html']:
    extract_page_details(page)
