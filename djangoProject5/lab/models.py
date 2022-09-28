from django.db import models
from django.db import models
from django.db import models

from django.db import models
# Create your models here.
class Users(models.Model):
    Nickname = models.CharField(max_length=20)
    Name = models.CharField(max_length=50)
    Birth_date = models.DateField()
    Phone = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    E_mail = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'Users'
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
class Products(models.Model):
    Product_Name = models.CharField(max_length=20)
    KPFC = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'Products'
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
class Recipes(models.Model):
    Recipe_Name = models.CharField(max_length=40)
    Category = models.CharField(max_length=50)
    Users = models.ForeignKey(Users, on_delete = models.CASCADE)
    Cooking_time = models.TimeField()
    Level = models.IntegerField()
    KPFC = models.CharField(max_length=50)
    Vegan = models.BinaryField()
    Descr = models.CharField(max_length=1000)
    class Meta:
        managed = False
        db_table = 'Recipes'
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
class Composition(models.Model):
    Recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    Products = models.ForeignKey(Products, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'Composition'
        verbose_name = "Состав"
        verbose_name_plural = "составы"
# Create your models here.

# Create your models here.

# Create your models here.

# Create your models here.
