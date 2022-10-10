from rest_framework import viewsets

from users.models import Ingredient
from api.serializers.ingredients import IngredientSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]
#
#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         eml = request.data.get('email')
#         username = request.data.get('username')
#
#         if username in RESTRICTED_USERNAMES:
#             return Response(
#                 {
#                     'username':
#                         f'Wrong username. Username - {username} is restricted'},
#                 status=status.HTTP_400_BAD_REQUEST)
#
#         if User.objects.filter(username=username).exists():
#             return Response(
#                 {
#                     'username':
#                         f'Wrong username. Such user - {username}  - is already used'
#                 },
#                 status=status.HTTP_400_BAD_REQUEST)
#
#         if User.objects.filter(email=eml).exists():
#             return Response(
#                 {
#                     'email':
#                         f'Wrong email. Such email - {eml}  - is already used'
#                 },
#                 status=status.HTTP_400_BAD_REQUEST)
#
#         user = User.objects.create(**serializer.validated_data)
#         user.set_password(serializer.validated_data['password'])
#         user.save()
#
#         queryset = User.objects.all()
#         saved_user = get_object_or_404(queryset, email=eml)
#         serializer_ans = UserSerializerAnswer(saved_user)
#
#         return Response(serializer_ans.data, status=status.HTTP_201_CREATED)
#
