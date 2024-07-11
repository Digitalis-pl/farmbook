from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from payments.models import Payments
from payments.serializers import PaymentsSerializer


# Create your views here.


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ('date',)
    filterset_fields = ('course', 'lesson', 'payment_method',)
