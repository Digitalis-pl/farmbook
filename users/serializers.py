from rest_framework.serializers import ModelSerializer, SerializerMethodField

from users.models import User, Payments


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PaymentsSerializer(ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'


class UserPayment(ModelSerializer):
    payment_in_course = SerializerMethodField()

    def get_payment_in_course(self, user):
        return Payments.objects.filter(user=user.pk).values()

    class Meta:
        model = User
        fields = ('email', 'city', 'payment_in_course')
