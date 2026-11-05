import os
import re
from collections import Counter

save_dir = r'c:\Users\aeyon\crystaltaxinc-clone\_scraped'
colors = Counter()

for fn in os.listdir(save_dir):
    if fn.endswith('.html'):
        path = os.path.join(save_dir, fn)
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
            
        hex_colors = re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}\b', html)
        for c in hex_colors:
            colors[c.lower()] += 1
            
        rgba_colors = re.findall(r'rgba?\([^)]+\)', html)
        for c in rgba_colors:
            colors[c] += 1

print('Top 25 colors found across site:')
for c, count in colors.most_common(25):
    print(f'  {c}: {count}')
