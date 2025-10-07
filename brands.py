import csv
from collections import Counter

cnt = Counter()

emoji = {
    "australia": "🇦🇺",
    "austria": "🇦🇹",
    "belgium": "🇧🇪",
    "canada": "🇨🇦",
    "china": "🇨🇳",
    "czech republic": "🇨🇿",
    "denmark": "🇩🇰",
    "finland": "🇫🇮",
    "france": "🇫🇷",
    "germany": "🇩🇪",
    "iceland": "🇮🇸",
    "indonesia": "🇮🇩",
    "ireland": "🇮🇪",
    "israel": "🇮🇱",
    "italy": "🇮🇹",
    "japan": "🇯🇵",
    "nepal": "🇳🇵",
    "netherlands": "🇳🇱",
    "new zealand": "🇳🇿",
    "norway": "🇳🇴",
    "slovenia": "🇸🇮",
    "spain": "🇪🇸",
    "sweden": "🇸🇪",
    "switzerland": "🇨🇭",
    "taiwan": "🇹🇼",
    "united states": "🇺🇸",
    "united kingdom": "🇬🇧",
    "south africa": "🇿🇦",
    "south korea": "🇰🇷",
}

results = []
with open("data/brands.csv") as f:
    reader = csv.DictReader(f, fieldnames=["brand", "country", "url"])
    for (k, row) in enumerate(reader):
        if not k: continue
        if not row["country"]: continue
        cnt.update([row["country"],])
        results.append(row)

results.sort(key=lambda x: x["brand"])

out = []

out.append("""
### <a id="companies">List of companies</a>

|US or not?|Company|Located|Site|
|-|-|-|-|""")
for result in results:
    good = "❌" if result["country"].lower() == "united states" else "✅"
    emo = emoji[result["country"].lower()]
    out.append(f'|{good}|{result["brand"]}|{emo} {result["country"]}|<a target="_blank" href="{result['url']}" title="Website">➡️</a>|')

out.append("""
### Count of countries

|Country|Count|
|-|-|""")

for (country, count) in sorted(cnt.items()):
    emo = emoji[country.lower()]
    out.append(f"|{emo} {country}|{count}|")

inlines = []
with open("content/2025-09-30-nationality-of-companies.md", "r") as infile:
    for line in infile.readlines():
        if line.startswith("### <a id"):
            break
        if line.endswith("\n"):
            line = line.strip()
        inlines.append(line)

outlines = inlines + out
with open("content/2025-09-30-nationality-of-companies.md", "w") as outfile:
    outfile.write("\n".join(outlines))
