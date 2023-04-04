from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home',views.home, name='home'),
    path('works', views.works, name='works'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact')
]
