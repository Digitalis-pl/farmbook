from django.shortcuts import render, get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from materials.models import Course
from payments.models import Payments
from payments.serializers import PaymentsSerializer
from users.permissions import IsOwner

from payments.models import Subscription


# Create your views here.


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ('date',)
    filterset_fields = ('course', 'lesson', 'payment_method',)


class SubscriptionController(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data["course_id"]
        course_item = get_object_or_404(Course, pk=course_id)
        sub_item = Subscription.objects.filter(user=user, course=course_id)
        if sub_item.exists():
            sub_item.delete()
            message = 'подписка удалена'
            return Response({"message": message})
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'test'
            return Response({"message": message, "user": user.pk, "course": course_item.name, "course_id": course_item.pk})
