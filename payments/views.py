import json

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
from payments.services import convert_rub_to_usd, create_price, create_session, create_product, check_sessions
from users.permissions import IsOwner

from payments.models import Subscription


# Create your views here.


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ('date',)
    filterset_fields = ('course', 'lesson', 'payment_method',)

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        amount = 0
        products = payment.course.values()
        prod_data = {}
        for index, prod in enumerate(products):
            prod_data['product' + str(index)] = json.dumps({'id': prod['id'], 'name': prod['name'], 'price': prod['price']})
            # prod_data['product' + str(index)] = prod['name']
            # prod_data['product' + str(index)] = prod['id']
            amount += prod['price']
        # amount_in_usd = convert_rub_to_usd(amount)
        product = create_product('payment', prod_data)
        print(product)
        price = create_price(amount, product)
        session_id, payment_link = create_session(len(prod_data), price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return PaymentsDetailSerializer
    #     return PaymentsSerializer


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
            return Response(
                {"message": message, "user": user.pk, "course": course_item.name, "course_id": course_item.pk})
