from rest_framework import serializers
from users.models import Ingredient, User


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')

# http://localhost/api/ingredients/
# http://localhost/api/ingredients/{id}/


class TokenSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
