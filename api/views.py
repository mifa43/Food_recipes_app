from turtle import title
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Recipes
from api.serializers import RecipesSerializer
from django.views.decorators.csrf import csrf_protect
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

        return Response(rec.data)  


# {
#     "title": "asfasf",
#     "ingredient": "bbbb", 
#     "recipe": "asfadfgcvb", 
#     "author":"sfxbbb",
#     "rating":1

# }
# request body