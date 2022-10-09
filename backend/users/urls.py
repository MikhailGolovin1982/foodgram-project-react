from django.urls import path, include
from rest_framework.authtoken import views

from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import UserViewSet, get_token

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
#     path('api/', include('djoser.urls')),  # Работа с пользователями.
#     path('api/', include('djoser.urls.authtoken')),  # Работа с токенами.
# ]

router = SimpleRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    # path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),  # Работа с токенами.
    # path('', include(auth_patterns)),
    # path('auth/', include(auth_patterns)),
]
