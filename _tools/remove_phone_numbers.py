import os
import re

base_dir = r'c:\Users\aeyon\crystaltaxinc-clone'

html_files = [
    'index.html',
    'about-us.html',
    'tax-services.html',
    'payroll-services.html',
    'accounting-services.html',
    'contact-us.html'
]

# 1. Regex to remove top-bar phone link
# <a href="tel:7189219800" class="top-bar-phone">...</a>
phone_top_bar_pattern = re.compile(
    r'\s*<a href="tel:7189219800" class="top-bar-phone">[\s\S]*?</a>',
    re.IGNORECASE
)

# 2. Regex to replace desktop navbar CTA button with Contact Us link
desktop_cta_pattern = re.compile(
    r'<div class="nav-item">\s*<a href="tel:7189219800" class="nav-cta-btn">[\s\S]*?</a>\s*</div>',
    re.IGNORECASE
)
desktop_cta_replacement = '<div class="nav-item">\n          <a href="contact-us.html" class="nav-cta-btn">Contact Us</a>\n        </div>'

# 3. Regex to replace mobile drawer phone call button
drawer_call_pattern = re.compile(
    r'<a href="tel:7189219800" class="nav-cta-btn"[^>]*>[\s\S]*?Call \(718\) 921-9800\s*</a>',
    re.IGNORECASE
)
drawer_cta_replacement = '<a href="contact-us.html" class="nav-cta-btn" style="width: 100%; justify-content: center;">Contact Us</a>'

for filename in html_files:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove top bar phone
    content = phone_top_bar_pattern.sub('', content)

    # Replace desktop navbar phone CTA with Contact Us
    content = desktop_cta_pattern.sub(desktop_cta_replacement, content)

    # Replace mobile drawer call button
    content = drawer_call_pattern.sub(drawer_cta_replacement, content)

    # Specific page replacements:
    if filename == 'index.html':
        # Hero phone CTA -> Contact Us Online
        hero_phone_pattern = re.compile(
            r'<a href="tel:7189219800" class="hero-phone-cta">[\s\S]*?</a>',
            re.IGNORECASE
        )
        content = hero_phone_pattern.sub(
            '<a href="contact-us.html" class="hero-phone-cta">Contact Us Online</a>',
            content
        )

    if filename == 'accounting-services.html':
        # Banner phone CTA -> Contact Us
        content = re.sub(
            r'<a href="tel:7189219800" class="hero-phone-cta"[^>]*>[\s\S]*?</a>',
            '<a href="contact-us.html" class="hero-phone-cta" style="padding: 0.85rem 2.25rem;">Contact Us</a>',
            content
        )

    if filename == 'payroll-services.html':
        content = content.replace('Call us today for an affordable quote', 'Contact us today for an affordable quote')

    if filename == 'contact-us.html':
        # Remove phone item from contact-info-list
        phone_info_item_pattern = re.compile(
            r'\s*<div class="contact-info-item">\s*<svg[^>]*>[\s\S]*?</svg>\s*<a href="tel:7189219800"[^>]*>[\s\S]*?</a>\s*</div>',
            re.IGNORECASE
        )
        content = phone_info_item_pattern.sub('', content)
        # Update placeholder
        content = content.replace('placeholder="(718) 921-9800"', 'placeholder="Your phone number (optional)"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Processed {filename}')

# README.md
readme_path = os.path.join(base_dir, 'README.md')
with open(readme_path, 'r', encoding='utf-8') as f:
    readme = f.read()

readme = re.sub(r'and telephone \(`\(718\) 921-9800`\),', '', readme)
readme = re.sub(r'- \*\*Top Contact Bar\*\*: Phone `\(718\) 921-9800` link\.', '- **Top Contact Bar**: Office Email `pmsoinc@mail2usa.com` link.', readme)
readme = readme.replace('telephone link `(718) 921-9800`,', '')
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme)
print('Processed README.md')

