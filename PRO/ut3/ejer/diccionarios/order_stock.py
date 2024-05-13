# ***********
# ¿HAY STOCK?
# ***********


def run(stock: dict, merch: str, amount: int) -> bool:
    available = ''
    for key, value in stock.items():
        if merch not in stock.keys():
            available = False
        else:
            if key == merch:
                if value >= amount:
                    available = True
                if value < amount:
                    available = False


    return available


if __name__ == '__main__':
    run({'pen': 20, 'cup': 11, 'keyring': 40}, 'cup', 9)