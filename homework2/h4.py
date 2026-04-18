import random

# степень рекурсия
def power(a, n):
    # база чтоб не улететь в бесконечность
    if n == 0:
        return 1
    
    # если минус переворачиваем число
    if n < 0:
        return 1 / power(a, -n)
    
    # просто жмем дальше рекурсию
    return a * power(a, n - 1)


# проверка високосного года
def is_leap(y):
    # если год норм чет по правилам значит ок
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


def days_in_month(m, y):
    # тупо список дней по месяцам
    d = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    # если февраль и год норм даем плюс день
    if m == 2 and is_leap(y):
        return 29
    
    return d[m - 1]


def date_to_days(d, m, y):
    # переводим дату в общие дни типа счетчик времени
    total = 0
    
    # пробегаем все годы считаем дни
    for i in range(y):
        total += 366 if is_leap(i) else 365
    
    # добиваем месяцы
    for i in range(1, m):
        total += days_in_month(i, y)
    
    # и дни докидываем
    total += d
    return total


def date_diff(d1, m1, y1, d2, m2, y2):
    # просто разница без заморочек
    return abs(date_to_days(d1, m1, y1) - date_to_days(d2, m2, y2))


# ищем где самое выгодное окно из 10 чисел
def min_sum_index(arr, i=0, best_sum=10**9, best_i=0):
    # дошли до конца стопаемся
    if i > len(arr) - 10:
        return best_i
    
    # считаем кусок из 10
    s = sum(arr[i:i+10])
    
    # если лучше запоминаем позицию
    if s < best_sum:
        best_sum = s
        best_i = i
    
    # двигаемся дальше
    return min_sum_index(arr, i+1, best_sum, best_i)


# меню чтоб юзер не потерялся
while True:
    print("\n меню")
    print("1 степень")
    print("2 даты")
    print("3 массив")
    print("0 выход")

    choice = input("выбирай ")

    if choice == "1":
        a = float(input("число "))
        n = int(input("степень "))
        print("ответ", power(a, n))

    elif choice == "2":
        print("первая дата")
        d1, m1, y1 = map(int, input().split())
        print("вторая дата")
        d2, m2, y2 = map(int, input().split())
        print("разница", date_diff(d1, m1, y1, d2, m2, y2))

    elif choice == "3":
        arr = [random.randint(1, 100) for _ in range(100)]
        print("массив готов")
        print("старт индекс", min_sum_index(arr))

    elif choice == "0":
        print("вышел")
        break

    else:
        print("не понял попробуй еще раз")