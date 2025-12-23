def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

name = input("Введіть своє ім'я: ")
age = int(input("Введіть свій вік: "))

print(say_hi(name, age))
