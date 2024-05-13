# ********************
# AQUÍ TIENE SU VUELTA
# ********************


def run(to_give_back: float, available_currencies: list) -> dict:
    
    money_back = {}
    money_rest = 0

    for currencie in (sorted(available_currencies))[::-1]:
        if to_give_back > 0:
            money_back[currencie] = (to_give_back // currencie) 
            to_give_back = to_give_back % currencie
        if to_give_back == 0:
            money_back == {}
            break

    return money_back


if __name__ == '__main__':
    run(20, [5, 2, 1])