from rest_framework import serializers
from .models import Bikes
# from django.contrib.auth.models import User


class BikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bikes
        fields = ['id', 'bike_name', 'description',
                  'quantity']
