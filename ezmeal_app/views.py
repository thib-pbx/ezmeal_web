from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
from .models import Recipes

def index(request):
    return render(request, 'ezmeal_app/index.html')

def view_recipe(request, recipe_name):
    return HttpResponse(f"Here will be displayed your recipes. This is {recipe_name}")
