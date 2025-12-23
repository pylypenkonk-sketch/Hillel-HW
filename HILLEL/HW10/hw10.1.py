def pow(x):
    return x ** 2

def some_gen(begin, n, func):
    value = begin
    for _ in range(n):
        yield value
        value = func(value)

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'

print('OK')
print(list(some_gen(1, 5, lambda x: x + 3)))
