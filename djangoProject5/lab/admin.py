from django.contrib import admin

from django.contrib import admin
from .models import Users, Recipes, Products, Composition
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Product_Name')
    list_display_links = ('id', 'Product_Name')
admin.site.register(Products, ProductsAdmin)
# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nickname')
    list_display_links = ('id', 'Nickname')
admin.site.register(Users, UsersAdmin)

class RecipesAdmin(admin.ModelAdmin):
    list_display = ('id', 'Recipe_Name')
    list_display_links = ('id', 'Recipe_Name')
admin.site.register(Recipes, RecipesAdmin)

class CompositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'Recipes_id', 'Products_id' )
admin.site.register(Composition, CompositionAdmin)