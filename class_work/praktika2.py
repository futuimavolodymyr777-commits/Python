#завдання 1
print("завдання 1")
height = int(input("введіть висоту прямокутника: "))
width = int(input("введіть ширину прямокутника: "))

for i in range(height):
    print("*" * width)

print("\nBOOOOOOM SHAKALAKA\n")

#завдання 2
print("завдання 2")
figure = input("введіть тип фігури (квадрат / прямокутник): ")
symbol = input("введіть символ: ")

if figure == "квадрат":
    size = int(input("введіть довжину сторони: "))
    for i in range(size):
        print(symbol * size)

elif figure == "прямокутник":
    height = int(input("введіть висоту: "))
    width = int(input("введіть ширину: "))
    for i in range(height):
        print(symbol * width)

else:
    print("невірний тип фігури")

print("\nBOOOOOOM SHAKALAKA\n")

#завдання 3
print("завдання 3")
size = int(input("введіть розмір сторони квадрата: "))

for i in range(size):
    if i == 0 or i == size - 1:
        print("*" * size)
    else:
        print("*" + " " * (size - 2) + "*")

print("\nBOOOOOOM SHAKALAKA\n")

#завдання 4
print("завдання 4")
height = int(input("введіть висоту прямокутника: "))
width = int(input("введіть ширину прямокутника: "))

for i in range(height):
    if i == 0 or i == height - 1:
        print("*" * width)
    else:
        print("*" + " " * (width - 2) + "*")

print("\nBOOOOOOM SHAKALAKA\n")

#завдання 5
print("завдання 5")
height = int(input("введіть висоту трикутника: "))
symbol = input("введіть символ: ")

for i in range(1, height + 1):
    print(symbol * i)

print("\nBOOOOOOM SHAKALAKA\n")

#завдання 6
print("завдання 6")
height = int(input("введіть висоту трикутника: "))
symbol = input("введіть символ: ")

for i in range(height):
    spaces = height - i - 1
    symbols = 2 * i + 1
    print(" " * spaces + symbol * symbols)