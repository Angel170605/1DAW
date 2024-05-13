n = int(input('Introduzca un número')) + 1
first_num = 1

for product in range(1, n):
    second_num = first_num + 1
    print(first_num**2 * second_num**2)
    first_num += 1
