from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes", null=True)
    title = models.CharField(max_length=255)
    ingredient = models.TextField()
    recipe = models.TextField()
    author = models.CharField(default=User,max_length=255)
    rating = models.IntegerField()

    def __str__(self):
            return self.title

class ClearBitData(models.Model):
    domain = models.CharField(max_length=255)
    streetAddress = models.CharField(max_length=255)
    foundedYear = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)


