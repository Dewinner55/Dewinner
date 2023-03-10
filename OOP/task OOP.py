# class Circle:
#     color = "blue"
#     pi = 3.14

#     def __init__(self) -> None:
#         self.radius = 2

#     def get_area(self):
#         return {self.radius ** 2 * self.pi}


# circle = Circle()
# print(circle.color)
# print(circle.get_area())

# TASK3

# class BankAccount:
#     balance = 0

#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f"Ваш баланс: {self.balance} сом")

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Ваш баланс: {self.balance} сом")


# account = BankAccount()
# account.deposit(-1)
# account.withdraw(-1)


# class BankAccount:
#     def __init__(self):
#         self.balance = 0

#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f'Ваш баланс: {self.balance} сом')

#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Ваш баланс: {self.balance} сом')


# account = BankAccount()
# account.deposit(-1)
# account.withdraw(-1)

# class Taxi:
#     cost = 10

#     def __init__(self, name):
#         self.name = name

#     def get_total_cost(self, km):
#         self.km = km
#         return f"Такси {self.name}, стоимость поездки: {self.cost * self.km}"


# taxi1 = Taxi("Namba")
# taxi2 = Taxi("Yandex")
# taxi3 = Taxi("Jorgo")

# print(taxi1.get_total_cost(10))
# print(taxi1.get_total_cost(6))
# print(taxi1.get_total_cost(14))

# class Taxi:
#     cost = 10

#     def __init__(self, name):
#         self.name = name

#     def get_total_cost(self, km):
#         self.km = km
#         return f"Такси {self.name}, стоимость поездки: {self.cost * self.km}"


# taxi1 = Taxi("Namba")
# taxi2 = Taxi("Yandex")
# taxi3 = Taxi("Jorgo")

# print(taxi1.get_total_cost(10))
# print(taxi1.get_total_cost(6))
# print(taxi1.get_total_cost(14))

# class Phone:
#     name = "John"
#     last_name = "Snow"
#     phone = "+996707707707"

#     def get_info(self):
#         print(f"Контакт: {self.name} {self.last_name}, телефон {self.phone}")


# contact = Phone()
# contact.get_info()

# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone

#     def get_info(self):
#         print(f"Контакт: {self.name} {self.last_name}, телефон: {self.phone}")


# contact = Phone("John", "Snow", "+996707707707")
# contact.get_info()

# class Salary:
#     percent = 8

#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience

#     def count_percent(self):
#         obj = self.salary * self.percent / 100 * self.experience
#         return obj


# result = Salary(10000, 10)
# print(result.count_percent())
# ----------------------------------------------------------
# from datetime import datetime


# def get_year1():
#     today = datetime.today()
#     today = today.year
#     return today


# class Nobel:

#     # today = datetime.today()
#     # today = today.year

#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner

#     # def get_year1():
#     #     today = datetime.today()
#     #     today = today.year
#     #     return today

#     def get_year(self):
#         return f"выиграл {get_year1() - self.year} лет назад"


# winner1 = Nobel("Литература", 1971, "Пабло Неруда")
# print(winner1.category, winner1.year, winner1.winner)
# print(winner1.get_year())


# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
# print(winner2.category, winner2.year, winner2.winner)
# print(winner2.get_year())

# # print(winner2.get_year1())

# # winner1.get_year1()

# # today = datetime.today()
# # today = today.year
# # print(today)
# # today = datetime.today()
# # print(today)
# # print(today.year)
# ----------------------------------------------------------
# from datetime import datetime


# class Nobel:

#     today = datetime.today()
#     today = today.year

#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner

#     def get_year(self):
#         return f"выиграл {self.today - self.year} лет назад"


# winner1 = Nobel("Литература", 1971, "Пабло Неруда")
# print(winner1.category, winner1.year, winner1.winner)
# print(winner1.get_year())


# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
# print(winner2.category, winner2.year, winner2.winner)
# print(winner2.get_year())

# ------------------------------------------------------------

# class Math:
#     def __init__(self, number):
#         self.number = number

#     def get_factorial(self):
#         factorial = 1
#         for i in range(2, self.number + 1):
#             factorial *= i
#         return factorial

#     def get_sum(self):
#         number = [int(x)for x in str(self.number)]
#         suma = sum(number)
#         return suma

#     def get_mul_table(self):
#         s = ''
#         for i in range(10):
#             s += f'{self.number}x{i+1}={self.number * (i+1)}' + '\n'
#         return s


# math = Math(0)
# print(math.get_factorial())
# print(math.get_sum())
# print(math.get_mul_table())


# -----------------------------------------------------------

# class Math:
#     def __init__(self, number):
#         self.number = number

#     def get_factorial(self):
#         self.factorial = 1
#         for i in range(2, self.number+1):
#             self.factorial = self.factorial*i
#         return self.factorial

#     def get_sum(self):
#         number = [int(x)for x in str(self.number)]
#         suma = sum(number)
#         return suma

#     def get_mul_table(self):
#         s = ''
#         for i in range(10):
#             s += f'{self.number}x{i+1}={self.number * (i+1)}' + '\n'
#         return s


# number1 = Math(0)
# print(number1.get_factorial())
# print(number1.get_sum())
# print(number1.get_mul_table())


# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"name:{self.name}, age: {self.age}")


# class Student(Person):

#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty

#     def display_student(self):
#         print(f"name:{self.name}, age: {self.age}, {self.faculty}")


# obj_student = Student("John", 21, "Foxford")
# obj_student.display()
# obj_student.display_student()


# from datetime import datetime


# class SmartPhones:
#     def __init__(self, name, color, memory):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = 0

#     def __str__(self):
#         return f"{self.name} {self.memory}GB"

#     def charge(self, charge_new):
#         self.battery = charge_new + charge_new
#         return charge_new


# class Iphone(SmartPhones):

#     def __init__(self, name, color, memory, ios):
#         super().__init__(name, color, memory)
#         self.ios = ios

#     def send_imessage(self):
#         return f"sending hello from {self.name} {self.memory}"


# phone = SmartPhones("Samsung", "Blue", "128")
# print(phone.__str__())
# print(phone.charge(20))
# print("")

# iphone = Iphone("Samsung", "Blue", "128", 11.4)
# print(iphone.send_imessage())


# import datetime


# class SmartPhones:
#     def __init__(self, name, color, memory):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = 0

#     def __str__(self):
#         return f"{self.name} {self.memory}"

#     def charge(self, charge_new):
#         self.battery = charge_new
#         return charge_new


# class Iphone(SmartPhones):

#     def __init__(self, name, color, memory, ios):
#         super().__init__(name, color, memory)
#         self.ios = ios

#     def send_imessage(self, string):
#         self.string = string
#         return f"sending {self.string} from {self.name} {self.memory}"


# class Samsung(SmartPhones):

#     def __init__(self, name, color, memory, android):
#         super().__init__(name, color, memory)
#         self.android = android

#     def show_time(self):
#         return datetime.datetime.today().time()


# phone = SmartPhones('generic', 'blue', '128GB')
# print(phone)

# print(phone.battery)
# phone.charge(20)
# print(phone.battery)

# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3')
# print(iphone7)
# print(iphone7.send_imessage('hello'))

# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo')
# print(samsung21.show_time())

# ----------------------------------------------------------------------

# class CustomError(Exception):

#     def __init__(self, message):
#         self.message = message


# def check_letters(str_):
#     if str_.islower():
#         raise capitals_error
#     else:
#         return f"ВСЕ ОТЛИЧНО! {str_}"


# capitals_error = CustomError("ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ")

# print(check_letters("hello"))
# print(check_letters("hello"))

# capitals_error =

# ------------------------------------------------------------------------

# class A:

#     def method1(self, string1):
#         self.string1 = string1
#         print(string1)


# class B(A):

#     def method1(self, string1, string2):
#         super().method1(string1)
#         self.string2 = string2
#         print(self.string2)


# obj = B()
# obj.method1("Основной функционал", "Дополнительный функционал")
# obj.method1("Основной функционал", "Дополнительный функционал")

# -------------------------------------------------------------------------

# class MyString(str):

#     def __init__(self, string):
#         self.string = string

#     def append(self, string1):
#         self.string1 = string1
#         self.res = self.string + self.string1
#         return self.res

#     def pop(self):
#         res = self.res[-1]
#         self.res = self.res[:-1]
#         return res

#     def __str__(self) -> str:
#         return self.res


# example = MyString('String')
# example.append('hello')

# print(example.pop())
# print(example)


# class MyString(str):
#     def __init__(self, stroka1):
#         self.stroka1 = stroka1

#     def append(self, stroka2):
#         self.stroka2 = stroka2
#         self.stroka1 = self.stroka1 + self.stroka2
#         return self.stroka1

#     def pop(self):
#         last_w = self.stroka1[-1]
#         self.stroka1 = self.stroka1[:-1]
#         return last_w

#     def __str__(self) -> str:
#         return self.stroka1


# example = MyString('String')
# example.append('hello')
# print(example.pop())
# print(example)

# -------------------------------------------------------------------

# class MyDict(dict):

#     def get1(self, key):
#         default = "Are you kidding?"
#         return dict.get(self, key, default)


# obj_dict = MyDict({'some_title': 2})
# print("")
# print(obj_dict.get1('some_titl'))
# print("")
# print(obj_dict)

# TASK 8

# class Password:

#     def __init__(self, string):
#         self.string = string

#     def __str__(self):
#         return "x" * len(self.string)

#     def validate(self):
#         if len(self.string) < 8 or len(self.string) > 15:
#             return f"Password should be longer than 8, and less than 15"
#         elif self.string != (lambda x: x.isdigit(), self.string):
#             return f"Password should contain numbers too"
#     # elif
#     #         return f"Password should contain letters as well"
#     # elif
#     #         return f"Your password should have some symbols"
#         else:
#             return f"Ваш пароль сохранен."


# password = Password("12345678j")
# print(password)
# print(password.validate())

# class Password:
#     def __init__(self, password):
#         self.password = password
#     def __str__(self) -> str:
#         return '*' * len(self.password)
#     def validate(self):
#         if not len(self.password) == 8 and len(self.password) < 15:
#           return f'Password should be longer than 8, and less than 15'
#         if not any(map(lambda i: i.isdigit(), self.password)):
#             return f'Password should contain numbers too'
#         if not any(map(lambda i: i.isalpha(), self.password)):
#             return f'Password should contain letters as well'
#         if not any(map(lambda i: i in ['@', '#', '&', '$', '%', '!', '~', '*'], self.password)):
#             return f'Your password should have some symbols'
#         return f'Ваш пароль сохранен.'
#     password = Password('sanem23@')
#     print(password.validate())
#     print(password)

# ----------------------------------------------------------------------

# import datetime


# class CreateMixin:
#     def create(self, key, todo):
#         if not (key in list(self.todos.keys())):
#             self.todos[key] = todo
#         else:
#             print("Задача под таким ключём уже существует")


# class DeleteMixin:
#     def delete(self, key):
#         self.todos.pop(key)


# class UpdateMixin:
#     def update(self, new_value, key):
#         self.todos[key] = new_value


# class ReadMixin:
#     def read(self):
#         res = [x for x in self.todos.items()]
#         return sorted(res)


# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):

#     todos = {}

#     def set_deadline(self, deadline):
#         time_ = datetime.datetime.now().day
#         list_ = deadline.split("/")[0]
#         return int(list_) - time_


# task = ToDo()
# print(task.set_deadline('31/12/2022'))
# print(task.create(1, 'todo'))
# # print(task.delete(3))
# print(task.update(1, 'todo'))
# # print(task.read())
# print(task.create(1, 'Do housework'))
# print(task.create(1, 'Do housework'))
# print(task.create(2, 'Go for a walk'))
# print(task.update(1, 'Do homework'))
# # print(task.delete(2))
# # print(task.read())
# print(task.set_deadline('31/12/2021'))


# ----------------------------------------------------------------------
# TASK 6 miksin
# class CreateMixin:
#     def create(self, key, todo):
#         if key in self.todos.keys():
#             return 'Задача под таким ключом уже существует'
#         self.todos[key] = todo
#         return self.todos


# class DeleteMixin:
#     def delete(self, key):
#         delete_ = self.todos.pop(key, 'нет такого ключа')
#         if 'нет такого ключа' == delete_:
#             return delete_
#         return delete_


# class UpdateMixin:
#     def update(self, key, new_value):
#         self.todos[key] = new_value
#         return self.todos


# class ReadMixin:
#     def read(self):
#         res = [x for x in self.todos.items()]
#         return sorted(res)


# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}

#     def set_deadline(self, deadline):
#         import datetime
#         time_ = datetime.datetime.now().strftime('%d/%m/%Y')
#         deadline = deadline.split('/')
#         time_ = time_.split('/')
#         deadline = list(map(int, deadline))
#         time_ = list(map(int, time_))
#         time_ = sum((time_[0], time_[1]*30, time_[2]*365))
#         deadline = datetime.date(deadline[2], deadline[1], deadline[0])
#         time_ = datetime.date.today()
#         return (deadline - time_).days


# task = ToDo()
# print(task.set_deadline('31/12/2022'))
# print(task.create(1, 'todo'))
# print(task.delete(3))
# print(task.update(1, 'todo'))
# print(task.read())
# print(task.create(1, 'Do housework'))
# print(task.create(1, 'Do housework'))
# print(task.create(2, 'Go for a walk'))
# print(task.update(1, 'Do homework'))
# print(task.delete(2))
# print(task.read())
# print(task.set_deadline('31/12/2021'))


# class RadioMixin:

#     def play_music(self, title):
#         self.title = title
#         print("Песня называется {title}")


# class Auto(RadioMixin):
#     pass


# class Boat(RadioMixin):
#     pass


# class Amphibian(Auto, Boat):
#     pass


# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# auto.play_music()
# boat.play_music()
# obj.play_music()

# ------------------------------------------------------------------------
# TASK 4

# from abc import ABC, abstractmethod


# class Coder(ABC):

#     count_code_time = 0

#     @abstractmethod
#     def get_info(self):
#         pass

#     @abstractmethod
#     def coding(self):
#         pass


# class Backend(Coder):

#     def __init__(self, experience, languages_backend):
#         self.experience = experience
#         self.languages_backend = languages_backend

#     def coding(self, hour):
#         self.hour = hour
#         self.count_code_time = hour
#         return self.count_code_time

#     def get_info(self):
#         return f"{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование"


# class Frontend(Coder):

#     def __init__(self, experience, languages_frontend):
#         self.experience = experience
#         self.languages_frontend = languages_frontend

#     def coding(self, hour):
#         self.hour = hour
#         self.count_code_time = hour
#         return self.count_code_time

#     def get_info(self):
#         return f"{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование"


# class Fullstack(Backend, Frontend):
#     pass


# a = Backend("Senior", "Ruby")
# b = Frontend("Junior", "C++")
# c = Fullstack("Ultra mega super puper senior", "HTML")
# a.coding(100)
# b.coding(520)
# c.coding(87946532)
# print(a.get_info())
# print(b.get_info())
# print(c.get_info())

# ------------------------------------------------------------------------

# TASK 5

# class Square:

#     def __init__(self, side1):
#         self.side1 = side1
#         # self.side2 = side2

#     def get_area(self):
#         result = (self.side1 * self.side1)
#         return result


# class Triangle:

#     def __init__(self, height, base):
#         self.height = height
#         self.base = base

#     def get_area(self):
#         result = (self.height * self.base) // 2
#         return result


# class Pyramid(Triangle, Square):

#     def __init__(self, height, base):
#         super().__init__(height, base)

#     def get_volume(self):
#         result = round((1/3*self.base**2*self.height))
#         return result, (type(result))


# square = Square(10)
# print(square.get_area())
# triangle = Triangle(2, 2)
# print(triangle.get_area())
# piramid = Pyramid(10, 10)
# print(piramid.get_volume())


# class Square:

#     def __init__(self, side) -> None:
#         self.side = side

#     def get_area(self):
#         return self.side * self.side


# class Triangle:
#     def __init__(self, height, base) -> None:
#         self.height = height
#         self.base = base

#     def get_area(self):
#         return int(0.5*self.base*self.height)


# class Pyramid(Triangle, Square):
#     def __init__(self, height, base) -> None:
#         super().__init__(height, base)

#     def get_volume(self):
#         return int(1/3*self.base**2*self.height)


# obj = Square(10)
# print(obj.get_area())
# obj2 = Triangle(2, 2)
# print(obj2.get_area())
# obj3 = Pyramid(10, 10)
# print(obj3.get_volume())

# Из-за round Не принимал, т.к. раунд метод округление , а int делает целое число!

# TASK 7

# class ExtensionMixin:

#     def __init__(self, name):
#         self.name = name
#         self.type_ = None
#         self.extensions = []

#     def add_extension(self, stroka):
#         self.stroka = stroka
#         return f"Добавлено новое расширение {self.stroka} для игры {self.name}"

#     def remove_extension(self, new_storka):
#         self.new_storka = new_storka
#         if self.new_storka == self.stroka:
#             return f"{self.stroka} был отключен от {self.name}"
#         else:
#             return f"Такого расирения нет в списке."


# class Game(ExtensionMixin):

#     def __init__(self, name):
#         self.name = name
#         self.type_ = None
#         self.extensions = []

#     def get_description(self):
#         return f"{self.name} это инди-игра в жанре песочницы с элементами выживания и открытым миром"

#     def get_extensions(self):
#         if len(self.extensions) == 0:
#             return "Нет подключенных расширений"
#         else:
#             return self.extensions


# game = Game("Minecraft")
# print(game.get_description())
# print(game.get_extensions())
# mixin = ExtensionMixin("Minecraft")
# print(mixin.add_extension("Multiverse-Core"))
# print(mixin.remove_extension("Multiverse"))
# print(mixin.remove_extension("Multiverse-Core"))

# -----------------------------------------------------------------------

# Решено!

# class ExtensionMixin:

#     def add_extension(self, stroka):
#         self.extensions.append(stroka)
#         return f"Добавлено новое расширение {stroka} для игры {self.name}."

#     def remove_extension(self, stroka):
#         if stroka in self.extensions:
#             self.extensions.remove(stroka)
#             return f"{stroka} был отключен от {self.name}"
#         else:
#             return f"Такого расширения нет в списке."


# class Game(ExtensionMixin):

#     def __init__(self, name, game_type):
#         self.type = game_type
#         self.name = name
#         self.extensions = []

#     def get_description(self, description):
#         return f"{self.name} это {description}"

#     def get_extensions(self):
#         if len(self.extensions) == 0:
#             return "Нет подключенных расширений"
#         else:
#             return self.extensions


# game = Game("Minecraft", "CS_GO")
# print(game.get_description(
#     "инди-игра в жанре песочницы с элементами выживания и открытым миром"))
# print(game.get_extensions())
# print(game.add_extension("Multiverse-Core"))
# game.extensions
# print(game.get_extensions())
# print(game.remove_extension("Multiverse"))
# print(game.remove_extension("Multiverse-Core"))
# print(game.get_extensions())

# -----------------------------------------------------------------------

# POLIMORFIZM TASK1

# def add(x):
#     print(len(x))


# # add("makers")

# a = '12342342345'
# b = [1, ['a', 5, 6], 2, 3, 4, 5]
# c = {1: 'a', 2: {'a': 1, 'b': 2}, 3: 'c'}

# add(a)
# add(b)
# add(c)

# TASK2


# class Dog:

#     def voice(self):
#         print("Гав")


# class Cat:

#     def voice(self):
#         print("Мяу")


# def to_pet(name):
#     return voice()


# cat = Cat()
# dog = Dog()

# print(to_pet("Barsik"))

# class Dog:
#     def voice(self):
#         print('Гав')


# class Cat:
#     def voice(self):
#         print('Мяу')


# def to_pet(name1, name2):
#     name1.voice()
#     name2.voice()


# barsik = Cat()
# rex = Dog()
# to_pet(rex, barsik)

# class Dog:
#     def voice(self):
#         print('Гав')


# class Cat:
#     def voice(self):
#         print('Мяу')


# barsik = Cat()
# rex = Dog()


# def to_pet(golos):
#     golos.voice()


# to_pet(rex)
# to_pet(barsik)

# TASK 3

# class Person:

#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name

#     def get_info(self):
#         return f"Привет, меня зовут {self.name} {self.last_name}"


# class Employee(Person):

#     def __init__(self, name, last_name, work, status):
#         super().__init__(name, last_name)
#         self.work = work
#         self.status = status

#     def get_info(self):
#         return f"Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}"


# class Student(Person):

#     def __init__(self, name, last_name, university, course):
#         super().__init__(name, last_name)
#         self.university = university
#         self.course = course

#     def get_info(self):
#         return f"Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе"


# person = Person("Иван", "Петров")
# employee = Employee("Иван", "Петров", "Рога и Копыта", "директор")
# student = Student("Иван", "Петров", "КГТУ", "3")
# print(person.get_info())
# print(employee.get_info())
# print(student.get_info())

# # TAKS 4

# from abc import ABC, abstractmethod
# from math import pi


# class Shape(ABC):

#     @abstractmethod
#     def get_area():
#         pass


# class Square(Shape):

#     def __init__(self, lenght):
#         self.lenght = lenght

#     def get_area(self):
#         return self.lenght ** 2


# class Circle(Shape):

#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return pi * self.radius ** 2


# class Triangle(Shape):

#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def get_area(self):
#         return 0.5 * self.base * self.height


# square = Square(2)
# circle = Circle(2)
# triangle = Triangle(2, 2)

# print(triangle.get_area())
# print(square.get_area())
# print(circle.get_area())

# # TASK6

# class Language:

#     def __init__(self, level, type_):
#         self.level = level
#         self.type_ = type_


# class Python(Language):

#     def write_function(self, func_name, arg):
#         self.func_name = func_name
#         self.arg = arg
#         return f"def {self.func_name}({self.arg}):"

#     def create_variable(self, var_name, value):
#         if isinstance(value, str):
#             self.var_name = var_name
#             self.value = value
#             return f"{self.var_name} = '{self.value}'"


# class JavaScript(Language):

#     def write_function(self, func_name, arg):
#         self.func_name = func_name
#         self.arg = arg
#         return f"function {self.func_name}({self.arg}) {{    }};"

#     def create_variable(self, var_name, value):
#         if isinstance(value, str):
#             self.var_name = var_name
#             self.value = value
#             return f"let {self.var_name} = '{self.value}'"


# py = Python("Junior", "NonType")
# print(py.write_function("get_code", "a"))
# print(py.create_variable("name", "John"))
# js = JavaScript("Middle", "NonType")
# print(js.write_function('validate', 'form'))
# print(js.create_variable('password', 'john@123'))

# # ------------------------------------------------------------------------
# #  Правильный код

# class Language:
#     def __init__(self, level, lang_type):
#         self.level = level
#         self.lang_type = lang_type


# class Python(Language):
#     def write_function(self, func_name, arg):
#         return f"def {func_name}({arg}):"

#     def create_variable(self, var_name, value):
#         if isinstance(value, str):
#             return f"{var_name} = '{value}'"
#         else:
#             return f"{var_name} = {value}"


# class JavaScript(Language):
#     def write_function(self, func_name, arg):
#         return f"function {func_name}({arg}) {{ }};"

#     def create_variable(self, var_name, value):
#         if isinstance(value, str):
#             return f"let {var_name} = '{value}';"
#         else:
#             return f"let {var_name} = {value};"


# py = Python('Intermediate', 'Backend')
# print(py.write_function('get_code', 'a'))
# print(py.create_variable('name', 'John'))

# js = JavaScript('Advanced', 'Frontend')
# print(js.write_function('validate', 'form'))
# print(js.create_variable('password', 'john@123'))

# TASK 7

# class Money:

#     def __init__(self, contry, symbol):
#         self.contry = contry
#         self.symbol = symbol


# class Rate:

#     dollar_coruse = 84.80
#     euro_course = 98.40


# class Dollar(Money, Rate):

#     def rate(self, money):
#         self.money = money
#         return f"$ {self.money} равен {self.money * self.dollar_coruse} сомам"


# class Euro(Money, Rate):

#     def rate(self, money):
#         self.money = money
#         return f"$ {self.money} равен {self.money * self.euro_course} сомам"


# money = Money("Киргизия", "som")
# dollar = Dollar
# rate = Rate()
# print(dollar.rate(100))
# euro = Euro()
# print(euro.rate(80))

# TASK 8

# class Planet:
#     def __init__(self, orbit):
#         self.orbit = orbit


# class Mercury(Planet):
#     def get_age(self, earth_age):
#         return f'на Меркурии ваш возраст составляет {int(earth_age * 365 /self.orbit)} лет'


# class Venus(Planet):
#     def get_age(self, earth_age):
#         return f'на Венере ваш возраст составляет {round(earth_age * 365 / self.orbit * 365)} дней'


# class Jupiter(Planet):
#     def get_age(self, earth_age):
#         return f'на Юпитере ваш возраст составляет {round(earth_age * 365 // self.orbit * 365 * 24)} часов'


# mercury = Mercury(88)
# venus = Venus(225)
# jupiter = Jupiter(12)

# print(venus.get_age(20))
# print(jupiter.get_age(20))
# print(mercury.get_age(20))


# class Planet:
#     def __init__(self, orbit):
#         self.orbit = orbit


# class Mercury(Planet):
#     def get_age(self, earth_age):
#         return f'на Меркурии ваш возраст составляет {int(earth_age * 365 /self.orbit)} лет'


# class Venus(Planet):
#     def get_age(self, earth_age):
#         return f'на Венере ваш возраст составляет {round(earth_age * 365 / self.orbit)} дней'


# class Jupiter(Planet):
#     def get_age(self, earth_age):
#         return f'на Юпитере ваш возраст составляет {round(earth_age * 365 * 24 / self.orbit)} часов'


# mercury = Mercury(88)
# venus = Venus(225)
# jupiter = Jupiter(12)

# print(venus.get_age(20))
# print(jupiter.get_age(20))
# print(mercury.get_age(20))
