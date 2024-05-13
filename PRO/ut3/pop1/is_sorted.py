# ***************
# ¿ESTÁ ORDENADO?
# ***************


def run(items: list) -> bool:
    items_sorted = True
    last_element = len(items)
    before_last_element = last_element - 1
    while before_last_element >= 0  and before_last_element > 0:
        if before_last_element > 0 or len(items) == 1 or len(items) == 0:
            items_sorted = True
            break
        if items[last_element] > items[before_last_element]:
            last_element -= 1
            before_last_element -= 1
            continue
            if before_last_element == 0:
                items_sorted = True
                break
            if items[last_element] < items[before_last_element]:
                items_sorted = False
                break 


    return items_sorted


if __name__ == '__main__':
    run(['a', 'f', 't'])