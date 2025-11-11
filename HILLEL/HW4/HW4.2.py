def sum_indexes(lst):
    if not lst:
        return 0

    total = sum(lst[x] for x in range (0, len(lst), 2))

    result = total * lst[-1]

    return result

numbers = input('Введіть список чисел через пробіл: ')
lst = [int(x) for x in numbers.split()]
result = sum_indexes(lst)

print(result)