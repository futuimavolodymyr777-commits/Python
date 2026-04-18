class Book:
    def __init__(self, title, authors, year):
        # создаем книжку закидываем туда название авторов и годик
        self.title = title
        self.authors = authors
        self.year = year

    def __str__(self):
        # как эта книжка будет выглядеть если ее вывести
        return f"{self.title} {self.year} {' '.join(self.authors)}"


class Library:
    def __init__(self, name, address):
        # делаем библиотеку имя адрес и пустой склад книг
        self.name = name
        self.address = address
        self.books = []

    def __str__(self):
        # инфа по библиотеке чисто для понтов
        return f"{self.name} {self.address}"

    def show_books(self):
        # если книг нет то грустим если есть показываем
        if not self.books:
            print("пусто брат книг нет")
        else:
            for i, book in enumerate(self.books, 1):
                print(i, book)

    def add_book(self, book):
        # кидаем книжку в коллекцию
        self.books.append(book)
        print("забросили книгу норм")

    def remove_book(self, title):
        # ищем книгу по названию и выкидываем если нашли
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("книгу снесли")
                return
        print("не нашли такую брат")

    def find_by_title(self, title):
        # ищем по названию типа совпадение по кусочку строки
        return [b for b in self.books if title.lower() in b.title.lower()]

    def find_by_author(self, author):
        # ищем по автору если он есть в списке
        return [b for b in self.books if any(author.lower() in a.lower() for a in b.authors)]


def menu():
    # создаем библиотеку чисто чтобы гонять тесты
    lib = Library("городская", "центр")

    while True:
        print("\nменю")
        print("1 показать все книги")
        print("2 закинуть книгу")
        print("3 выкинуть книгу")
        print("4 поиск по названию")
        print("5 поиск по автору")
        print("0 выйти")

        choice = input("че жмем ")

        if choice == "1":
            lib.show_books()

        elif choice == "2":
            title = input("название давай ")
            authors = input("авторы через запятую ").split(",")
            authors = [a.strip() for a in authors]
            year = input("годик ")

            book = Book(title, authors, year)
            lib.add_book(book)

        elif choice == "3":
            title = input("че удаляем ")
            lib.remove_book(title)

        elif choice == "4":
            title = input("че ищем ")
            res = lib.find_by_title(title)
            for b in res:
                print(b)

        elif choice == "5":
            author = input("какой автор ")
            res = lib.find_by_author(author)
            for b in res:
                print(b)

        elif choice == "0":
            print("вышли")
            break

        else:
            print("не понял че ты нажал")


if __name__ == "__main__":
    menu()