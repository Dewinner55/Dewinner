# OOП - объектно ориентированное программировние
# Класс -> описание как должен выглядить объект то есть в классе мы описываем какими свойствами/то есть данными и поведениями/ то есть фукнциями должен обладать объект
# Объект -> сущность которую мы создаём от класса, у объекта есть собственное состояние свойств/ то есть данных
# Целью создания было связать данные(атрибуты) с функциями(методы) которые использовали их

# Свойствами/либо (атрибутами) - называют обычные переменные внутри класса, которых храняться данные определенного объекта
# Методы - обычные функции которые описывают поведения объекта, функции внутри класса называют методами

# john_dannyi = ["John", "Snow", 30, "King of North", 5000]


# def show_info(human):
# print(
# f"Name: {human[0]} {human[1]}, age:{human[-1]}, job: {human[2]}, salary: {human[3]}")


# show_info(john)
# ------------------------------------------------------------------------------------------------
# class Human:

#     def __init__(self, name, last_name, age, job, salary) -> None:
#         self.name = name + " " + last_name
#         self.age = age
#         self.job = job
#         self.salary = salary

#     def show_info(self):
#         return f"Name: {self.name}, age: {self.age}, job: {self.job}, salary: {self.salary}"


# john_dannyi = ["John", "Snow", 30, "King of North", 5000]
# print(type(john_dannyi))
# # john = Human(john_dannyi)
# john = Human("John", "Snow", 30, "King of North", 5000)
# print(type(john))
# sultan = Human("Sultan", "Katana", 19, "Mentor", 100)

# # print(dir(john))
# print(john.show_info())
# # print(john.name)
# # print(john.age)
# print("")
# print(sultan.show_info())


# class Dog:
#     age = 0
#     ushi = True
#     # Атрибуты класса

#     def __init__(self, name, color):
#         # Инициализатор, именно здесь создаются атрибуты объекта
#         # В self прилетает ссылка на объект от класса
#         self.name = name  # атрибута объекта
#         self.color = color

#     def bark(self):
#         return (f"{self.name} лает!")


# bobik = Dog("Bobik", "Brown")
# yumi = Dog(name="Yumi", color="White")
# aktosh = Dog("Aktosh", "Gray")

# print(
#     f"name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, ushi: {bobik.ushi}")
# print(
#     f"name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, ushi: {yumi.ushi}")
# print(
#     f"name: {aktosh.name}, age: {aktosh.age}, color: {aktosh.color}, ushi: {aktosh.ushi}")

# print("")

# bobik.age = 2
# yumi.age = 1
# aktosh.age = 3
# aktosh.ushi = False

# print("After")
# print(
#     f"name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, ushi: {bobik.ushi}")
# print(
#     f"name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, ushi: {yumi.ushi}, {yumi.bark()}")
# print(
#     f"name: {aktosh.name}, age: {aktosh.age}, color: {aktosh.color}, ushi: {aktosh.ushi}")


class Human:
    age = 0

    def __init__(self) -> None:
        self.raychel = "Raychel"
        print("init worked")

    def method1(self):
        self.john = "John"
        self.raychel = "John"
        print("methon1 worked")
        return self.john, self.raychel


object = Human()
# print(f"{object.raychel}, {object.method1()}")
print()
# object.method1()
print(object.raychel)
