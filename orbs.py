from item_mod_pool_gen import generate_mod_pool
from roll_mods import roll_mods
import random

def use_transmute(item, filtered_mods):
    if item['rarity'] != "normal":
        return None
    item["prefix_count"] = 0
    item["suffix_count"] = 0
    item["blocked_groups"] = set()
    item["rolled_mods"] = []
    item["rarity"] = "magic"

    mod_pool = generate_mod_pool(filtered_mods, item)
    num_mods = random.randint(1,2)
    return roll_mods(mod_pool, item, num_mods)

def use_chaos(item, filtered_mods):
    if item['rarity'] != "rare":
        return None
    item["prefix_count"] = 0
    item["suffix_count"] = 0
    item["blocked_groups"] = set()
    item["rolled_mods"] = []
    num_mods = random.randint(3,6)

    mod_pool = generate_mod_pool(filtered_mods, item)
    return roll_mods(mod_pool, item, num_mods)

def use_alchemy(item, filtered_mods):
    if item['rarity'] != 'normal':
        return None

    item['rarity'] = 'rare'
    item["prefix_count"] = 0
    item["suffix_count"] = 0
    item["blocked_groups"] = set()
    item["rolled_mods"] = []

    mod_pool = generate_mod_pool(filtered_mods, item)
    num_mods = random.randint(3, 6)
    return roll_mods(mod_pool, item, num_mods)

def use_alteration(item, filtered_mods):
    if item['rarity'] != 'magic':
        return None
    
    item['rarity'] = 'magic'
    item["prefix_count"] = 0
    item["suffix_count"] = 0
    item["blocked_groups"] = set()
    item["rolled_mods"] = []

    mod_pool = generate_mod_pool(filtered_mods, item)
    num_mods = random.randint(1,2)
    return roll_mods(mod_pool, item, num_mods)