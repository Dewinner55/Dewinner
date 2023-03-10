# В объектно-ориентированном программировании(ООП) существуют три типа методов, в зависимости от того, как они связаны с классом и экземплярами класса:

#    1. Методы класса(class methods): Эти методы связаны с классом, а не с конкретным экземпляром класса. Они определяются с использованием декоратора @ classmethod и имеют первым параметром ссылку на класс cls. Обычно они используются для создания альтернативных конструкторов или для работы со свойствами класса.

#    2. Методы экземпляра(instance methods): Эти методы связаны с конкретным экземпляром класса. Они определяются без использования специальных декораторов и имеют первым параметром ссылку на экземпляр self. Они обычно используются для работы с конкретными данными объекта.

#    3. Статические методы(static methods): Эти методы не связаны ни с классом, ни с экземпляром класса. Они определяются с использованием декоратора @ staticmethod и не принимают параметры self или cls. Они обычно используются для реализации общих для класса функций или для утилитарных функций, которые не требуют доступа к данным объекта или класса.
# --------------------------------------------------------------------------------
# 1) Пример метода класса(class methods)

# class B:

#     @classmethod
#     def class_method(cls, string):
#         print("класс метод")
#         print("первый аргумент: ", cls)


# obj_b = B()
# obj_b.class_method(5)
# B.class_method(5)

# class C:

#     counter = 0

#     def __init__(self) -> None:
#         self.__inc_counter()

#     @classmethod
#     def __inc_counter(cls):
#         cls.counter += 1


# obj1 = C()
# obj2 = C()
# obj3 = C()
# print(C.counter)

# class Pizza:

#     def __init__(self, radius, *ingredients):
#         self.radius = radius
#         self.ingredients = ingredients

#     def cook(self):
#         print(f"готовися пицца с размером {self.radius * 2} см с ингредиетами {self.ingredients}")

#     @classmethod
#     def four_cheese(cls, r):
#         pizza = cls(r, "моцарела", "чедер", "голландский", "брынза")
#         return pizza


# pizza1 = Pizza(17, "пеперони", "моцарелла", "грибы")
# pizza2 = Pizza.four_cheese(15)
# pizza3 = Pizza.four_cheese(20)
# pizza1.cook()
# pizza2.cook()
# pizza3.cook()

# class Person:
#     surname = "Stark"

#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_date(cls, name, date_birth):
#         from datetime import datetime
#         age = datetime.today().year - date_birth
#         return cls(name, age)


# obj = Person.from_birth_date("John", 1997)
# print(obj.name, obj.surname, obj.age)
# obj2 = Person("Sansa", 25)
# print(obj2.name, obj2.surname, obj2.age)


# --------------------------------------------------------------------------------
#
# 2) Пример метода экземпляра(instance methods):

# class A:

#     def instnace_method(self, a):
#         print("Это метод объъекта")
#         print("Это 1 аргумент: ", self)


# obj_a = A()
# Если вызываем у объекта, то self передается автоматически
# obj_a.instnace_method(5)
# A.instnace_method(obj_a, 5)
# --------------------------------------------------------------------------------
#
# 3) Пример метода Статические методы(static methods)

# class S:

#     @staticmethod
#     def static_method():
#         print("Статический метод")


# obj = S()
# obj.static_method()
# S.static_method()

# class A:

#     def __init__(self, diameter, height) -> None:
#         self.di = diameter
#         self.height = height
#         self.area = self.get_area(self.di, self.height)

#     @staticmethod
#     def get_area(diameter, h):
#         from math import pi
#         circle = pi * (diameter / 2) ** 2
#         side = pi * h * diameter
#         area = circle * 2 + side
#         return round(area, 2)


# obj = A(10, 7)
# print(f"Area: {obj.area}")
# obj2 = A(4, 10)
# print(f"Area: {obj2.get_area(4,10)}")
