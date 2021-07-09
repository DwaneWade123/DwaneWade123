from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics

class TicketListView(generics.ListAPIView):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

