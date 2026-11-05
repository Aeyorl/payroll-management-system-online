import os
import re

save_dir = r'c:\Users\aeyon\crystaltaxinc-clone\_scraped'
for fn in sorted(os.listdir(save_dir)):
    if fn.endswith('.html'):
        path = os.path.join(save_dir, fn)
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
        print('====================================')
        print(f'FILE: {fn}')
        print('====================================')
        title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
        print('Title:', title_match.group(1) if title_match else 'None')
        desc_match = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)["\']', html, re.IGNORECASE)
        if not desc_match:
            desc_match = re.search(r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+name=["\']description["\']', html, re.IGNORECASE)
        print('Description:', desc_match.group(1) if desc_match else 'None')
        
        # Extract headings
        headings = re.findall(r'<(h[1-4])[^>]*>(.*?)</\1>', html, re.IGNORECASE | re.DOTALL)
        clean_headings = []
        for tag, text in headings:
            cleaned = re.sub(r'<[^>]+>', ' ', text)
            cleaned = ' '.join(cleaned.split())
            if cleaned:
                clean_headings.append(f'{tag.upper()}: {cleaned}')
        print('Headings count:', len(clean_headings))
        for h in clean_headings:
            print('  ', h)

