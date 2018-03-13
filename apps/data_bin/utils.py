import collections


def vice_versa_map(dic={}):
    """

    """
    res = {}
    for key in dic:
        val = dic[key]
        for item in val:
            res[item] = key
    return res


def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        # new_key = parent_key + sep + k if parent_key else k
        new_key = k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def simplify_mapping(json_mapping):
    simple_map = {}
    for index_name in json_mapping:
        json_index = json_mapping[index_name]
        for table_name in json_index:
            json_table = json_index[table_name]
            for field_name in json_table:
                search_field_list = []
                field_mapping = json_table[field_name]
                for search_field_name in field_mapping['fields']:
                    search_field_list.append(search_field_name)
                simple_map[field_name] = search_field_list
    return simple_map


def enrich_data(json_item, simple_map={}):
    json_item_source = json_item['_source']
    json_item_new_source = {}
    for key in json_item_source:
        if key == 'LastName':
            print('ss')
        current_value = json_item_source[key]
        if current_value is not None and len(str(current_value)) > 0:

            json_item_new_source[key] = current_value
            if key in simple_map.keys():
                search_field_list = simple_map[key]
                for search_field in search_field_list:
                    if search_field in json_item_new_source.keys():
                        old_value = json_item_new_source[search_field]

                        # check if old value if list object
                        if isinstance(old_value, (list,)):
                            # check if current value exists in list
                            if current_value not in old_value:
                                old_value.append(current_value)
                        else:
                            # check if current value not equal with old value
                            if old_value != current_value:
                                json_item_new_source[search_field] = [old_value, current_value]
                    else:
                        json_item_new_source[search_field] = current_value

    return json_item_new_source
