from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView

from users.serializers import UserSerializer
from users.models import User
# Create your views here.


class UserCreateAPI(CreateAPIView):
    serializer_class = UserSerializer


class UserListAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPI(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPI(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyAPI(DestroyAPIView):
    queryset = User.objects.all()
