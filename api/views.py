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
        url = "https://person-stream.clearbit.com/v1/people/email/alex@alexmaccaw.com"
        token = "-u sk_990572798c73dacbc19933426c0ff168:"
        headers = {'Authorization': 'Token sk_990572798c73dacbc19933426c0ff168:'}
        hed={"username": "sk_990572798c73dacbc19933426c0ff168:"}
        rsp = requests.request(method, url, headers=headers, auth=hed)
        print(rsp.content)
        # data = ClearBitSerializer(ClearBitData(), request.data)
        # getData = requests.post("https://person-stream.clearbit.com/v1/people/email/alex@alexmaccaw.com -u sk_990572798c73dacbc19933426c0ff168:")
        # print(getData.content)
        # if data.is_valid(raise_exception=True):
    
        #     data.save()
        #     return Response(data.data )
        # else:
        #     return Response({"email": "is not valid"})
        return Response(rsp )
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

# patrick@stripe.com

# {"username": "adawfrgsdegts34", 
# "email": "patrick@stripe.com",
#  "password":  "kskslfk224"}

# sk_990572798c73dacbc19933426c0ff168 streetAddress foundedYear sectordomain location linkedin employees estimatedAnnualRevenue 

