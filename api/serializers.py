from rest_framework import serializers
from .models import Recipes

class RecipesSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=200)
    title = serializers.CharField(max_length=200)
    ingredient = serializers.CharField()
    recipe = serializers.CharField()
    author = serializers.CharField(max_length=200)
    
    rating = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = Recipes
        fields = ('__all__')