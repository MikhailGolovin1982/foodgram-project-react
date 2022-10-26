from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views.recipes import IngredientViewSet, RecipeViewSet, TagViewSet
from api.views.users import SubscribeViewSet, UserViewSet

router = SimpleRouter()
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('tags', TagViewSet, basename='tags')
router.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path(r'recipes/<int:id>/shopping_cart/',
         RecipeViewSet.as_view({'post': 'shopping_cart', 'delete': 'shopping_cart'})),
    path('recipes/download_shopping_cart/',
         RecipeViewSet.as_view({'get': 'download_shopping_cart'})),
    path(r'recipes/<int:id>/favorite/', RecipeViewSet.as_view({'post': 'favorite', 'delete': 'favorite'})),
    path(r'users/<int:id>/subscribe/', SubscribeViewSet.as_view({'post': 'subscribe', 'delete': 'subscribe'})),
    path('users/me/', UserViewSet.as_view({'get': 'me'})),
    path('users/subscriptions/', SubscribeViewSet.as_view({'get': 'subscriptions'})),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]
