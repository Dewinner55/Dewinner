from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(verbose_name='Название товара', max_length=60)
    price = models.DecimalField(verbose_name='Цена', max_digits=4, decimal_places=2)
    description = models.TextField(verbose_name='Описание товара', max_length=500, blank=True, null=True)
    quantity = models.IntegerField(verbose_name='Количество товаров на складе')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

