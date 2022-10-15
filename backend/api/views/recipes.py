from rest_framework import viewsets, permissions

from recipes.models import Ingredient, Tag, Recipe
from api.serializers.recipes import IngredientSerializer, TagSerializer, RecipeSerializer, RecipeSerializerLight
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # pagination_class = None
    search_fields = ('name',)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action == 'create':
            return RecipeSerializerLight
        return RecipeSerializer

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
