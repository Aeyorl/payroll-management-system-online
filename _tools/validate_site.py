import os
import glob
import json
from html.parser import HTMLParser

class Validator(HTMLParser):
    def __init__(self, base_dir, html_file):
        super().__init__()
        self.base_dir = base_dir
        self.html_file = html_file
        self.errors = []
        self.images = []
        self.links = []
        self.scripts = []
        self.title = None
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'title':
            self.in_title = True
        elif tag == 'img':
            src = attrs_dict.get('src')
            if src:
                self.images.append(src)
                target = os.path.join(self.base_dir, src.replace('/', os.sep))
                if not os.path.exists(target):
                    self.errors.append(f'Broken image src: {src}')
        elif tag == 'link':
            href = attrs_dict.get('href')
            rel = attrs_dict.get('rel', '')
            if href and not href.startswith('http') and not href.startswith('#'):
                self.links.append((rel, href))
                target = os.path.join(self.base_dir, href.replace('/', os.sep))
                if not os.path.exists(target):
                    self.errors.append(f'Broken link href: {href} (rel={rel})')
        elif tag == 'script':
            src = attrs_dict.get('src')
            if src and not src.startswith('http'):
                self.scripts.append(src)
                target = os.path.join(self.base_dir, src.replace('/', os.sep))
                if not os.path.exists(target):
                    self.errors.append(f'Broken script src: {src}')
        elif tag == 'a':
            href = attrs_dict.get('href')
            if href and not href.startswith(('http', 'mailto:', 'tel:', '#')):
                target = os.path.join(self.base_dir, href.replace('/', os.sep))
                if not os.path.exists(target):
                    self.errors.append(f'Broken nav link: {href}')

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title = data.strip()

for base in [r'c:\Users\aeyon\crystaltaxinc-clone', r'c:\Users\aeyon\payroll-management-system-online']:
    print(f'=== Validating {base} ===')
    # Validate webmanifest
    wm_path = os.path.join(base, 'site.webmanifest')
    if os.path.exists(wm_path):
        with open(wm_path, 'r', encoding='utf-8') as f:
            wm = json.load(f)
        for ic in wm.get('icons', []):
            ic_src = ic['src'].lstrip('./')
            if not os.path.exists(os.path.join(base, ic_src.replace('/', os.sep))):
                print(f'ERROR: manifest icon missing {ic_src}')
        print('site.webmanifest: VALID')
    else:
        print('ERROR: site.webmanifest missing')

    # Validate HTML files
    for h in sorted(glob.glob(os.path.join(base, '*.html'))):
        with open(h, 'r', encoding='utf-8') as f:
            content = f.read()
        v = Validator(base, h)
        v.feed(content)
        name = os.path.basename(h)
        if v.errors:
            print(f'{name}: ERRORS -> {v.errors}')
        else:
            print(f'{name}: OK (Title: "{v.title}", Images: {len(v.images)}, Links: {len(v.links)})')

