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
        fields = ('email', 'username', 'first_name', 'last_name', 'password')

        model = User
        lookup_field = "username"
        lookup_value_regex = "[^/]+"


class UserSerializerSimpleUser(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)

    class Meta:
        fields = ('email', 'username', 'first_name', 'last_name', 'password')
        model = User
        lookup_field = "username"
        lookup_value_regex = "[^/]+"
