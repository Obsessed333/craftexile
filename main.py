import json
from mod_filter import filter_mods
from item_mod_pool_gen import generate_mod_pool
from roll_mods import roll_mods
from generate_random_item import generate_item, filter_items
from orbs import use_alchemy, use_alteration, use_chaos, use_transmute, use_scouring
from print import print_item


def main():
    global ALL_MODS_BY_ID
    with open("mods.json", encoding="utf-8") as f:
        raw_mods = json.load(f)
    
    with open("base_items.json", encoding="utf-8") as f:
        raw_items = json.load(f)
    
    ALL_MODS_BY_ID = raw_mods
    
    filtered_mods = filter_mods(raw_mods)
    filtered_items = filter_items(raw_items)

    current_item = None

    while True:
        print ("\n=== Crafting CLI ===")
        print("G) Generate new base item")
        print("T) Use Transmute")
        print("A) Use Alteration")
        print("L) Use Alchemy")
        print("C) Use Chaos")
        print("X) Use Scouring")
        print("S) Show current item")
        print("Q) Quit")

        choice = input("> ").strip().lower()

        if choice == "q":
            break
        
        elif choice == "g":
            current_item = generate_item(filtered_items)
            current_item["rarity"] = "normal"
            current_item["prefix_count"] = 0
            current_item["suffix_count"] = 0
            current_item["blocked_groups"] = set()
            current_item["rolled_mods"] = []
            print_item(current_item, ALL_MODS_BY_ID)

        elif choice == "s":
            if current_item == None:
                print('No item yet. Generate one first')
            else:
                print_item(current_item, ALL_MODS_BY_ID)
        elif choice =="t":
            if current_item == None:
                print('No item yet. Generate one first')
                continue
            new_item = use_transmute(current_item, filtered_mods)
            if new_item is None:
                print("Transmute can only be used on normal items.")
            else:
                current_item = new_item
                print_item(current_item, ALL_MODS_BY_ID)
        
        elif choice =="l":
            if current_item == None:
                print('No item yet. Generate one first')
                continue
            new_item = use_alchemy(current_item, filtered_mods)
            if new_item is None:
                print("Alchemy can only be used on rare items.")
            else:
                current_item = new_item
                print_item(current_item, ALL_MODS_BY_ID)
        
        elif choice =="c":
            if current_item == None:
                print('No item yet. Generate one first')
                continue
            new_item = use_chaos(current_item, filtered_mods)
            if new_item is None:
                print("Chaos can only be used on rare items.")
            else:
                current_item = new_item
                print_item(current_item, ALL_MODS_BY_ID)
        
        elif choice =="a":
            if current_item == None:
                print('No item yet. Generate one first')
                continue
            new_item = use_alteration(current_item, filtered_mods)
            if new_item is None:
                print("Alteration can only be used on magic items.")
            else:
                current_item = new_item
                print_item(current_item, ALL_MODS_BY_ID)
        
        elif choice =="x":
            if current_item == None:
                print('No item yet. Generate one first')
                continue
            new_item = use_scouring(current_item)
            if new_item is None:
                print("Scouring can only be used in magic or rare items.")
            else:
                current_item = new_item
                print_item(current_item, ALL_MODS_BY_ID)


    

if __name__ == "__main__":
    main()