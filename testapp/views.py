from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

# Create your views here.


class EmployeeModelViewSetCBV(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]
