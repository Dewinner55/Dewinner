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
    list_display = ('title', 'teacher', 'list_of_students')

    def list_of_students(self, obj):
        return 'John'


