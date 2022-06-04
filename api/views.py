from cgitb import handler
from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Recipes, ClearBitData
from api.serializers import RecipesSerializer, UserSerializer, ClearBitSerializer
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django.contrib.auth.models import User
import requests
from requests.auth import HTTPBasicAuth
import os
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
        email = requests.get(f"https://api.hunter.io/v2/email-verifier?email={request.data['email']}&api_key=9da638a648b2befb4689c7d152cc8cb07ad1a7e8")
        handler = email.json()
        print(request.data["email"])
        if handler["data"]["webmail"] == True:

            if reg.is_valid(raise_exception=True):
    
                reg.save()
                return Response(reg.data )
        else:
            return Response({"email": "is not valid"})
        return Response(reg.data )

@csrf_protect
@api_view(["POST"])
def clearBitApi(request):
    if request.method == 'POST':
        method = "get"
        url = f"https://person.clearbit.com/v2/combined/find?email={request.data['email']}"
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer {0}'.format(os.getenv("DJANGO_CLEARBIT_APIKEY"))
            }
        rsp = requests.request(method, url, headers=headers)
        r = rsp.json()
        ds = {
            "domain": r["company"]["domain"],
            "streetAddress": r["company"]["geo"]["streetAddress"],
            "foundedYear": r["company"]["foundedYear"],
            "linkedin": "linkedin.com/" + r["company"]["linkedin"]["handle"]
            }
        data = ClearBitSerializer(ClearBitData(), ds)
        try:
            if data.is_valid(raise_exception=True):
        
                data.save()
                return Response(data.data )
        except:
     
            return Response({"domain": "exists"})
# {"email": "patrick@stripe.com"}