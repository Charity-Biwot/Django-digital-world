from distutils.sysconfig import customize_compiler
# from msilib.schema import Class
from django.shortcuts import render
from rest_framework import viewsets
from wallet .models import Customer
from .serializer import Customerserializer

# Create your views here.
class Customerviewset (viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = Customerserializer

