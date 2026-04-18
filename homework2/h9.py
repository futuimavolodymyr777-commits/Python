import random
import string

def draw_header():
    print("=" * 50)
    print("СУПЕР ГРА 2067".center(50))
    print("=" * 50)


def draw_menu():
    print("Оберіть дію:")
    print("[ 1 ] Нова гра")
    print("[ 2 ] Завантажити збереження")
    print("[ 3 ] Вихід")
    print("=" * 50)


def make_nicks(name):
    nick1 = name + str(random.randint(100, 9999))

    sep = random.choice(["_", ".", "-"])
    letters = "".join(random.choices(string.ascii_lowercase, k=3))
    nick2 = name + sep + letters

    prefixes = ["Pro", "Super", "Ultra"]
    prefix = random.choice(prefixes)
    nick3 = name.capitalize() + prefix + str(random.randint(10, 99))

    return nick1, nick2, nick3


# старт экрана
draw_header()
draw_menu()

choice = input("Ваш вибір: ")

if choice == "1":
    name = input("Введіть ім'я: ")
    n1, n2, n3 = make_nicks(name)

    print("\nВаші ніки:")
    print(n1)
    print(n2)
    print(n3)

elif choice == "2":
    print("Завантаження... (поки пусто)")

elif choice == "3":
    print("Вихід...")

else:
    print("Невірний вибір")