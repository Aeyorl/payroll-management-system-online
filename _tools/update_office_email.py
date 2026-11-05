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

email_top_bar = '''        <a href="mailto:pmsoinc@mail2usa.com" class="top-bar-email" style="display: inline-flex; align-items: center; gap: 0.4rem; color: var(--primary); font-weight: 600;">
          <svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
          pmsoinc@mail2usa.com
        </a>\n'''

email_mobile_drawer = '''      <a href="mailto:pmsoinc@mail2usa.com" class="nav-cta-btn" style="width: 100%; justify-content: center; margin-top: 0.65rem; background-color: #ffffff; color: var(--primary) !important; border: 1.5px solid var(--primary);">
        <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
        pmsoinc@mail2usa.com
      </a>\n'''

for filename in html_files:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add email to top-bar
    if 'pmsoinc@mail2usa.com' not in content:
        content = content.replace(
            '<div class="container top-bar-content">\n        <a href="tel:7189219800"',
            '<div class="container top-bar-content">\n' + email_top_bar + '        <a href="tel:7189219800"'
        )
        # Also add to mobile drawer footer
        content = content.replace(
            'Call (718) 921-9800\n      </a>\n    </div>',
            'Call (718) 921-9800\n      </a>\n' + email_mobile_drawer + '    </div>'
        )

    # 2. In contact-us.html, add email item in contact-info-list
    if filename == 'contact-us.html':
        old_contact_info = '''              <div class="contact-info-item">
                <svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
                <a href="tel:7189219800" style="color: var(--primary); font-weight: 600;">(718)921-9800</a>
              </div>'''

        new_contact_info = old_contact_info + '''\n              <div class="contact-info-item">
                <svg viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
                <a href="mailto:pmsoinc@mail2usa.com" style="color: var(--primary); font-weight: 600;">pmsoinc@mail2usa.com</a>
              </div>'''
        
        if 'mailto:pmsoinc@mail2usa.com' not in content:
            content = content.replace(old_contact_info, new_contact_info)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {filename} with office email')

# Update README.md
readme_path = os.path.join(base_dir, 'README.md')
with open(readme_path, 'r', encoding='utf-8') as f:
    readme = f.read()

if 'pmsoinc@mail2usa.com' not in readme:
    readme = readme.replace(
        'telephone (`(718) 921-9800`).',
        'telephone (`(718) 921-9800`), and office email (`pmsoinc@mail2usa.com`).'
    )
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme)
    print('Updated README.md with office email')

