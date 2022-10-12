from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views.recipes import IngredientViewSet, TagViewSet, RecipeViewSet

router = SimpleRouter()
router.register('ingredients', IngredientViewSet)
router.register('tags', TagViewSet)
router.register('recipes', RecipeViewSet)


urlpatterns = [
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),  # Работа с токенами.
    path('', include(router.urls)),
]
