import os
import re

save_dir = r'c:\Users\aeyon\crystaltaxinc-clone\_scraped'
svgs = {}

for fn in os.listdir(save_dir):
    if fn.endswith('.html'):
        path = os.path.join(save_dir, fn)
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
            
        matches = re.findall(r'(<svg[^>]*>.*?</svg>)', html, re.DOTALL | re.IGNORECASE)
        for s in matches:
            # find aria-label or data-ux
            label_m = re.search(r'aria-label=["\']([^"\']+)["\']', s)
            aid_m = re.search(r'data-aid=["\']([^"\']+)["\']', s)
            name = label_m.group(1) if label_m else (aid_m.group(1) if aid_m else f'svg_{len(svgs)}')
            if name not in svgs:
                svgs[name] = s

print(f'Total unique SVGs identified: {len(svgs)}')
for k in svgs:
    print(f'  SVG: {k}')

import json
with open(r'c:\Users\aeyon\crystaltaxinc-clone\extracted_svgs.json', 'w', encoding='utf-8') as f:
    json.dump(svgs, f, indent=2)
