from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Recipes
from api.serializers import RecipesSerializer, UserSerializer
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django.contrib.auth.models import User
import requests
# Create your views here.


@api_view(["GET"])  # kao i u fastapi deklaracija metode
def getRecipes(request):    
    if request.method == 'GET':
        rec = Recipes.objects.all() 
    serializer = RecipesSerializer(rec, many=True)
    return Response(serializer.data)

@csrf_protect
@api_view(["POST"])  # kao i u fastapi deklaracija metode
def postRecipes(request):    
    if request.method == 'POST':
        rec = RecipesSerializer(Recipes(), request.data)    # |TypeError: Model.save() missing 1 required positional argument: 'self'|*Recipes() reseno sa
        if rec.is_valid(raise_exception=True):  # validacija request.data
            rec.save()  #cuvanje u elastic
            return Response(rec.data)#redirect('home')

        return Response(rec.data)  

@csrf_protect
@api_view(["POST"])
def register(request):
    if request.method == 'POST':
        reg = UserSerializer(User(), request.data)
        email = requests.get("https://api.hunter.io/v2/email-verifier?email=mifa43kotez@gmail.com&api_key=9da638a648b2befb4689c7d152cc8cb07ad1a7e8")
        if reg.is_valid(raise_exception=True):
            print(email.content)

            # reg.save()
            return Response(reg.data )
        return Response(reg.data )
# { 
#     "title": "asfasf",
#     "ingredient": "bbbb", 
#     "recipe": "asfadfgcvb", 
#     "author":"sfxbbb",
#     "rating":1
# }
# # request body

# {"username": "adgsdegts34", 
# "email": "mifa43@gmail.com",
#  "password":  "kskslfk224"}