import os, re

base_dir = r'c:\Users\aeyon\crystaltaxinc-clone'
files = [
    'index.html',
    'about-us.html',
    'tax-services.html',
    'payroll-services.html',
    'accounting-services.html',
    'contact-us.html',
    'README.md'
]

found = 0
for rel in files:
    path = os.path.join(base_dir, rel)
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for idx, line in enumerate(lines, 1):
        if re.search(r'href=["\']tel:|921-9800|\(718\)|7189219800', line, re.I):
            print(f'Remaining in {rel}:{idx}: {line.strip()[:100]}')
            found += 1

if found == 0:
    print('SUCCESS: Zero phone numbers or tel: links remain anywhere in the project!')
else:
    print(f'Total found: {found}')

