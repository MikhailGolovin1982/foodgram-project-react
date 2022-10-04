from rest_framework import viewsets, status, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Ingredient, User
from .serializers import IngredientSerializer, UserSerializerAnswer, TokenSerializer

from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsAdmin, IsOwner
from .serializers import UserSerializer #, UserSerializerSimpleUser


RESTRICTED_USERNAMES = [
    'me',
]


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        eml = request.data.get('email')
        username = request.data.get('username')

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

        User.objects.create(**serializer.validated_data)

        queryset = User.objects.all()
        saved_user = get_object_or_404(queryset, email=eml)
        serializer_ans = UserSerializerAnswer(saved_user)

        return Response(serializer_ans.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    user = get_object_or_404(User, email=email)
    if user.password == serializer.data.get('password'):
        token = str(RefreshToken.for_user(user).access_token)
        return Response({"auth_token": token}, status=status.HTTP_201_CREATED)
    return Response({"auth_token": "Wrong user password"},
                    status=status.HTTP_400_BAD_REQUEST)
