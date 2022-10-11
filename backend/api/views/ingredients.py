from rest_framework import viewsets, permissions

from recipes.models import Ingredient
from api.serializers.ingredients import IngredientSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    pagination_class = None
    search_fields = ('name',)
