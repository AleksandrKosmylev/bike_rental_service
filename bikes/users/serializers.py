from django.contrib.auth.models import AbstractUser
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    bikes = serializers.HyperlinkedRelatedField(many=True, view_name='bike-detail', read_only=True)

    class Meta:
        model = AbstractUser
        fields = ['url', 'id', 'username', 'snippets']