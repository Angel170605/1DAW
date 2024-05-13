# ***************
# APLANA LA LISTA
# ***************


def run(elements: list) -> list:
    flatten_elements = []
    for element in elements:
        if element == int:
            flatten_elements.append(int(element))
        if isinstance(element, list):
            for num in element:
                flatten_elements.append(num)
        else:
            flatten_elements.append(element)

    return flatten_elements


if __name__ == '__main__':
    run([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])
