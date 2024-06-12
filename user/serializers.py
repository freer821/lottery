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
    customer_no = serializers.CharField(required=False, allow_blank=True)
    company_extra = serializers.CharField(required=False, allow_blank=True)
    addr_extra = serializers.CharField(required=False, allow_blank=True)
    fax = serializers.CharField(required=False, allow_blank=True)
    website = serializers.CharField(required=False, allow_blank=True)
    bank = serializers.CharField(required=False, allow_blank=True)
    iban = serializers.CharField(required=False, allow_blank=True)
    bic = serializers.CharField(required=False, allow_blank=True)
    is_won = serializers.BooleanField(required=False)

    class Meta:
        model = Customer
        fields = '__all__'
        extra_kwargs = {
            'type': {'required': True},
            'customer_no': {'required': False},
            'company': {'required': True},
            'sex': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'company_extra': {'required': False},
            'addr': {'required': True},
            'addr_extra': {'required': False},
            'postcode': {'required': True},
            'city': {'required': True},
            'country': {'required': True},
            'tel': {'required': True},
            'fax': {'required': False},
            'email': {'required': True},
            'bill_email': {'required': True},
            'website': {'required': False},
            'tax_id': {'required': True},
            'ust_id': {'required': True},
            'bank': {'required': False},
            'iban': {'required': False},
            'bic': {'required': False},
            'is_won': {'required': False}
        }

    def create(self, validated_data):
        if validated_data.get('customer_no') is None:
            validated_data['customer_no'] = 'KN'+getRandomNo(7)

        return Customer.objects.create(**validated_data)
