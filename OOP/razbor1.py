"""
Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога от зарплаты - 15 % . Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.
"""


# class Salary:
#     procent = 15

#     def __init__(self, zarplata, stach):
#         self.zarplata = zarplata
#         self.stach = stach

#     def __str__(self) -> str:
#         return f"{self.zarplata}, {self.stach}"

#     def get_nalog(self):
#         return (self.zarplata * self.procent // 100) * (self.stach * 12)


# obj = Salary(170000, 11)
# print(obj)
# print(obj.get_nalog())

# ------------------------------------------------------------------------

# import math


# class Calc:

#     def plus(self, a, b):  # Функция сложения
#         return a + b

#     def sqrt(self, num):  # Функция нахождения квадратного корня
#         res = math.sqrt(num)
#         return round(res, 2)

#     def percent(self, num, percent):  # Функция нахождения % от числа
#         return (num * percent) / 100

#     def minus(self, c, d):
#         return c - d

#     def super_func(self, string):  # Функция выполняет вычисление чисел в строке
#         try:
#             return eval(string)
#         except:
#             return "Invalid Operation"


# calc = Calc()
# print(calc.plus(4, 5))
# print(calc.sqrt(9))
# print(calc.percent(110, 11))
# print(calc.minus(87, 35))
# print(calc.super_func("(5-7)**2-10%"))

# -----------------------------------------------------------------------

# import random


# class Sniper:

#     healt = 100

#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name

#     def shoot(self, snipers):
#         snipers.healt = snipers.healt - 20
#         print(f"Атаковал {self}")
#         print(f"Жертва {snipers}, осталось здровья у жертвы: {snipers.healt}")


# sniper1 = Sniper("John")
# sniper2 = Sniper("Jamie")
# # print("")
# # print(sniper1, sniper1.healt)
# # print(sniper2, sniper2.healt)
# # print("")
# # sniper2.shoot(sniper1)
# # sniper2.shoot(sniper1)
# # print("")
# # print(sniper1, sniper1.healt)
# # print(sniper2, sniper2.healt)

# while sniper1.healt and sniper2.healt:
#     choice = random.randint(1, 2)
#     if choice == 1:
#         sniper1.shoot(sniper2)
#     else:
#         sniper2.shoot(sniper1)


# if sniper1.healt:
#     print(f"{sniper1} победил!!!")
# else:
#     print(f"{sniper2} победил!!!")

# print("")
# print(sniper1, sniper1.healt)
# print(sniper2, sniper2.healt)

# -----------------------------------------------------------------------

# class Crud:

#     __products = []
#     __id = 0

#     def _get_id(self):
#         self.__id += 1
#         return self.__id

#     def _get_product(self, id):
#         for x in self.__products:
#             if x["id"] == id:
#                 return x
#         return False

#     def create(self):
#         title = input("Vvedite tittle: ")
#         price = input("Vvedite price: ")
#         self.__products.append(
#             {"id": self._get_id(), "title": title, "price": price})
#         return self.__products

#     def list_of_products(self):
#         print("Все наши продукты: ")
#         for x in self.__products:
#             print(x["title"])

#     def detail_product(self):
#         print("Поиск по ID")
#         id = int(input("Введите ID продукта: "))
#         product = self._get_product(id)
#         print(product if product else "Нет такого продукта!!!")

#     def update_product(self):
#         print("Обновление продукта")
#         id = int(input("Введите ID продукта: "))
#         product = self._get_product(id)
#         if not product:
#             print("Нет такого продукта!")
#             return
#         choice = input("Что изменить?(title/price): ")
#         index = self.__products.index(product)
#         self.__products[index][choice] = input("Введите новое значение: ")

#     def delete_product(self):
#         print("Удаление продукта: ")
#         id = int(input("Введите ID продукта: "))
#         product = self._get_product(id)
#         if not product:
#             print("нет такого продукта")
#             return
#         self.__products.remove(product)
#         print("Удалено")


# product = Crud()
# product.create()
# product.create()
# print("")
# product.list_of_products()
# print("")
# product.detail_product()
# print("")
# product.update_product()
# print("")
# product.delete_product()
# print("")
# product.list_of_products()

# ------------------------------------------------------------------------

