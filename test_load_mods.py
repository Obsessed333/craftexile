import json

with open("mods.json", encoding="utf-8") as f:
    mods = json.load(f)


print(type(mods))
print(len(mods))
first_key = next(iter(mods))
print(first_key)
print(mods[first_key].keys())