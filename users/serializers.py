from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField

from users.models import User
from payments.models import Payments
from payments.serializers import PaymentsSerializer


class UserSerializer(ModelSerializer):
    payment_in_course = SerializerMethodField()
    full_name = CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'full_name', 'email', 'password', 'city', 'payment_in_course',)

    def get_payment_in_course(self, user):
        return Payments.objects.filter(user=user.pk).values()


class UserForGuestSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'email', 'city')
