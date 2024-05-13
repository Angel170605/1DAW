value_1 = input('intoduzca el primer valor')
value_2 = input('introduzca el segundo valor')
value_3 = input('introduzca el tercer valor')

if value_1 < value_2:
    if value_1 < value_3:
        print(f'{value_1}')
    if value_3 < value_1:
        print(f'{value_3}')
    else:
        print(f'{value_2}')
if value_2 < value_1:
    if value_2 < value_3:
        print(f'{value_2}')
    if value_3 < value_2:
        print(f'{value_3}')
    else:
        print(f'{value_1}')
