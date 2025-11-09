symbol = input('через пробіл')

if symbol.strip() == '':
    lst = []
else:
    lst = [int(x) for x  in symbol.split()]

if not lst:
    result = [[], []]
else:
    mid = (len(lst) + 1) // 2
    result = [lst[:mid], lst[mid:]]

print(result)