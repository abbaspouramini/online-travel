import datetime
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Trip, Station, Ticket
from passenger.models import Passenger
from .serializer import TripSerializer,TicketSerializer

class TripList(APIView):
    def post(self,request):
        sttime = request.data["start_time_date"].split("-")
        trips = Trip.objects.filter(start_station = Station.objects.get(name=request.data["start_station"]),
                                    end_station = Station.objects.get(name=request.data["end_station"]),
                                    start_time_date__date = datetime.date(int(sttime[0]),int(sttime[1]),int(sttime[2])))
        serializer = TripSerializer(trips,many=True)
        return Response({"trips":serializer.data})

class TripCreate(APIView):
    def post(self,request):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            mtrip=Trip.objects.get(id=serializer.data["id"])
            for i in range(1,mtrip.train.total_capacity+1):
                ticketins = Ticket(trip_id=mtrip.id,seat_number=i, number=str(mtrip.id)+str(i))
                ticketins.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TripBook(APIView):
    def post(self,request):
        if not Ticket.objects.filter(trip_id = request.data["trip_id"], passenger_id = request.data["passenger_id"]):
            tickets=Ticket.objects.filter(trip_id=request.data["trip_id"],passenger=None)
            myticket = tickets.first()
            myticket.passenger_id = request.data["passenger_id"]
            myticket.user = request.user
            myticket.save(update_fields=["passenger","user"])
            serializer = TicketSerializer(myticket)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({"message":"is exist"},status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if Ticket.objects.filter(number=request.data["ticket_id"],user=request.user):
            myticket = Ticket.objects.get(number=request.data["ticket_id"])
            data = myticket.delete()
            return Response(data,status=status.HTTP_200_OK)
        return Response({"message": "is not exist"}, status=status.HTTP_400_BAD_REQUEST)

class TravelsList(APIView):
    def get(self,request):
        tickets = Ticket.objects.filter(user=request.user)
        serializer = TicketSerializer(tickets, many=True)
        return Response({"tickets":serializer.data})


class TripDetail(APIView):
    def get_object(self, pk):
        try:
            return Trip.objects.get(pk=pk)
        except Trip.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        trip = self.get_object(pk)
        serializer = TripSerializer(trip)
        return Response(serializer.data)