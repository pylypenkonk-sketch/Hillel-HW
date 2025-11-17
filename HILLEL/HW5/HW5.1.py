import keyword
import string

var_name = input("Змінна: ")

if not var_name:
    print(False)

elif keyword.iskeyword(var_name):
    print(False)

elif var_name[0].isdigit():
    print(False)

elif any(ch.isupper() for ch in var_name):
    print(False)

elif " " in var_name:
    print(False)

elif any(ch in string.punctuation.replace("_", "") for ch in var_name):
    print(False)

elif all(ch == "_" for ch in var_name) and len(var_name) > 1:
    print(False)

elif not all(ch.islower() or ch.isdigit() or ch == "_" for ch in var_name):
    print(False)

else:
    print(True)
