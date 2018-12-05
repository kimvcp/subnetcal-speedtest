from django.urls import path
import views

urlpatterns = [
    path('',views.index,name='index'),
    path('subnet/',views.subnet,name='subnet'),
]