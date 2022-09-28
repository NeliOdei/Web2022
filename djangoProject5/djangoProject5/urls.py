from django.contrib import admin
from django.urls import path
from lab import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('recipes_info/<int:id>/', views.recipe, name='recipes_url'),
    path('Users_info/<int:id>/', views.user, name='users_url')
]
