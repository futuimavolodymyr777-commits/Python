# задание 1 считаем сумму и среднее
nums = list(map(int, input("введи числа через пробел ").split()))

total = sum(nums)  # считаем всю сумму
avg = total / len(nums) if nums else 0  # среднее если список не пустой

print("сумма =", total)
print("среднее =", avg)


# задание 2 считаем сколько раз число встречается
nums = list(map(int, input("введи числа ").split()))
x = int(input("какое число ищем "))

count = nums.count(x)  # тупо считаем сколько раз есть

print("встречается раз =", count)


# задание 3 сумма всех плюсовых чисел
nums = list(map(int, input("введи числа ").split()))

pos_sum = sum(n for n in nums if n > 0)  # берем только плюсики

print("сумма плюсов =", pos_sum)


# задание 4 индексы четных чисел
nums = list(map(int, input("введи числа ").split()))

indexes = []  # сюда кидаем индексы

for i, n in enumerate(nums):
    if n % 2 == 0:
        indexes.append(i)  # если четное записали индекс

print("индексы четных =", indexes)


# задание 5 убираем дубли
nums = list(map(int, input("введи числа ").split()))

unique = list(set(nums))  # убрали повторки через сет

print("уникальные =", unique)