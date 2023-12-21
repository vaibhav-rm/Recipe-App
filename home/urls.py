from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_recipe/<id>/', views.delete_recipe, name="delete_recipe"),
    path('update_recipe/<id>/', views.update_recipe, name="update_recipe")
]
