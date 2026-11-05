import json

with open(r'c:\Users\aeyon\crystaltaxinc-clone\extracted_svgs.json', 'r', encoding='utf-8') as f:
    svgs = json.load(f)

icon_map = {}
for k, v in svgs.items():
    if 'facebook.com' in v or 'M22 12.061C22' in v:
        icon_map['facebook'] = v
    elif 'instagram.com' in v or 'M16.604 8.516' in v or '15.033a3.033' in v:
        icon_map['instagram'] = v
    elif 'twitter.com' in v or 'M23.954 4.569' in v or 'twitter' in v.lower():
        icon_map['twitter'] = v
    elif 'pinterest.com' in v or 'pinterest' in v.lower() or '12 0C5.373' in v:
        icon_map['pinterest'] = v
    elif 'yelp.com' in v or 'yelp' in v.lower():
        icon_map['yelp'] = v
    elif 'IconHamburger' in v:
        icon_map['hamburger'] = v
    elif 'CloseIcon' in v:
        icon_map['close'] = v
    elif k == 'plus' or 'plus' in v:
        icon_map['plus'] = v
    elif k == 'minus' or 'minus' in v:
        icon_map['minus'] = v

print('Mapped icons:')
for name in icon_map:
    print(f'  {name}: {icon_map[name][:60]}...')

with open(r'c:\Users\aeyon\crystaltaxinc-clone\icons_clean.json', 'w', encoding='utf-8') as f:
    json.dump(icon_map, f, indent=2)
