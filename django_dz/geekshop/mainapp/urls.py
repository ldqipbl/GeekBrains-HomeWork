from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from mainapp import views
from geekshop import settings


app_name = 'mainapp'

urlpatterns = [
    path('', views.products, name='index'),
    path('<int:pk>', views.products, name='products'),
]
