import urllib.request
import ssl

ctx = ssl.create_default_context()

urls = [
    'https://www.pmso.live/locations',
    'https://payroll-management-system-online.vercel.app/locations',
    'https://www.pmso.live/',
    'https://www.pmso.live/about-us'
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, context=ctx) as resp:
            body = resp.read().decode('utf-8', errors='replace')
            title = ''
            if '<title>' in body:
                title = body.split('<title>')[1].split('</title>')[0]
            loc_count = body.count('location-card')
            print(f"[{resp.status}] {url}")
            print(f"      Title: {title}")
            if 'locations' in url:
                print(f"      Location Cards: {loc_count}")
    except Exception as e:
        print(f"[ERR] {url} -> {e}")
