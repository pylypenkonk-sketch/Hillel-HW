number1 = float(input("Enter a number: "))
operation = input("Enter a operation: ")
number2 = float(input("Enter a number: "))

if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    if number2 != 0:
        result = number1 / number2
    else :
        result = 'Ділення на нуль неможливе'
else :
    result = 'Операція неможлива'

print(result)
