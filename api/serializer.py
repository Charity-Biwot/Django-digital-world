from dataclasses import field
# from pyexpat import model
from rest_framework import serializers
from wallet .models import Customer

class Customerserializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        field= ("first_name","email","age")