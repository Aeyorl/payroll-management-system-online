import os
import re

base_dir = r'c:\Users\aeyon\crystaltaxinc-clone'
pages = ['index.html', 'about-us.html', 'tax-services.html', 'payroll-services.html', 'accounting-services.html', 'contact-us.html']

errors = []

for page in pages:
    filepath = os.path.join(base_dir, page)
    if not os.path.exists(filepath):
        errors.append(f"Missing page: {page}")
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check referenced assets
    assets = re.findall(r'(?:src|href|url)\(["\']?([^"\'\)\s>]+)["\']?', content)
    for asset in assets:
        if asset.startswith('http://') or asset.startswith('https://') or asset.startswith('#') or asset.startswith('tel:') or asset.startswith('mailto:') or asset.startswith('data:'):
            continue
        asset_clean = asset.split('?')[0].split('#')[0]
        if not asset_clean:
            continue
        asset_path = os.path.normpath(os.path.join(base_dir, asset_clean))
        if not os.path.exists(asset_path):
            errors.append(f"In {page}: broken local reference -> '{asset}' (resolved: {asset_path})")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for err in errors:
        print("  -", err)
else:
    print("Validation PASSED! All 6 pages and referenced local assets exist.")
