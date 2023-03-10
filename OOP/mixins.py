# Mixins - это классы которые будут использоваться для наследования, но от этих миксинов не создают объекты
# Для чего используют Mixins:
# 1. Вы хотите предоставить множества доп. функии(методов) для классов
# 2. Вы хоитет использовать одну конкретную функцию во множестве разных классов

# class Machines:

#     def start_engine(self):
#         print("Started engine!")


# class Radio_mixin:

#     def play_radio(self):
#         print("Music is playing")


# class Auto(Machines, Radio_mixin):
#     pass


# class Plane(Machines):
#     pass


# class Traine(Machines, Radio_mixin):
#     pass


# auto = Auto()
# # auto.start_engine()
# # auto.play_radio()
# plane = Plane()
# # plane.start_engine()
# # plane.play_radio()
# traine = Traine()
# # traine.start_engine()
# # traine.play_radio()

# auto.start_engine()
# auto.play_radio()

# plane.start_engine()

# traine.start_engine()
# traine.play_radio()

# -------------------------------------------------------------

# class FlyMixin:
#     def fly(self):
#         print('я могу летать')


# class WalkMixin:
#     def walk(self):
#         print('я могу ходить')


# class SwimMixin:
#     def swim(self):
#         print('я могу плыть')


# class Human(WalkMixin, SwimMixin):
#     name = 'человек'

#     def talk(self):
#         print('я могу говорить')


# class Fish(SwimMixin):
#     name = 'рыба'


# class Exocoetidae(SwimMixin, FlyMixin):
#     name = 'летучая рыба'


# class Duck(SwimMixin, WalkMixin, FlyMixin):
#     name = 'утка'


# duck = Duck()
# duck.fly(), duck.walk(), duck.swim()

# -------------------------------------------------------------



