import math

#студент типа объект с оценками
class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = []  #тут оценки лежат

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age} лет"

    def show_grades(self):
        if self.grades:
            print("оценки:", self.grades)
        else:
            print("оценок нет пока")  #пусто

    def add_grade(self, grade):
        self.grades.append(grade)
        print("добавили оценку")  #закинули оценку


#тачка просто инфа
class Car:
    def __init__(self, brand, model, speed, year):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}), {self.speed} км/ч"

    def show_info(self):
        print(self)  #выводим как есть


#круг
class Circle:
    def __init__(self, radius):
        self.radius = radius  #радиус

    def area(self):
        return math.pi * self.radius ** 2  #площадь

    def perimeter(self):
        return 2 * math.pi * self.radius  #длина круга


#прямоугольник
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b  #стороны

    def area(self):
        return self.a * self.b  #a*b

    def perimeter(self):
        return 2 * (self.a + self.b)  #обводка


#треугольник
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c  #3 стороны

    def perimeter(self):
        return self.a + self.b + self.c  #сложили

    def area(self):
        p = self.perimeter() / 2  #половина периметра
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))  #герон


#главный движ
def main():
    student = Student("Volodymyr", "Futuima", 16)
    car = Car("BMW", "M5", 305, 2022)  #норм бэха

    while True:
        print("\nменю")
        print("1 студент")
        print("2 машина")
        print("3 фигуры")
        print("0 выход")

        choice = input("выбор: ")

        if choice == "1":
            while True:
                print("\nстудент")
                print("1 показать")
                print("2 добавить оценку")
                print("3 оценки")
                print("0 назад")

                c = input("выбор: ")

                if c == "1":
                    print(student)  #инфа
                elif c == "2":
                    g = int(input("оценка: "))
                    student.add_grade(g)  #добавили
                elif c == "3":
                    student.show_grades()  #смотрим
                elif c == "0":
                    break  #назад

        elif choice == "2":
            print(car)
            car.show_info()

        elif choice == "3":
            while True:
                print("\nфигуры")
                print("1 круг")
                print("2 прямоугольник")
                print("3 треугольник")
                print("0 назад")

                c = input("выбор: ")

                if c == "1":
                    r = float(input("радиус: "))
                    obj = Circle(r)
                    print("площадь:", obj.area())
                    print("периметр:", obj.perimeter())

                elif c == "2":
                    a = float(input("a: "))
                    b = float(input("b: "))
                    obj = Rectangle(a, b)
                    print("площадь:", obj.area())
                    print("периметр:", obj.perimeter())

                elif c == "3":
                    a = float(input("a: "))
                    b = float(input("b: "))
                    c_ = float(input("c: "))
                    obj = Triangle(a, b, c_)
                    print("площадь:", obj.area())
                    print("периметр:", obj.perimeter())

                elif c == "0":
                    break  #назад

        elif choice == "0":
            print("пока")
            break


#запуск
main()
