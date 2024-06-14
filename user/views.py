from django.utils import timezone

import django_filters
from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, action, authentication_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from common.middleware import getStandardResponse
from user.models import Customer
from user.serializers import CustomerSerializer


@api_view(['POST'])
@authentication_classes([])  # No authentication for this view
def register(request):
    data = JSONParser().parse(request)
    serializer = CustomerSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(getStandardResponse(200))

    return Response(getStandardResponse(500, serializer.errors))


@api_view(['POST'])
@authentication_classes([])  # No authentication for this view
def login(request):
    username = request.data.get("username", "")
    password = request.data.get("password", "")

    user = authenticate(username=username, password=password)
    if not user:
        return Response(getStandardResponse(400, 'username or password wrong!'))

    token, _ = Token.objects.get_or_create(user=user)
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])

    return Response(getStandardResponse(200, '', {'token': token.key}))


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('-createdtime')
    serializer_class = CustomerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['is_won']

    @action(detail=True, methods=['get'])
    def won(self, request, pk=None):
        instance = self.get_object()
        instance.is_won = True
        instance.save()
        customers = Customer.objects.filter(is_won=False).all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(getStandardResponse(200, data=serializer.data))
