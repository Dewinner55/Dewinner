# Принципы ООП:
# 1. Наследование
# 2. Инкапсуляция
# 3. Полиморфизм
# 4. Абстракция
# 5. Композиции
# 6. Агрегация

# Наследование - позволяет принимать методы и атрибуты для дочернего класса
# Родительский класс
# Дочерний класс

# class Animal:
#     def print_info(self):
#         print("I'm an animal!")

# class Croco(Animal):
#     pass

# croco = Croco()
# croco.print_info()

# class Animal:
#     name = None
#     golos = None
#     meal = None

#     def say(self):
#         print(f"This animal is {self.name}: {self.golos}")

#     def eat(self):
#         print(f"This animal is {self.name}: {self.meal}")

# class Lion(Animal):
#     name = "Lion"
#     golos = "roar"
#     meal = "meat"


# class Dog(Animal):
#     name = "Dog"
#     golos = "bark"
#     meal = "meat"


# class Koala(Animal):
#     name = "Koala"
#     golos = "roar"
#     meal = "efkalipt"

# rex = Dog()
# simba = Lion()
# julian = Koala()

# rex.say()
# rex.eat()

# simba.say()
# simba.eat()

# julian.say()
# julian.eat()
# -----------------------------------------------------------
# class Laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def get_info(self):
#         return {"brand": self.brand, "model": self.model, "price": self.price}


# class MacBook(Laptop):
#     def __init__(self, brand, model, price, year, display):
#         super().__init__(brand, model, price)
#         self.year = year
#         self.display = display

#     def get_info(self):
#         repr = super().get_info()
#         repr["year"] = self.year
#         repr["display"] = self.display
#         return repr


# class Acer(Laptop):
#     def __init__(self, brand, model, price, videocard, displya):
#         super().__init__(brand, model, price)
#         self.videocard = videocard
#         self.display = displya

#     def get_info(self):
#         repr = super().get_info()
#         repr["videocard"] = self.videocard
#         repr["display"] = self.display
#         return repr


# mac = MacBook("Apple", "Air", "1000$", 2022, 13)
# print(mac.get_info())
# acer = Acer("Acer", "FX", "1500$", 2022, 16)
# print(acer.get_info())
# ----------------------------------------------------------

# class Employee:
#     bonus = 1.5

#     def __init__(self, name, lastname, salary):
#         self.name = f"{name} {lastname}"
#         self.salary = salary

#     def get_info(self):
#         return f"FIO: {self.name} Salary: {self.salary}"

#     def give_increase(self):
#         self.salary = self.salary * self.bonus
#         # return f"\nSalary_Bonus: {self.salary}"

#     def __str__(self) -> str:
#         return self.get_info()


# class Developer(Employee):
#     def __init__(self, name, lastname, salary, language):
#         super().__init__(name, lastname, salary)
#         self.language = language

#     def get_info(self):
#         info = super().get_info()
#         info += f", Pro Language: {self.language}"
#         return info


# class Manager(Employee):
#     def __init__(self, name, lastname, salary, devs=[]):
#         super().__init__(name, lastname, salary)
#         self.devs = devs

#     def add_devs(self, developer):
#         self.devs.append(developer)

#     def show_devs(self):
#         return [x.get_info() for x in self.devs]


# dev1 = Developer("John", "Snow", 1000, "Python")
# dev2 = Developer("Brad", "Pit", 2000, "C++")
# dev3 = Developer("Kristial", "Beil", 3000, "JS")
# dev4 = Developer("Monika", "Beluchi", 800, "Paskal")

# man1 = Manager("Harisson", "Ford", 5000)
# man2 = Manager("Genri", "Kavil", 11_000, [dev1, dev2])

# print(f"\nManager {man1.get_info()}, has {man1.show_devs()} developers")
# print("------------------------------------------------")
# print(f"Manager {man2.get_info()}, has {man2.show_devs()} developers")
# print("------------------------------------------------")

# man1.add_devs((dev1))
# man1.add_devs((dev4))
# print("")
# print("After")
# print(f"\nManager {man1.get_info()}, has {man1.show_devs()} developers")
# print("------------------------------------------------")
# print(f"Manager {man2.get_info()}, has {man2.show_devs()} developers")
# print("------------------------------------------------")

# dev1.give_increase()
# man2.give_increase()

# print("")
# print("After Bonus")
# print("")
# print(dev1)
# print("------------------------------------------------")
# print(man2)
