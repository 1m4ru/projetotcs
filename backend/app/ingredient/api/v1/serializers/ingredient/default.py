"""
API V1: Ingredient Serializers
"""
###
# Libraries
###
from rest_framework import serializers
from app.ingredient.models.ingredient import Ingredient
###
# Serializers
###


class DefaultIngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'
