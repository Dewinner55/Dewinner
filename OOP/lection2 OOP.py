#############    Переменных класса и экземпляра    #############

'''
При изучении объектно-ориентированного программирования на Python может возникнуть несколько сложностей, когда дело доходит до разграничения переменных класса и экземпляра. Давайте разберем разницу между переменными класса и экземпляра и посмотрим примеры, демонстрирующие различные варианты использования.

Во-первых,помним что классы часто представляют что-то в реальном мире, так что представьте, хотите ли вы создать класс, списка студентов. Вы можете создать класс с именем Student, который представляет собой шаблон, который определяет различные атрибуты студента. Таким образом, каждый студент является экземпляром класса Student.

При работе с данными любого типа некоторые атрибуты будут уникальными, а некоторые будут общими. Рассмотрим пример с учениками: у каждого учащегося в этом классе один и тот же номер и один учитель, но у каждого из них есть уникальное имя, возраст и любимый предмет.

Переменные класса.
Переменные класса обычно являются переменными, которые являются общими для всех экземпляров. И они определены так:
'''

# class Student:
#    teacher = 'Gulzana eje'  # переменная класса

'''
Каждый экземпляр класса будет иметь одинаковое значение для этих переменных:
'''

# adinay = Student()
# semetey = Student()

# print(adinay.teacher)
# # Gulzana eje

# print(semetey.teacher)
# # Gulzana eje

'''
Переменные экземпляра.
Переменные экземпляра (также называемые атрибутами данных) уникальны для каждого экземпляра класса и определяются в методе класса, например:
'''

# class Student:
#    teacher = 'Mrs. Jones'  # переменная класса

#    def __init__(self, name):
#        self.name = name  # переменная экземпляра

'''
Посмотрите, как каждый экземпляр теперь содержит уникальное значение name:
'''

# adinay = Student('Adinay')
# semetey = Student('Semetey')

# print(adinay.name)
# # Adinay

# print(semetey.name)
# # Semetey

'''
Чего ожидать от переменных класса.
Переменные класса являются общими для всех экземпляров класса. Напоминаем, что они определены так:
'''

# class Student:
#    teacher = 'Gulzana eje'
