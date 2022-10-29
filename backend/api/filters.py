from django_filters import rest_framework as filters

from recipes.models import Recipe


class RecipeFilter(filters.FilterSet):
    tags = filters.CharFilter(field_name='tags__slug')
    # category = filters.CharFilter(field_name='category__slug')
    # genre = filters.CharFilter(field_name='genre__slug')
    # name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    # year = filters.NumberFilter(field_name='year')

    class Meta:
        model = Recipe
        fields = (
            'tags',
        )
