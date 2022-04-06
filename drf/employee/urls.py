from django.urls import path
from .api import EmployeeCreateApi

urlpatterns = [
    path('api/create', EmployeeCreateApi.as_view()),
]