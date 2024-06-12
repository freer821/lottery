import string
import random

from rest_framework import serializers

from user.models import Customer


def getRandomNo(keylength=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=keylength))


class CustomerSerializer(serializers.ModelSerializer):
    createdtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    updatedtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    contact = serializers.JSONField(required=False)
    is_won = serializers.BooleanField(required=False)

    class Meta:
        model = Customer
        fields = '__all__'
        extra_kwargs = {
            'company': {'required': True},
            'sex': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'country': {'required': True},
            'tel': {'required': True},
            'email': {'required': True},
            'is_won': {'required': False}
        }

    def create(self, validated_data):
        if validated_data.get('customer_no') is None:
            validated_data['customer_no'] = 'KN'+getRandomNo(7)

        return Customer.objects.create(**validated_data)
