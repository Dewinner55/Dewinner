
# 1. связь данных с методами
# 2. механизм языка который позволяет ограничить доступ к определенным компонентам класса
# Инкапсуляция как связь
# -----------------------------------------------------------
# class Phone:
#     number = "+996500700700"

#     def print_number(self):
#         print(f"Мой номер: {self.number}")

# my_phone = Phone()
# my_phone.print_number()

# -------------------------------------------------------------

# Инкапскуляция как управление доступом
# 3 уроня доступа в питоне:
# 1. Публичный(public) - number, print_number
# 2. Защищенный(_protected, parent/child) - nubmer
# 3. Приватный(__private, только в текущем классе) - _number

# class Car:
#     _contry = "Germany"

#     def __init__(self):
#         self.marka = "Mercedes-Benz"
#         self._model = "W140"
#         self.__motor = "ABC"


# obj = Car()
# print(obj.marka)
# print(obj._contry)
# print(obj._model)
# print(obj._Car__motor)

# -------------------------------------------------------------

# class Phone:
#     username = "John Snow"
#     _caller = "Jamie Lanister"
#     __count_of_call = 15

#     def call(self):
#         print(f"{self._caller} Звонит!")

#     def __increment_of_calls(self):
#         self.__count_of_call += 1

#     def turn_on(self):
#         print(f"{self.username} взял трубку!")
#         self.__increment_of_calls()

#     def get_count(self):
#         print(self.__count_of_call)


# obj = Phone()
# obj.get_count()
# obj.call()
# obj.turn_on()
# obj.get_count()

# -------------------------------------------------------------

# getter & setter
# Они используются для получения и установки значений в защищенные аттрибуты, чтобы избежать прямого доступа к захищенному аттрибуты и еще с помощью сеттеров и гетторов можно добовлять логику проверки при получении данных

# class Person:

#     def __init__(self, name) -> None:
#         self.__name = name
#         self.__age = 0

#     def deisplay_info(self):
#         print(f"My name is {self.__name}, I'm {self.__age} years old!")

#     # getter
#     def getter_name(self):
#         return self.__name

#     # setter
#     def setter_name(self, name):
#         if not isinstance(name, str):
#             print("Invalid value")
#         else:
#             self.__name = name

#     # getter
#     def getter_age(self):
#         return self.__age

#     # setter
#     def setter_age(self, age):
#         if not isinstance(age, int) or not 0 <= age < 150:
#             print("Invalid valuer for age!")
#         else:
#             self.__age = age


# person = Person("John")
# person.deisplay_info()

# person.setter_name(None)
# person.setter_age(-18)
# # person.deisplay_info()
# print("")
# person.deisplay_info()
# person.setter_name("Jamie")
# person.setter_age(24)
# person.deisplay_info()
# print("")

# -------------------------------------------------------------

# class Russia:

#     __name = "Russia Federation"
#     __population = 0

#     def get_population(self):
#         return self.__population

#     def set_population(self, population):
#         if not isinstance(population, int) or population < 0:
#             print("Invalid value")
#         else:
#             self.__population = population

#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         if not isinstance(name, str):
#             print("Invalid value")
#         else:
#             self.__name = name

#     def display_info(self):
#         print(f"Population of {self.get_name()}: {self.get_population()}")


# russia = Russia()
# russia.set_population(143_000_000)
# russia.set_name("India")
# russia.display_info()

# -----------------------------------------------------------------------


