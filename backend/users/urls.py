from django.urls import path, include

from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import UserViewSet, get_token

router = SimpleRouter()

auth_patterns = [
    path('auth/token/login/', get_token),    # To get TOKEN
    # path('auth/token/logout/', del_token),    # To delete TOKEN
]

router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(auth_patterns)),
    # path('auth/', include(auth_patterns)),
]
