number1 = int(input("Enter a number: "))
operation = input("Enter an operation: ")
number2 = int(input("Enter another number: "))

if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2
elif operation == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        result = 'Ділення на 0 неможливе'
else:
    result = 'Операція неможлива'

print("Результат:", result)
