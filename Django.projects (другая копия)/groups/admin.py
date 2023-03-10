from django.contrib import admin

from groups.models import Teacher, Student, Group_Students, Group
# Register your models here.

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Group_Students)
# admin.site.register(Group)

@admin.register(Group)
class Groups(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'count_students', 'list_of_students')


    def count_students(self, obj):
        info = Group_Students.objects.filter(group_id=obj)
        return info.count()
    count_students.short_description = 'Количество студентов'


    def list_of_students(self, obj):
        info = Group_Students.objects.filter(group_id=obj)
        result = []
        for x in info:
            x = str(x)
            index = x.index(('->'))
            result.append(x[:index])


        return result
    list_of_students.short_description = 'Студенты'
