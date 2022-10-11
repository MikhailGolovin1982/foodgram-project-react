from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views.ingredients import IngredientViewSet


router = SimpleRouter()
router.register('ingredients', IngredientViewSet)


urlpatterns = [
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),  # Работа с токенами.
    path('', include(router.urls)),
]
