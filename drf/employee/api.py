from rest_framework import generics
from rest_framework.response import Response
from .serializer import EmployeeSerializer
from .models import Employee

class EmployeeCreateApi(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer