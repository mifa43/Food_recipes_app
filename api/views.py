from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Recipes
from api.serializers import RecipesSerializer

# Create your views here.


@api_view(["GET"])  # kao i u fastapi deklaracija metode
def getRecipes(request):    
    if request.method == 'GET':
        rec = Recipes.objects.all() 
    serializer = RecipesSerializer(rec, many=True)
    return Response(serializer.data)
