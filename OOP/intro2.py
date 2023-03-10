# class Human:
#     age = 0

#     def __init__(self, name, lastname, wieght, nationality) -> None:
#         self.name = name + " " + lastname
#         self.wieght = wieght
#         self.nationality = nationality

#     def birthday(self):
#         import random
#         print(f"\nHappy birthday, {self.name}!!!")
#         self.age += 1
#         self.wieght += random.randint(3, 6)


# object1 = Human("John", "Snow", 3.3, "American")
# object2 = Human("Abu", "Bakr", 3.8, "Arabic")
# print("-----------------------------------------------")
# print(f"\nname {object1.name}\nwieght {object1.wieght}\nnationality {object1.nationality}\nage {object1.age}")
# print(f"\nname {object2.name}\nwieght {object2.wieght}\nnationality {object2.nationality}\nage {object2.age}")
# print("\nafter 1 year: ")
# object1.birthday()
# object2.birthday()
# print("-----------------------------------------------")
# print(f"\nname {object1.name}\nwieght {object1.wieght}\nnationality {object1.nationality}\nage {object1.age}")
# print(f"\nname {object2.name}\nwieght {object2.wieght}\nnationality {object2.nationality}\nage {object2.age}")
# print("\nafter 2 year: ")
# object1.birthday()
# object2.birthday()
# print("-----------------------------------------------")
# print(f"\nname {object1.name}\nwieght {object1.wieght}\nnationality {object1.nationality}\nage {object1.age}")
# print(f"\nname {object2.name}\nwieght {object2.wieght}\nnationality {object2.nationality}\nage {object2.age}")
# print("\nafter 3 year: ")
# object1.birthday()
# object2.birthday()
# print("-----------------------------------------------")
# print(f"\nname {object1.name}\nwieght {object1.wieght}\nnationality {object1.nationality}\nage {object1.age}")
# print(f"\nname {object2.name}\nwieght {object2.wieght}\nnationality {object2.nationality}\nage {object2.age}")
# print("\nafter 4 year: ")
# object1.birthday()
# object2.birthday()
# print("-----------------------------------------------")
# print(f"\nname {object1.name}\nwieght {object1.wieght}\nnationality {object1.nationality}\nage {object1.age}")
# print(f"\nname {object2.name}\nwieght {object2.wieght}\nnationality {object2.nationality}\nage {object2.age}")
# print("\nafter 5 year: ")
# object1.birthday()
# object2.birthday()
# print("-----------------------------------------------")
# print(f"\nname {object1.name}\nwieght {object1.wieght}\nnationality {object1.nationality}\nage {object1.age}")
# print(f"\nname {object2.name}\nwieght {object2.wieght}\nnationality {object2.nationality}\nage {object2.age}")
# print("\nafter 6 year: ")
# object1.birthday()
# object2.birthday()

# _________________________________________________________________________________

# class Students():
#     univer = "MIT"

#     def __init__(self, name, lastname):
#         self.name = f"{name} {lastname}"
#         self.books = []
#         self.languages = {}
#         self.knowledge = 0
#         self.is_ready_to_work = False

#     def add_points(self, points):
#         self.knowledge += points
#         if self.knowledge > 500:
#             self.is_ready_to_work = True

#     def ready_to_work(self):
#         if self.is_ready_to_work == True:
#             print(f"{self.name} is ready to work!!")

#     def read_book(self, book):
#         self.books.append(book)
#         self.add_points(50)

#     def do_lab_work(self):
#         self.add_points(50)

#     def dp_project(self):
#         self.add_points(100)

#     def learn_new_languages(self, languages, points):
#         if not points in range(70, 101):
#             raise Exception("Invalid points")
#         self.languages.setdefault("Languages", languages)
#         self.add_points(points)


# students1 = Students("john", "Snow")
# students2 = Students("Jamie", "Lanister")
# print(students1.name, "\n")
# print(students2.name, "\n")

# students1.read_book("Game of Thrones")
# students1.read_book("1984")
# students1.read_book("Nemo")
# students1.read_book("Robinzon")

# # students1.do_lab_work()
# # students1.do_lab_work()
# # students1.dp_project()
# students1.learn_new_languages("Python", 90)
# students1.learn_new_languages("C++", 75)

# students2.read_book("Game of Thrones")
# students2.read_book("1984")
# students2.read_book("Nemo")
# students2.read_book("Robinzon")

# students2.do_lab_work()
# students2.do_lab_work()
# students2.dp_project()
# students2.learn_new_languages("Python", 90)
# students2.learn_new_languages("C++", 75)

# print(
#     f"\nAfter study {students1.name}, \n{students1.books}, \n{students1.languages}, \n{students1.knowledge}")
# print(f"\nReady to work: {students1.is_ready_to_work}!")
# students1.ready_to_work()
# print("--------------------------------------------------------")
# print(
#     f"\nAfter study {students2.name}, \n{students2.books}, \n{students2.languages}, \n{students2.knowledge}")
# print(f"\nReady to work: {students2.is_ready_to_work}!")
# students2.ready_to_work()

# _________________________________________________________________________________

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def __str__(self):
#         return f"{self.brand} -> {self.model}"


# object1 = Car("BMW", "7 series")
# object2 = Car("KIA", "RIO")
# object3 = Car("Mersedes", "w140")

# object1.__str__
# print(f"{object1.brand} -> {object1.model}")
# print(" ")
# print(object1, "!")
# print(object2, "!")
# print(object3, "!")

# _________________________________________________________________________________

# class Soda:
#     def __init__(self, ingredient=None):
#         if isinstance(ingredient, str):
#             self.ingredient = ingredient
#         else:
#             self.ingredient = None

#     def show_my_drink(self):
#         if self.ingredient:
#             print(f"Gazirovka is {self.ingredient}!")
#         else:
#             print(f"Normal gazirovka!")


# a = Soda("malina")
# a.show_my_drink()

# b = Soda(5)
# b.show_my_drink()

# c = Soda(False)
# c.show_my_drink()

# d = Soda("Grusha")
# d.show_my_drink()

# _________________________________________________________________________________

# class A:
#     pass


# a = A()
# print(type(A()))
# print(type(a))
# b = 5
# print(isinstance(a, A), isinstance(b, A))

# _________________________________________________________________________________

# class TriangleCheker:
#     def __init__(self, sides: list) -> None:
#         self.sides = sides

#     def __str__(self) -> str:
#         if not all(isinstance(x, (int, float)) for x in self.sides):
#             return f"Нельзя построить треугольник! Т.к. все стороны должны быть числами!"
#         if any(x <= 0 for x in self.sides):
#             return "Нельзя построить треугольник! Т.к. все стороны должны быть больше нуля!"
#         self.sides.sort()
#         if self.sides[0] + self.sides[1] <= self.sides[-1]:
#             return "Нельзя построить треуольник т.к. сумма двух сторон должна быть больше самой длинной стороны!"
#         return "Мы можем построить треугольник"


# t1 = TriangleCheker([10, 10, 10])
# print(t1)

