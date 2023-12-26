from django.shortcuts import render
from rest_framework import viewsets
from Userdata_api.models import Userdatamodel
from Userdata_api.dataserializer import Userdataserializer


# Create your views here.
class Dataviewset(viewsets.ModelViewSet):
    queryset = Userdatamodel.objects.all()
    serializer_class = Userdataserializer
