import json
import random




def filter_items(raw_items):
        
    filter = {}

    for key, value in raw_items.items():
          if value.get("domain") == 'item' and value.get('release_state') == 'released':
                filter[key] = value

    dict_list = []
    for key, value in filter.items():
          temp_dict = {}
          temp_dict['name'] = value['name']
          temp_dict['drop_level'] = value['drop_level']
          temp_dict['requirements'] = value['requirements']
          temp_dict['tags'] = value['tags']
          dict_list.append(temp_dict)

    with open('filtered_items', 'w') as json_file:
            json.dump(dict_list, json_file, indent= 3)
    
    return dict_list



def generate_item(filtered_items):
      
      random_item = random.choice(filtered_items)
      
      item = {
            'name': random_item['name'],
            'ilvl': random.randint(random_item['drop_level'], 100),
            'tags': random_item['tags'],
            'prefix_count': 0,
            'suffix_count': 0,
            'blocked_groups': set(),
            'rolled_mods': [],
      }
      if item['name'] == 'Energy Blade':
            return generate_item(filtered_items)
      return item

