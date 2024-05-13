import sys

nums = [int(num) for num in sys.argv[1:]]

calc = (sum(nums)) / len(nums)
print(f'{round(calc, 2)}')
