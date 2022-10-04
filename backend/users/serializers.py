from rest_framework import serializers
from .models import Ingredient, User


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')

# http://localhost/api/ingredients/
# http://localhost/api/ingredients/{id}/


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password')
        lookup_field = "username"
        lookup_value_regex = "[^/]+"


class UserSerializerAnswer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name')
        lookup_field = "username"
        lookup_value_regex = "[^/]+"


class TokenSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
