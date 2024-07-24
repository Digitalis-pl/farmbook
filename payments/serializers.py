from rest_framework import serializers

from rest_framework.serializers import ModelSerializer

from payments.models import Payments

from payments.services import check_sessions


class PaymentsSerializer(ModelSerializer):
    session_params = serializers.SerializerMethodField()

    def get_session_params(self, obj):
        return check_sessions(obj.session_id)

    class Meta:
        model = Payments
        fields = '__all__'


#class PaymentsDetailSerializer(ModelSerializer):
#    session_params = serializers.SerializerMethodField()
#
#    def get_session_params(self, payment):
#        return check_sessions(payment.session_id)
#
#    class Meta:
#        model = Payments
#        fields = ('id', 'session_id', 'date', 'payments_summ', 'payment_method', 'link', 'user', 'course', 'lesson', 'session_params')
