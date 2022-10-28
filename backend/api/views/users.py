import djoser.views
from djoser.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers.users import (SubscribeSerializer,
                                   SubscriptionShowSerializer, CustomUserSerializer, CustomUserCreateSerializer)
from users.models import Follow, User


class UserViewSet(djoser.views.UserViewSet):

    @action(['get'], detail=False)
    def me(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'Пользователь не авторизован'}, status=status.HTTP_401_UNAUTHORIZED)

        self.get_object = self.get_instance
        if request.method == 'GET':
            return self.retrieve(request, *args, **kwargs)

    @action(
        detail=True,
        methods=['post', 'delete'],
        permission_classes=(permissions.IsAuthenticated,)
    )
    def subscribe(self, request, **kwargs):
        """Позволяет текущему пользователю подписываться/отписываться от
        от автора контента, чей профиль он просматривает."""

        target_user = int(kwargs['id'])
        author = get_object_or_404(User, id=target_user)
        if request.method == 'POST':
            serializer = SubscribeSerializer(
                data={'user': request.user.id, 'following': author.id}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            author_serializer = SubscriptionShowSerializer(
                author, context={'request': request}
            )
            return Response(
                author_serializer.data, status=status.HTTP_201_CREATED
            )
        subscription = get_object_or_404(
            Follow, user=request.user, following=author
        )
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=False,
        methods=['get'],
        permission_classes=(permissions.IsAuthenticated,)
    )
    def subscriptions(self, request):
        """Позволяет текущему пользователю
        просмотреть свои подписки."""

        queryset = User.objects.filter(following__user=request.user)

        serializer = self.get_serializer(queryset, many=True)
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )

    def get_serializer_class(self):
        if self.action in ['subscribe', 'subscriptions']:
            return SubscriptionShowSerializer
        elif self.action == 'create':
            return CustomUserCreateSerializer
        elif self.action == 'set_password':
            return settings.SERIALIZERS.set_password
        return CustomUserSerializer


