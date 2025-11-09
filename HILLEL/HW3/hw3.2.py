symbol = input('через пробіл: ')
lst = [str(x) for x in symbol.split()] # float int також працюють

if lst and lst != [lst[-1]]:
    lst = [lst[-1]] + lst[:-1]

print(lst)
