# функция полиморфизма - len()

# print(len("makers"))
# print(len([1, 2, 3, 4, 5]))
# print(len({1: 2, 3: 4}))
# print(len((1, 2, 3, 4)))

# +(__add__) - метод полиформизма

# print(5+5)
# print("mak" + "ers")
# print([1, 2, 3]+[4, 5, 6])
# print((1, 2, 3)+(4, 5, 6))

# Полиморфизм - способность метода обрабатывать данные разных типов (объектов от класса), обычно это реализуция путем создания базовго класса и наличия двху или более подклассов, которые все реализуют(переопределяют) методы с одинаковой сигнатурой(названием)
# Широко распространённое определение: "Один интерфейс - много реализаций"

# class Animal:

#     def info(self):
#         pass

#     def make_sound(self):
#         pass


# class Dog(Animal):

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"It's a dog. Dogs name is {self.name}, age {self.age}")

#     def make_sound(self):
#         print("Bark bark")


# class Cat(Animal):

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"It's a cat. Cats name is {self.name}, age {self.age}")

#     def make_sound(self):
#         print("Meow meow")


# cat = Cat("Garfild", 5)
# dog = Dog("Pluto", 9)

# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()
#     print()

# ----------------------------------------------------------------------

# Абстрация(Абстрактный класс) - его можно рассматривать как набор методов, которые должны быть реализованны во всех дочерних классах, которые будут унаследованны от абстрактого класса

# Абстрактный метод - это метод у которого есть объявление но нет реализации

from abc import ABC, abstractmethod as absm
from math import pi


# class Shape(ABC):

#     def __init__(self, name):
#         self.name = name

#     @absm
#     def area(self):
#         pass

#     @absm
#     def info(self):
#         pass


# class Square(Shape):

#     def __init__(self, lenght):
#         self.lenght = lenght
#         super().__init__("Квадрат")

#     def area(self):
#         return self.lenght * 4

#     def info(self):
#         print(f"Я {self.name}, у меня все углы равны 90 градусам!")


# class Circle(Shape):

#     def __init__(self, radius):
#         self.radius = radius
#         super().__init__("Окружность")

#     def area(self):
#         return pi * self.radius ** 2

#     def info(self):
#         print(f"Я {self.name}, и я фигура в двумерной плоскости!")


# square = Square(4)
# circle = Circle(4)

# for obj in (square, circle):
#     print()
#     print(obj.area())
#     obj.info()
#     print()

# ----------------------------------------------------------------------

# class CheesPiece(ABC):
#     # Общий метод, который будут использовать все наследники этоого класса
#     def take(self):
#         print("Take a chess piece!")

#     # Абстрактный метод, который необходимо переопредлить для каждого наследника
#     @absm
#     def move(self):
#         pass


# class Queen(CheesPiece):

#     def move(self):
#         return "Queen moves where she wants diagonaly, vertically and horizantally"


# class Pawn(CheesPiece):

#     def move(self):
#         return "The pawn can move directly to one cell!"


# queen = Queen()
# pawn = Pawn()
# print(queen.move())
# queen.take()
# print(pawn.move())
# pawn.take()

# ---------------------------------------------------------------------

# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.

# class Phone:

#     def __init__(self, os, imei):
#         self.__os = os
#         self.__imei = imei
#         self.__battery = 100

#     @property
#     def battery_getter(self):
#         if self.__battery < 0.5:
#             self.__battery = 0
#             raise Exception("Телефон разряжен")
#         print(f"{self.__battery}%")

#     @property
#     def get_info(self):
#         if self.__battery < 0.5:
#             self.__battery = 0
#             raise Exception("Телефон разряжен")
#         self.__battery -= 0.5
#         print(f"OS: {self.__os}, IMEI: {self.__imei}")

#     def music_play(self):
#         if self.__battery <= 5:
#             self.__battery = 0
#             raise Exception("Телефон разряжен")
#         self.__battery -= 5
#         self.__battery -= 0.5
#         print("Слушаем Мирбека Атабекова")

#     def video_play(self):
#         if self.__battery <= 10:
#             raise Exception("Недопустимый уровень заряда")
#         self.__battery -= 7
#         self.__battery -= 0.5
#         print("Смотрим Топлес")

#     def charge_battery(self, sec):
#         from time import sleep
#         i = 0
#         self.sec = sec
#         while i <= sec:
#             sleep(1)
#             if self.__battery < 100:
#                 self.__battery += 1
#             print(
#                 f"Идет зарядка батареи! Ваш уровень заряда {self.__battery}%")
#             i += 1
#             if self.__battery >= 100:
#                 break
#         print(f"Батарея заряжена на {self.__battery}%")


# phone = Phone("IOS", "14")
# # phone.battery()
# phone.music_play()
# phone.battery_getter
# phone.get_info
# phone.charge_battery(20)

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def get_area():
        pass

class Square(Shape):

    def __init__(self, lenght):
        self.lenght = lenght

    def get_area(self):
        return self.lenght * 4

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2

class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

square = Square(2)
circle = Circle(2)
triangle = Triangle(2,2)

print(triangle.get_area())
print(square.get_area())
print(circle.get_area())