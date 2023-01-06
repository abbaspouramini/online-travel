from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Passenger
from .serializer import PassengerSerializer
#create new passenger and get all passenger
class PassengerList(APIView):
    def get(self,request):
        passengers = Passenger.objects.filter(user=request.user)
        serializer = PassengerSerializer(passengers,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PassengerSerializer(data=request.data)
        user = request.user
        if serializer.is_valid():
            serializer.validated_data["user"] = user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#get, update and delete a passenger
class PassengerDetail(APIView):
    def get_object(self, pk):
        try:
            return Passenger.objects.get(pk=pk)
        except Passenger.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        passenger = self.get_object(pk)
        serializer = PassengerSerializer(passenger)
        return Response(serializer.data)

    def put(self,request,pk):
        passenger = self.get_object(pk)
        serializer = PassengerSerializer(passenger,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        passenger = self.get_object(pk)
        serializer = PassengerSerializer(passenger)
        passenger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        