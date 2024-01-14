from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from Userdata_api.UserdataModel import Userdatamodel
from Userdata_api.dataserializer import Userdataserializer


# Create your views here.
class Dataviewset(viewsets.ModelViewSet):
    queryset = Userdatamodel.objects.all()
    serializer_class = Userdataserializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]



