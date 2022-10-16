from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

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
