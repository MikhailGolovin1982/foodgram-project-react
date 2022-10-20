from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views.recipes import IngredientViewSet, TagViewSet, RecipeViewSet
from api.views.users import SubscribeViewSet

router = SimpleRouter()
router.register('ingredients', IngredientViewSet)
router.register('tags', TagViewSet)
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path(r'recipes/<int:id>/favorite/', RecipeViewSet.as_view({'post': 'favorite', 'delete': 'favorite'})),
    path(r'users/<int:id>/subscribe/', SubscribeViewSet.as_view({'post': 'subscribe', 'delete': 'subscribe'})),
    path(r'users/subscriptions/', SubscribeViewSet.as_view({'get': 'subscriptions'})),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),  # Работа с токенами.
    path('', include(router.urls)),
]
