import os
import re

base_dir = r'c:\Users\aeyon\crystaltaxinc-clone'

brand_text = "Payroll Management System Online"

html_files = [
    'index.html',
    'about-us.html',
    'tax-services.html',
    'payroll-services.html',
    'accounting-services.html',
    'contact-us.html'
]

for filename in html_files:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Title tag
    content = re.sub(r'<title>CrystalTax Inc\s*-\s*', f'<title>{brand_text} - ', content)
    content = re.sub(r'<title>(.*?) - CrystalTax Inc</title>', rf'<title>\1 - {brand_text}</title>', content)
    content = re.sub(r'Tax Preparation Services\s*-\s*CrystalTax Inc', f'Tax Preparation Services - {brand_text}', content)

    # 2. Meta tags
    content = re.sub(r'<meta\s+name=["\']author["\']\s+content=["\']CrystalTax Inc["\']\s*/>', f'<meta name="author" content="{brand_text}" />', content)
    content = re.sub(r'<meta\s+property=["\']og:site_name["\']\s+content=["\']CrystalTax Inc["\']\s*/>', f'<meta property="og:site_name" content="{brand_text}" />', content)
    content = re.sub(r'<meta\s+property=["\']og:title["\']\s+content=["\']CrystalTax Inc', f'<meta property="og:title" content="{brand_text}', content)
    content = re.sub(r'<meta\s+name=["\']twitter:title["\']\s+content=["\']CrystalTax Inc["\']\s*/>', f'<meta name="twitter:title" content="{brand_text}" />', content)
    content = re.sub(r'<meta\s+name=["\']twitter:description["\']\s+content=["\']Crystal Tax Inc Tax Preparation["\']\s*/>', f'<meta name="twitter:description" content="{brand_text} Tax Preparation" />', content)
    content = re.sub(r'Crystal Tax Inc\. was started in 2011', f'{brand_text} was started in 2011', content)

    # 3. Nav brand logo and text
    old_nav_brand = '<a href="index.html" class="nav-brand" title="CrystalTax Inc">\n        <img src="assets/images/logo.webp" alt="CrystalTax Inc" />\n      </a>'
    new_nav_brand = f'<a href="index.html" class="nav-brand" title="{brand_text}">\n        <img src="assets/images/logo.webp" alt="{brand_text}" />\n        <span class="brand-name">{brand_text}</span>\n      </a>'
    content = content.replace(old_nav_brand, new_nav_brand)

    # In case whitespace differed
    content = re.sub(
        r'<a href="index\.html" class="nav-brand" title="CrystalTax Inc">\s*<img src="assets/images/logo\.webp" alt="CrystalTax Inc" />\s*</a>',
        new_nav_brand,
        content
    )

    # 4. Mobile drawer header logo and text
    old_mobile_hdr = '<div class="mobile-drawer-header">\n      <img src="assets/images/logo.webp" alt="CrystalTax Inc" />'
    new_mobile_hdr = f'<div class="mobile-drawer-header">\n      <div style="display:flex;align-items:center;">\n        <img src="assets/images/logo.webp" alt="{brand_text}" />\n        <span class="brand-name" style="font-size:1rem;">{brand_text}</span>\n      </div>'
    content = content.replace(old_mobile_hdr, new_mobile_hdr)
    content = re.sub(
        r'<div class="mobile-drawer-header">\s*<img src="assets/images/logo\.webp" alt="CrystalTax Inc" />',
        new_mobile_hdr,
        content
    )

    # 5. Hero title in index.html
    content = content.replace('<h1 class="hero-title">Crystal Tax Inc</h1>', f'<h1 class="hero-title">{brand_text}</h1>')

    # 6. Content occurrences
    # "At CrystalTax," -> "At Payroll Management System Online,"
    content = content.replace('At CrystalTax,', f'At {brand_text},')
    content = content.replace('at CrystalTax ', f'at {brand_text} ')
    content = content.replace('at CrystalTax,', f'at {brand_text},')
    content = content.replace('at CrystalTax', f'at {brand_text}')
    # "CrystalTax offers" -> "Payroll Management System Online offers"
    content = content.replace('CrystalTax offers', f'{brand_text} offers')
    # "CrystalTax is your solution" -> "Payroll Management System Online is your solution"
    content = content.replace('CrystalTax is your solution', f'{brand_text} is your solution')
    # "CrystalTax Inc provides" -> "Payroll Management System Online provides"
    content = content.replace('CrystalTax Inc provides', f'{brand_text} provides')
    # "CrystalTax crafts" -> "Payroll Management System Online crafts"
    content = content.replace('CrystalTax crafts', f'{brand_text} crafts')
    # "CrystalTax today" -> "Payroll Management System Online today"
    content = content.replace('CrystalTax today', f'{brand_text} today')
    # "How can CrystalTax assist you?" -> "How can Payroll Management System Online assist you?"
    content = content.replace('How can CrystalTax assist you?', f'How can {brand_text} assist you?')
    # "sent to CrystalTax Inc." -> "sent to Payroll Management System Online."
    content = content.replace('sent to CrystalTax Inc.', f'sent to {brand_text}.')
    # "CrystalTax has been handling" -> "Payroll Management System Online has been handling"
    content = content.replace('"CrystalTax has been handling', f'"{brand_text} has been handling')
    # Contact page hours card header:
    # <h4 style="...">CrystalTax Inc</h4>
    content = re.sub(r'(<h4[^>]*>)\s*CrystalTax Inc\s*(</h4>)', rf'\g<1>{brand_text}\g<2>', content)
    # iframe title:
    content = content.replace('title="CrystalTax Inc Office Location"', f'title="{brand_text} Office Location"')

    # 7. Footer copyright
    content = content.replace('Copyright &copy; 2024 CrystalTax Inc - All Rights Reserved.', f'Copyright &copy; 2024 {brand_text} - All Rights Reserved.')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {filename}')


