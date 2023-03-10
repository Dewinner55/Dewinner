# Множественное наследование - это когда класс наследуется от двух или более классов

# mro(Methon Resolution Order) - механизм для корректного поиска родительских методов. Был создан для решения проблемы ромба после введения object в Python. Поиск идет таким образом что если у родительсикх классов один общий предок то идет поиск в ширину.

# class Auto:

#     def play_music_at_station(self):
#         print("music is playing!")

#     def ride(self):
#         print("We riding on the ground!")


# class Plane:

#     def play_music_at_station(self):
#         print("listening Ed Sheeran!")

#     def fly(self):
#         print("we're flying")


# class FutureAuto(Auto, Plane):
#     pass


# futureauto = FutureAuto()
# futureauto.fly()
# futureauto.ride()
# futureauto = Plane()
# futureauto.play_music_at_station()
# -----------------------------------------------------------

# class A:

#     def print_A(self):
#         print("A")


# class B:

#     def print_B(self):
#         print("B")


# class C:

#     def print_C(self):
#         print("C")


# class ABC(A, B, C):
#     pass


# obj = ABC()

# obj.print_A()
# obj.print_B()
# obj.print_C()

# print(ABC.mro())

# ----------------------------------------------------------

# class Test:
#     pass


# obj = Test()
# print(dir(obj))
# print("")
# obj2 = object()
# print(dir(obj2))
# print("")
# print(Test.mro())

# -----------------------------------------------------------

# Проблема ромба(решена с помощью mro())

# class Zero:

#     def say(self):
#         print("class Zero!")


# class First(Zero):

#     def say(self):
#         print("class First")


# class Second(Zero):

#     def say(self):
#         print("class Second")


# class MyClass(First, Second):

#     def say(self):
#         super().say()
#         print("My Class")


# class_ = MyClass()
# class_.say()
# print(MyClass.mro())

# ------------------------------------------------------------

# Проблема перекрестного наследования

# class Y:
#     pass


# class X:
#     pass


# class A(X, Y):
#     pass


# class B(X, Y):
#     pass


# class MyClass(A, B):
#     pass


# obj = MyClass()
# print(MyClass.mro())

