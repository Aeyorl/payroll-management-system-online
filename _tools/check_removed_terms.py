import re

with open('c:/Users/aeyon/payroll-management-system-online/locations.html', 'r', encoding='utf-8') as f:
    text = f.read()

terms = ['Utah', 'Florida', 'Puerto Rico', 'data-filter="ut"', 'data-filter="fl"', 'data-filter="pr"', 'data-region="ut"', 'data-region="fl"', 'data-region="pr"']
for t in terms:
    print(f"{t}: {text.count(t)}")

print("\n--- Filter Buttons ---")
btns = re.findall(r'<button type="button" class="location-filter-btn[^"]*"[^>]*>(.*?)</button>', text)
for b in btns:
    print(b)

cards = re.findall(r'<article class="location-card" data-region="([^"]+)"', text)
print(f"\nTotal location cards: {len(cards)}")
