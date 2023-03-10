from django.db import models

# Create your models here.
class City(models.Model):
    title = models.CharField(max_length=150)
    country = models.CharField(max_length=155)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return f'{self.title}'


class Car(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='images')
    contacts = models.CharField(max_length=255)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title}'



class Musician(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    psevdonim = models.CharField(max_length=150, blank=True)

    def __str__(self):
        if self.psevdonim:
            return f'{self.psevdonim}'
        return f"{self.name} {self.last_name}"

class Song(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='songs')
    feat = models.ForeignKey(Musician, on_delete=models.SET_NULL, null=True, related_name='feats', blank=True)
    poster = models.ImageField(upload_to='images/posters/')
    year = models.DateField()

    def __str__(self):
        if self.feat:
            return f'{self.author} - {self.title} feat. {self.feat}'
        return f'{self.author} - {self.title}'

class Award(models.Model):
    nominant = models.OneToOneField(Musician, on_delete=models.CASCADE, related_name='award', unique=True)
    year = models.DateTimeField()

    def __str__(self):
        return f'{self.nominant} - Golden VOICE! {self.year}'
