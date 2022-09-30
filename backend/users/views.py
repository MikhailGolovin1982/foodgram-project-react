from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Ingredient, User
from .serializers import IngredientSerializer

from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsAdmin, IsOwner
from .serializers import UserSerializer, UserSerializerSimpleUser


RESTRICTED_USERNAMES = [
    'me',
]


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def user_view(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    eml = serializer.data.get('email')
    username = serializer.data.get('username')

    if username in RESTRICTED_USERNAMES:
        return Response(
            {
                'username':
                    f'Wrong username. Username - {username} is restricted'},
            status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response(
            {
                'username':
                    f'Wrong username. Such user - {username}  - is already used'
            },
            status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=eml).exists():
        return Response(
            {
                'email':
                    f'Wrong email. Such email - {eml}  - is already used'
            },
            status=status.HTTP_400_BAD_REQUEST)

    User.objects.create(
        email=eml,
        username=username,
        first_name=serializer.data.get('first_name'),
        last_name=serializer.data.get('last_name'),
        password=serializer.data.get('password')
    )

    # serializer.save()
    # answer_data = serializer.data.popitem('password')
    answer_data = serializer.data
    answer_data.popitem("password")
    answer_data["id"] = User.objects.filter(username=username)[0].id

    # return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(answer_data, status=status.HTTP_200_OK)


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def token(request):
#     serializer = ConfirmSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     username = serializer.data.get('username')
#     user = get_object_or_404(User, username=username)
#     if user.confirm == serializer.data.get('confirmation_code'):
#         token = str(RefreshToken.for_user(user).access_token)
#         return Response({'token': token}, status=status.HTTP_200_OK)
#     return Response({'confirmation_code': 'Wrong confirmation code'},
#                     status=status.HTTP_400_BAD_REQUEST)
