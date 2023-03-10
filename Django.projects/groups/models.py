from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    languages = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.last_name}'

class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contacts = models.CharField(max_length=100)
    passport = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.last_name}'

class Group_Students(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    group_id = models.ForeignKey('Group', on_delete=models.RESTRICT)

    class Meta:
        verbose_name = 'Group student'
        verbose_name_plural = 'Group students'

    def __str__(self):
        return f'{self.student_id} -> {self.group_id}'

class Group(models.Model):
    title = models.CharField(max_length=100, verbose_name='Загаловок')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, verbose_name='Учителя')
    students = models.ManyToManyField(Student, through=Group_Students)

    def __str__(self):
        return f'{self.title}'


