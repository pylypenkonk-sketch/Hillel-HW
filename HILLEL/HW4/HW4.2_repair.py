numbers = input('Введіть список чисел через пробіл: ')
lst = [int(x) for x in numbers.split()]

if not lst:
    result = 0
else:
    total = sum(lst[x] for x in range(0, len(lst), 2))
    result = total * lst[-1]

print(result)
