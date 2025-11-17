import string

text = input("Введіть рядок: ")

clean = "".join(ch for ch in text if ch not in string.punctuation)

words = clean.split()

hashtag = "#" + "".join(word.capitalize() for word in words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
