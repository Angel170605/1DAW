num_a = 0
num_b = 1

for _ in range(100):
    while _ != f'{num_a}' + f'{num_b}' + f'{num_b}':
        print(num_a)
        print(num_b)
        print(num_b)
    break
print(num_a + num_b)
