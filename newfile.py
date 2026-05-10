import requests
import json

# 1. API-ൽ നിന്ന് മലയാളം stations എടുക്കുന്നു
url = "https://de1.api.radio-browser.info/json/stations/search"
params = {"language": "malayalam", "limit": 500, "hidebroken": True}
stations = requests.get(url, params=params).json()

# 2. Duplicate ഒഴിവാക്കുന്നു - name + stream url നോക്കി
seen = set()
clean_data = []
for s in stations:
    key = (s['name'].strip().lower(), s['url_resolved'])
    if key not in seen and s['url_resolved']: # URL ഉള്ളത് മാത്രം
        seen.add(key)
        clean_data.append({
            "name": s['name'].strip(),
            "url": s['url_resolved'],
            "homepage": s['homepage'],
            "country": s['country'],
            "state": s['state'],
            "tags": s['tags'],
            "bitrate": s['bitrate'],
            "codec": s['codec']
        })

# 3. Name അനുസരിച്ച് sort ചെയ്ത് save ചെയ്യുന്നു
clean_data = sorted(clean_data, key=lambda x: x['name'].lower())

with open('malayalam_stations_with_url.json', 'w', encoding='utf-8') as f:
    json.dump(clean_data, f, ensure_ascii=False, indent=2)

print(f"Total unique stations: {len(clean_data)}")
print("Saved to malayalam_stations_with_url.json")
import json
