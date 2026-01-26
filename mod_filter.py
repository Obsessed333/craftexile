import json

with open("mods.json", encoding="utf-8") as f:
    raw_mods = json.load(f)

filtered = {}

for mod_id, mod in raw_mods.items():
    gen_type = mod.get("generation_type")
    if mod.get("domain") == "item" and gen_type in ("prefix", "suffix"):
        filtered[mod_id] = mod

dict_list = []
for key, value in filtered.items():
    temp_dict = {}
    temp_dict["id"] = key
    temp_dict["name"] = value["name"]
    temp_dict["type"] = value["generation_type"]
    temp_dict["group"] = value["groups"][0]
    temp_dict["min_ilvl"] = value["required_level"]
    temp_dict["weight"] = 0
    for item in value["spawn_weights"]:
        if item["tag"] == "default":
            temp_dict["weight"] = item["weight"]
    dict_list.append(temp_dict)

with open('normalized_mods.json', 'w') as json_file:
        json.dump(dict_list, json_file, indent= 3) 
    
print(filtered["ColdDamagePercent6"])
   


        