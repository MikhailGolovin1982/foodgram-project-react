from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, CurrentUserDefault
from rest_framework.validators import UniqueTogetherValidator

# from api.serializers.recipes import RecipeSerializerShort
from users.models import User, Follow


class UserSerializer(serializers.ModelSerializer):
    is_subscribed = SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'id', 'username', 'first_name', 'last_name', 'is_subscribed']

    def get_is_subscribed(self, obj):
        request_user = self.context.get('request').user
        if not request_user.is_authenticated:
            return False
        elif request_user == obj:
            return False

        return Follow.objects.filter(user=request_user, following=obj).exists()


# class SubscribeSerializerRepresentation(serializers.ModelSerializer):
#     author = UserSerializer(read_only=True)
#     recipes = RecipeSerializerShort(many=True, read_only=True)
#
#     class Meta:
#         model = User
#         fields = ['author', 'recipes']


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user', 'following')
        model = Follow

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following'],
                message='Only unique following is possible'
            )
        ]

    def validate(self, data):
        """Проверяем, что пользователь не подписывается на самого себя."""
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                'Подписка на cамого себя не имеет смысла'
            )
        return data

    # def to_representation(self, instance):
    #             serializer = SubscribeSerializerRepresentation(instance)
    #             return serializer.data
