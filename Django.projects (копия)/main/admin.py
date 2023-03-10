from django.contrib import admin

from main.models import City, Car, Musician, Song, Award

# Register your models here.
admin.site.register(City)
admin.site.register(Car)
admin.site.register(Musician)
admin.site.register(Song)
admin.site.register(Award)