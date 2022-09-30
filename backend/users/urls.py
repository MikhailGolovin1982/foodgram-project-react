from django.urls import path, include

from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import user_view


auth_patterns = [
    path('users/', user_view),
]

# auth_patterns = [
#     # path('signup/', email),
#     path('token/login/', token),    # To get TOKEN
# ]

urlpatterns = [
    path('', include(auth_patterns)),
    # path('auth/', include(auth_patterns)),
]
