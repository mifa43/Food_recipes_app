from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Recipes
from django.contrib.auth import get_user_model

@registry.register_document
class RecipesDocument(Document):
    class Index:
        # ime index-a
        name = 'recipes'

        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Recipes # dodeljivanje modela

        # polja iz modela koja ce biti ukljucena u elastic index
        fields = [
            'title',
            'ingredient',
            'recipe',
            'author',
            'rating'
        ]