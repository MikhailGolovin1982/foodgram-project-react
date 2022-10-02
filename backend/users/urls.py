from django.urls import path, include

from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import UserViewSet


router = SimpleRouter()

# auth_patterns = [
#     path('users/', user_view),
# ]

# auth_patterns = [
#     # path('signup/', email),
#     path('token/login/', token),    # To get TOKEN
# ]

router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
    # path('', include(auth_patterns)),
    # path('auth/', include(auth_patterns)),
]
