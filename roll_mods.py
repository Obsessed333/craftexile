from item_mod_pool_gen import generate_mod_pool
import json
import random



def roll_mods(mod_pool, item):
    for _ in range(3):
        eligible_mods = []
        for mod in mod_pool:
            if mod["type"] == "prefix":
                if item["prefix_count"] < 3 and mod['group'] not in item['blocked_groups']:
                        eligible_mods.append(mod)
            if mod["type"] == "suffix":
                if item["suffix_count"] < 3 and mod['group'] not in item['blocked_groups']:
                        eligible_mods.append(mod)
        if not eligible_mods:
            break
        mod_weights = [mod['effective_weight'] for mod in eligible_mods]
        selected_mod = random.choices(eligible_mods, weights=mod_weights, k = 1)[0]
        if selected_mod['type'] == "prefix":
                item['prefix_count'] += 1
        else:
                item["suffix_count"] += 1
        item['blocked_groups'].add(selected_mod['group'])
        item['rolled_mods'].append(selected_mod['id'])
    return item