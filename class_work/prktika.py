import random

#Завдання 1
num = int(input("Завдання 1 введіть число: "))
for i in range(1, 11):
    print(num, "*", i, "=", num * i)

print("\n....................\n")

#Завдання 2
print("завдання 2 таблиця множення від 1 до 9")
for i in range(1, 10):
    for j in range(1, 11):
        print(i, "*", j, "=", i * j)
    print()

print("\n...............\n")

#Завдання 3
n = int(input("завдання 3 скільки чисел ви хочете ввести? "))
max_num = None

for i in range(n):
    x = int(input("Введіть число: "))
    if max_num is None or x > max_num:
        max_num = x

print("Найбільше число:", max_num)

print("\n............\n")

#Завдання 4
print("завдання 4 гра 'Вгадай число'")
secret = random.randint(1, 500)
attempts = 0

while True:
    guess = int(input("введіть число (0 — вихід): "))

    if guess == 0:
        print("гру завершено")
        break

    attempts += 1

    if guess < secret:
        print("Загадане число більше")
    elif guess > secret:
        print("Загадане число менше")
    else:
        print("Ви вгадали число!")
        print("Кількість спроб:", attempts)
        break

print("\n.............\n")

#Завдання 5
print("завдання 5 малювання фігури")
figure = input("Введіть тип фігури (квадрат/прямокутник): ")

symbol = input("Введіть символ: ")

if figure == "квадрат":
    size = int(input("Введіть довжину сторони: "))
    for i in range(size):
        print(symbol * size)

elif figure == "прямокутник":
    width = int(input("Введіть ширину: "))
    height = int(input("Введіть висоту: "))
    for i in range(height):
        print(symbol * width)

else:
    print("Невірний тип фігури")