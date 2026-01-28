import json




def generate_mod_pool(all_mods, item):
    
    mod_pool = []

    for mod in all_mods:

        pool_dict= {}

        if mod['min_ilvl'] > item['ilvl']:
            continue

        effective_weight = 0

        default_weight = 0

        for i in mod['spawn_weights']:

            if i['tag'] == 'default':

                default_weight = i['weight']
                continue

            split_tag = i['tag'].split("_")

            if all(any(tag in item_t for item_t in item['tags']) for tag in split_tag):
                
                effective_weight = i['weight']
                tag = i['tag']
                break

        if effective_weight == 0 and default_weight > 0:
                
                effective_weight = default_weight

        if effective_weight == 0:

            continue

        pool_dict['id'] = mod['id']
        pool_dict['type'] = mod['type']
        pool_dict['effective_weight'] = effective_weight
        pool_dict['tag'] = tag
        pool_dict['group'] = mod['group']
        mod_pool.append(pool_dict)
        
    return mod_pool






