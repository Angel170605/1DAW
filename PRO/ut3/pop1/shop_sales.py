# *******************************
# VENTAS EN TIENDA DE INFORMÁTICA
# *******************************


def run(sales: list) -> tuple:
    pcs_sales = []
    displays_sales = []
    for sale in range(len(sales)):
        pcs_sales.append(sales[sale][0])
        displays_sales.append(sales[sale][1])

    pcs = sum(pcs_sales)
    displays = sum(displays_sales)

    return pcs, displays


if __name__ == '__main__':
    run([[4, 5], [1, 3], [3, 2]])