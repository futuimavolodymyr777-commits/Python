# задание 1
s = input("введи строку: ")

letters = 0
digits = 0

for i in s:
    if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        letters += 1
    if i >= '0' and i <= '9':
        digits += 1

print("буквы:", letters)
print("цифры:", digits)


# задание 2
x = input("введи символ: ")

count = 0
for i in s:
    if i == x:
        count += 1

print("символ встречается:", count)


# задание 3
rev = ""
for i in s:
    rev = i + rev

print("перевёрнутая строка:", rev)


# задание 4
w = input("введи слово для поиска: ")

count = 0
word = ""

for i in s + " ":
    if i != " ":
        word += i
    else:
        if word == w:
            count += 1
        word = ""

print("слово встречается:", count)


# задание 5
old = input("слово для замены: ")
new = input("новое слово: ")

result = ""
word = ""

for i in s + " ":
    if i != " ":
        word += i
    else:
        if word == old:
            result += new + " "
        else:
            result += word + " "
        word = ""

print("после замены:", result)


# задание 6
longest = ""
word = ""

for i in s + " ":
    if i != " ":
        word += i
    else:
        if len(word) > len(longest):
            longest = word
        word = ""

print("самое длинное слово:", longest)
