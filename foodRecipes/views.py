from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import render
import requests
from rest_framework.response import Response
from api.models import Recipes
from api.serializers import UserSerializer
from foodRecipes.forms import RegisterForm
# Create your views here.

class HomeView(TemplateView):
    template_name = "main/home.html"

class GetRecipe(ListView):
    model = Recipes
    context_object_name = "recipe"
    template_name = "main/getRecipes.html"

class Register(CreateView):
    form_class = RegisterForm
    template_name = "main/register/register.html"
    # success_url = reverse_lazy("home")

class SearchView(TemplateView):
    template_name = "main/search.html"
    # context_object_name = "recipe"
