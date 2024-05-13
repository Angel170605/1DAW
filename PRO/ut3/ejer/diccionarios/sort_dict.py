# *********************
# ORDENE MI DICCIONARIO
# *********************


def run(unsorted_items: dict) -> list:
   sorted_keys = []
   sorted_values = sorted(item for item in items.values())

   for key, value in unsorted_items.items():
        for s_value in sorted_values:
            if s_value == value:
                sorted_keys.append()


    sorted_items = ((s_key, s_val) for s_key, s_val in zip(sorted_keys, sorted_values)) 

    return sorted_items


if __name__ == '__main__':
    run({'a': 'two', 'b': 'one', 'c': 'three'})