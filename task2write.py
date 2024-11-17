import shelve

countryDict = {
    "Germany": 83783942,
    "France": 67564251,
    "United Kingdom": 67215293,
    "Italy": 59257566,
    "Spain": 47450795,
    "Poland": 37797258,
    "Netherlands": 17331239,
    "Belgium": 11668278,
    "Sweden": 10310365,
    "Austria": 8955102,
    "Switzerland": 8705288,
    "Portugal": 10305564,
    "Greece": 10375172,
    "Czech Republic": 10553843
}

average = sum(countryDict.values()) / len(countryDict.values())
filtered = dict((k, v) for k, v in countryDict.items() if v > average)
print("Writing:")
print(filtered)

with shelve.open("db.db") as db:
    db["countries"] = list(filtered.keys())
    db["populations"] = list(filtered.values())
