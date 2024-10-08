from bikes.rental.models import Bikes
from bikes.rental.serializers import BikesSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.views import View
from django.http import HttpResponse
"""
from django.contrib.auth.models import User
from rest_framework import generics
from bikes.rental.serializers import UserSerializer



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
"""



class Home(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Bikes, World!")




class BikesList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    """
    List all bikes
    """
    def get(self, request, format=None):
        bikes = Bikes.objects.all()
        serializer = BikesSerializer(bikes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
