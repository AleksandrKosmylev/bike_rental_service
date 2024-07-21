from bikes.rental.models import Bikes
from bikes.rental.serializers import BikesSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class BikesList(APIView):
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
