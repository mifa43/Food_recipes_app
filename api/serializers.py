from rest_framework import serializers
from .models import Recipes, ClearBitData
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
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
        fields = ("__all__")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate_password(self, value: str) -> str:

        return make_password(value) # algorithm za password resen problem 


class ClearBitSerializer(serializers.ModelSerializer):

    domain = serializers.CharField(max_length=255)
    streetAddress = serializers.CharField(max_length=255)
    foundedYear = serializers.CharField(max_length=255)
    linkedin = serializers.CharField(max_length=255)

    class Meta:
        model = ClearBitData
        fields = ("__all__")

class UserTokenSerialiser(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "id")

            