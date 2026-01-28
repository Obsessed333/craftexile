

def print_item(item, ALL_MODS_BY_ID):
    print(f"Rarity: {item['rarity'].capitalize()}")
    print(item["name"])
    print(f"Item Level: {item['ilvl']}")
    print()

    print("Mods:")
    for mod_id in item["rolled_mods"]:
        full_mod = ALL_MODS_BY_ID[mod_id]
        print(f" - {full_mod['name']} ({full_mod['groups']})")