operation = input('Introduzca su operación (separada por espacios)')
value_separation = operation.find(' ')
first_value = int(operation[:value_separation])
operator = operation[value_separation:value_separation]
second_value = int(operation[operator:])


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
