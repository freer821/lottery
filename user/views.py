import django_filters
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from common.middleware import getStandardResponse
from user.models import Customer
from user.serializers import CustomerSerializer


@api_view(['POST'])
def register(request):
    data = JSONParser().parse(request)
    serializer = CustomerSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(getStandardResponse(200))

    return Response(getStandardResponse(500, serializer.errors))


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('-createdtime')
    serializer_class = CustomerSerializer
    authentication_classes = (BasicAuthentication,)
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
