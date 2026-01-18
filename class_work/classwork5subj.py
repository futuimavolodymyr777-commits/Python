print("меню")
print("1 оцінка за іспит")
print("2 премія за стаж")
print("3 сума цифр парна або непарна")
print("4 щасливе шестизначне число")
print("5 обмін цифр у шестизначному числі")

choice = int(input("виберіть номер завдання "))

# завдання 1
if choice == 1:
    score = int(input("введіть бал від 0 до 100 "))

    if score < 0 or score > 100:
        print("помилка бал має бути від 0 до 100")
    elif score >= 90:
        print("відмінно")
    elif score >= 70:
        print("добре")
    elif score >= 50:
        print("задовільно")
    else:
        print("незадовільно")

# завдання 2
elif choice == 2:
    salary = float(input("введіть зарплату "))
    experience = float(input("введіть стаж роботи "))

    if experience < 1:
        print("премія не передбачена")
    elif experience < 3:
        print("премія", salary * 0.05)
    elif experience < 5:
        print("премія", salary * 0.10)
    else:
        print("премія", salary * 0.15)

# завдання 3
elif choice == 3:
    number = int(input("введіть чотиризначне число "))

    a = number // 1000
    b = number // 100 % 10
    c = number // 10 % 10
    d = number % 10

    sum_digits = a + b + c + d

    if sum_digits % 2 == 0:
        print("сума цифр парна")
    else:
        print("сума цифр непарна")

# завдання 4
elif choice == 4:
    number = int(input("введіть шестизначне число "))

    if number < 100000 or number > 999999:
        print("помилка це не шестизначне число")
    else:
        a = number // 100000
        b = number // 10000 % 10
        c = number // 1000 % 10
        d = number // 100 % 10
        e = number // 10 % 10
        f = number % 10

        if a + b + c == d + e + f:
            print("число щасливе")
        else:
            print("число нещасливе")

# завдання 5
elif choice == 5:
    number = int(input("введіть шестизначне число "))

    if number < 100000 or number > 999999:
        print("помилка це не шестизначне число")
    else:
        a = number // 100000
        b = number // 10000 % 10
        c = number // 1000 % 10
        d = number // 100 % 10
        e = number // 10 % 10
        f = number % 10

        new_number = f * 100000 + e * 10000 + c * 1000 + d * 100 + b * 10 + a
        print("результат", new_number)

else:
    print("невірний вибір пункту меню")