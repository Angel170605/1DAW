first_value = int(input('Introduzca un valor'))
second_value = int(input('Introduzca otro valor'))
operator = input('Introduzca un operador')


match operator:
    case '+':
        print(first_value + second_value)
    case '-':
        print(first_value - second_value)
    case '*':
        print(first_value * second_value)
    case '/':
        print(first_value / second_value)
    case '**':
        print(first_value**second_value)
    case _:
        print('Introduzca otro operador')
