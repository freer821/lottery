from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('register', register),
    path('login', login),

    path('', include(router.urls))
]