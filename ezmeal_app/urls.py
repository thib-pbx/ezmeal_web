from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:recipe_name>/', views.view_recipe, name='view_recipe_by_name')
]