# from django.contrib.auth.models import User
from bikes.users.models import CustomUser
from rest_framework import generics
from bikes.users.serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer