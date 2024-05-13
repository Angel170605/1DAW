num = int(input('Introduzca un número'))
n_multiples = num // 3
multiples = num // n_multiples

for _ in range(n_multiples):
    print(multiples)
    multiples += 3
    if n_multiples >= num:
        break
