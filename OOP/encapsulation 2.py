# Аннотация свойств (@property(getter,setter))

# class Person:
#     __name = "John"
#     __age = 22
#     __code = "+996"
#     __number = "500 200 200"
#     __full_number = __code + __number

#     @property
#     def name(self):
#         print(self.__name)

#     @name.setter
#     def new_name(self, name):
#         if not isinstance(name, str):
#             print("Invalid value")
#             return
#         self.__name = name

#     @property
#     def age(self):
#         print(self.__age)

#     @age.setter
#     def new_age(self, age):
#         if not isinstance(age, int) or not 18 <= age < 65:
#             print("Invalid valuer for age!")
#             return
#         self.__age = age

#     @property
#     def number(self):
#         name = input("Введите своё имя: ")
#         if self.__name != name:
#             print("Неверное имя")
#             return
#         print(self.__full_number)

#     @number.setter
#     def new_number(self, value: dict):
#         if value["code"] != "+996":
#             print("Это не код Киргизии")
#         elif len(value["number"]) != 9:
#             print("Неверная длинна телефона")
#         self.__code = value["code"]
#         self.__number = value["value"]
#         self.__full_number = self.__code + self.__number


# person = Person()
# person.name, person.age
# person.new_name = "Sherlock"
# person.new_age = 30
# person.new_name, person.new_age
# person.number
# person.new_number = {"code": '+55', "number": '999_888_777'}

# class Circle:

#     def __init__(self, radius) -> None:
#         self.__radius = radius


#     @property
#     def radius(self):
#         return self.__radius

#     @radius.setter
#     def radius(self, value):
#         if not isinstance(value, (int, float)):
#             raise Exception("Ошибка значение, это должны быть числа")
#         self.__radius = value


# circle = Circle(42)
# print(circle.radius)
# circle.radius = 50.5
# print(circle.radius)
# print("")
# circle.radius = "ter"
