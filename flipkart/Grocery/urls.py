from django.urls import path 
from Grocery import views

urlpatterns =[
    path('Grocery/',views.Grocery, name="Grocery")


]