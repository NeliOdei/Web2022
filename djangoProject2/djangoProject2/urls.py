from django.contrib import admin
from django.urls import path

from bmstu_lab import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GetOrders),
    path('order/<int:id>/', views.GetOrder, name='order_url'),
]


#urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('hello/', views.hello),
#]