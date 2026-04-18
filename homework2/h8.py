import os

# 1 пишем 3 строки в файл
print("задание 1")

# открываем файл на запись
f = open("data.txt", "w", encoding="utf-8")

for i in range(3):
    # ввод строки от юзера
    text = input("введи строку: ")
    
    # записываем в файл
    f.write(text + "\n")

# закрываем файл
f.close()

print("готово 1")


# 2 анализ слов в логе
print("\nзадание 2")

try:
    # читаем файл логов
    f = open("log.txt", "r", encoding="utf-8")
    text = f.read().lower()
    f.close()

    # режем на слова
    words = text.split()

    stats = {}

    # считаем сколько раз каждое слово встречается
    for w in words:
        if w in stats:
            stats[w] += 1
        else:
            stats[w] = 1

    # сортируем по частоте
    sorted_words = sorted(stats.items(), key=lambda x: x[1], reverse=True)

    # пишем топ 10 в файл
    f = open("word_stats.txt", "w", encoding="utf-8")

    for i in range(min(10, len(sorted_words))):
        word = sorted_words[i][0]
        count = sorted_words[i][1]
        f.write(word + " " + str(count) + "\n")

    f.close()

except:
    print("ошибка с файлами")

print("готово 2")


# 3 система заказов
print("\nзадание 3")

# добавление заказа
def add_order():
    # открываем файл в режим добавления
    f = open("orders.txt", "a", encoding="utf-8")

    num = input("номер заказа: ")
    name = input("товар: ")
    count = input("количество: ")
    price = input("цена: ")

    # записываем строку заказа
    f.write(num + "," + name + "," + count + "," + price + "\n")

    f.close()


# просмотр всех заказов
def show_orders():
    try:
        f = open("orders.txt", "r", encoding="utf-8")
        print(f.read())
        f.close()
    except:
        print("файл не найден")


# поиск заказа
def search_order():
    num = input("номер заказа: ")

    try:
        f = open("orders.txt", "r", encoding="utf-8")

        # ищем строку с номером
        for line in f:
            if line.startswith(num):
                print("найдено:", line)

        f.close()

    except:
        print("ошибка")


# обновление заказа
def update_order():
    num = input("номер заказа: ")
    new_lines = []

    try:
        f = open("orders.txt", "r", encoding="utf-8")

        # читаем и обновляем нужную строку
        for line in f:
            if line.startswith(num):
                parts = line.strip().split(",")

                # меняем количество и цену
                parts[2] = input("новое количество: ")
                parts[3] = input("новая цена: ")

                new_lines.append(",".join(parts) + "\n")
            else:
                new_lines.append(line)

        f.close()

        # перезаписываем файл
        f = open("orders.txt", "w", encoding="utf-8")
        f.writelines(new_lines)
        f.close()

    except:
        print("ошибка")


# удаление заказа
def delete_order():
    num = input("номер заказа: ")
    new_lines = []

    try:
        f = open("orders.txt", "r", encoding="utf-8")

        # пропускаем нужный заказ
        for line in f:
            if not line.startswith(num):
                new_lines.append(line)

        f.close()

        # переписываем файл без удалённого заказа
        f = open("orders.txt", "w", encoding="utf-8")
        f.writelines(new_lines)
        f.close()

    except:
        print("ошибка")


# меню
while True:
    print("\n1 добавить")
    print("2 показать")
    print("3 поиск")
    print("4 обновить")
    print("5 удалить")
    print("0 выход")

    c = input("выбор: ")

    if c == "1":
        add_order()

    elif c == "2":
        show_orders()

    elif c == "3":
        search_order()

    elif c == "4":
        update_order()

    elif c == "5":
        delete_order()

    elif c == "0":
        break

print("конец программы")