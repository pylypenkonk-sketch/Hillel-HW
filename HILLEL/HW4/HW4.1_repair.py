numbers = input('Введіть список чисел через пробіл: ')
lst = [int(x) for x in numbers.split()]

insert_pos = 0
for num in lst:
    if num != 0:
        lst[insert_pos] = num
        insert_pos += 1
while insert_pos < len(lst):
    lst[insert_pos] = 0
    insert_pos += 1

print(lst)
