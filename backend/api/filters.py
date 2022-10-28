from django_filters import rest_framework as filters

from recipes.models import Recipe


class SubscriptionsFilter(filters.FilterSet):
    recipes_limit = filters.NumberFilter(
        field_name='recipes_limit',
        method='get_recipes_limit',
    )

    def get_recipes_limit(self, queryset, name, value):
        print(value)
        print(type(value))
        if self.request.user.is_authenticated and value:
            queryset = queryset.filter(following__user__user=self.request.user).values('recipes')[:value]
            return queryset
        return queryset

    class Meta:
        model = Recipe
        fields = [
            'recipes_limit',
        ]

# class TitleFilter(filters.FilterSet):
#     category = filters.CharFilter(field_name='category__slug')
#     genre = filters.CharFilter(field_name='genre__slug')
#     name = filters.CharFilter(field_name="name", lookup_expr='icontains')
#     year = filters.NumberFilter(field_name='year')
#
#     class Meta:
#         model = Title
#         fields = ('category', 'genre', 'name', 'year')
