from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
import requests
from rest_framework.response import Response
from api.models import Recipes
# Create your views here.

class HomeView(TemplateView):
    template_name = "main/home.html"

class GetRecipe(ListView):
    model = Recipes
    context_object_name = "recipe"
    template_name = "main/getRecipes.html"
    