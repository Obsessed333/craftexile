import json
from mod_filter import filter_mods
from item_mod_pool_gen import generate_mod_pool
from roll_mods import roll_mods
from generate_random_item import generate_item, filter_items


def main():

    with open("mods.json", encoding="utf-8") as f:
        raw_mods = json.load(f)
    
    with open("base_items.json", encoding="utf-8") as f:
        raw_items = json.load(f)
    

    filtered_mods = filter_mods(raw_mods)
    filtered_items = filter_items(raw_items)

    item = generate_item(filtered_items)

    mod_pool = generate_mod_pool(filtered_mods, item)

    rolled_item = roll_mods(mod_pool, item)

    print(rolled_item)

if __name__ == "__main__":
    main()