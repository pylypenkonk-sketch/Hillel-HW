def is_palindrome(text):
    filtered = ''.join(c.lower() for c in text if c.isalnum())
    return filtered == filtered[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'

print("ОК")
print(is_palindrome("Was it a car or a cat I saw?"))
print(is_palindrome("hello"))
