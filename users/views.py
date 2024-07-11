from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from users.serializers import UserSerializer, UserForGuestSerializer
from users.permissions import IsThatMe
from users.models import User
# Create your views here.


class UserCreateAPI(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserForGuestSerializer


class UserRetrieveAPI(RetrieveAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        current_user = self.request.user
        if self.get_object().pk == current_user.pk:
            return UserSerializer
        return UserForGuestSerializer


class UserUpdateAPI(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsThatMe)


class UserDestroyAPI(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsThatMe)
