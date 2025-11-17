import keyword
import string

var_name = input("Змінна: ")

punct = string.punctuation.replace("_", "")

if var_name in keyword.kwlist:
    print(False)
elif var_name and var_name[0].isdigit():
    print(False)
elif not all(ch.islower() or ch == "_" or ch.isdigit() for ch in var_name):
    print(False)
elif any(ch in punct for ch in var_name):
    print(False)
elif var_name.count("_") > 1:
    print(False)
else:
    print(True)