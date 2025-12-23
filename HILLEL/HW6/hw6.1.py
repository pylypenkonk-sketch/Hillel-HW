import string

s = input("Введіть літери через дефіс: ").strip()
start, end = s.split('-')

letters = (
    string.ascii_letters +
    "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
)

i1 = letters.index(start)
i2 = letters.index(end)

print(letters[i1:i2 + 1])

