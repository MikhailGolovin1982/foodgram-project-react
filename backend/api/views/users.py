from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers.users import SubscribeSerializer, SubscriptionShowSerializer
from users.models import User, Follow


class SubscribeViewSet(viewsets.ModelViewSet):
    serializer_class = SubscribeSerializer
    queryset = User.objects.all()

    @action(
        detail=True,
        methods=['post', 'delete'],
        permission_classes=(permissions.IsAuthenticated,)
    )
    def subscribe(self, request, *args, **kwargs):
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
                # serializer.data, status=status.HTTP_201_CREATED
            )
        subscription = get_object_or_404(
            Follow, user=request.user, following=author
        )
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
