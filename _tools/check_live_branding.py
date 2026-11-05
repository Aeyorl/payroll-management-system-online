import urllib.request
import re

pages = ['index.html', 'about-us.html', 'tax-services.html', 'payroll-services.html', 'accounting-services.html', 'contact-us.html']
for page in pages:
    url = f'http://localhost:3000/{page}'
    html = urllib.request.urlopen(url).read().decode('utf-8')
    title = re.search(r'<title>(.*?)</title>', html).group(1)
    brand = re.search(r'class="brand-name">([^<]+)', html)
    print(f'{page}: Title="{title}" | Brand="{brand.group(1) if brand else "None"}"')

