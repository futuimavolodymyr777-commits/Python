# задание 1 словарь переводов
def task1():
    # создаем словарь
    dictionary = {
        "cat": "кіт",
        "dog": "собака",
        "house": "будинок",
        "car": "авто",
        "tree": "дерево"
    }
    
    # ввод слова
    word = input("введи слово на английском: ").lower()
    
    # проверка есть ли слово
    if word in dictionary:
        print("перевод:", dictionary[word])
    else:
        print("слово не найдено")


# задание 2 общие игры
def task2():
    # ввод количества друзей
    n = int(input("сколько друзей: "))
    
    # ввод игр пользователя
    user_games = set(input("твои игры через пробел: ").split())
    
    # изначально считаем что все могут играть в твои игры
    common_games = user_games
    
    # ввод игр друзей
    for i in range(n):
        friend_games = set(input(f"игры друга {i+1}: ").split())
        
        # находим пересечение
        common_games = common_games & friend_games
    
    # вывод результата
    if common_games:
        print("все могут играть в:", list(common_games))
    else:
        print("нет общих игр")


# меню
def menu():
    while True:
        print("\n1 задание 1")
        print("2 задание 2")
        print("0 выход")
        
        ch = input("выбор: ")
        
        if ch == "1":
            task1()
        elif ch == "2":
            task2()
        elif ch == "0":
            print("выход")
            break
        else:
            print("ошибка")


menu()