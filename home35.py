print("1 - степінь")
print("2 - fizz buzz")
print("3 - обід")

n = int(input())

# завдання 1
if n == 1:
    a = int(input("введіть число: "))
    b = int(input("введіть степінь: "))
    print(a ** b)

# завдання 2
elif n == 2:
    x = int(input("введіть число від 1 до 100: "))

    if x % 15 == 0:
        print("fizz buzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)

# завдання 3
elif n == 3:
    total = 0

    snack = input("закуска (салат/суп/ні): ")
    main = input("основна страва (курка/риба/ні): ")
    dessert = input("десерт (морозиво/фрукти/ні): ")

    if snack == "салат":
        total += 5
    elif snack == "суп":
        total += 7

    if main == "курка":
        total += 10
    elif main == "риба":
        total += 12

    if dessert == "морозиво":
        total += 3
    elif dessert == "фрукти":
        total += 4

    # знижка за всі три позиції
    if snack != "ні" and main != "ні" and dessert != "ні":
        total = total * 0.9

    # знижка якщо сума > 20
    if total > 20:
        total = total * 0.85

    print("підсумкова вартість:", total)