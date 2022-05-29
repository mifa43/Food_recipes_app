from rest_framework import serializers
from .models import Recipes
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault

# u fastapi-u kao pydantic modeli
class RecipesSerializer(serializers.ModelSerializer):
    user = CurrentUserDefault()
    title = serializers.CharField(max_length=200)
    ingredient = serializers.CharField()
    recipe = serializers.CharField()
    author = serializers.CharField(max_length=200)
    
    rating = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = Recipes
        fields = ('__all__')