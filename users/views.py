from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from users.serializers import UserSerializer, PaymentsSerializer, UserPayment
from users.models import User, Payments
# Create your views here.


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ('date',)
    filterset_fields = ('course', 'lesson', 'payment_method',)


class UserCreateAPI(CreateAPIView):
    serializer_class = UserSerializer


class UserListAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPI(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserPayment


class UserUpdateAPI(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyAPI(DestroyAPIView):
    queryset = User.objects.all()
