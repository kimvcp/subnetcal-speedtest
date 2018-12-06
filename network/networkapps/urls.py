from django.urls import path
from networkapps import views

urlpatterns = [
    path('',views.index,name='index'),
]