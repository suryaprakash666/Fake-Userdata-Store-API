from rest_framework import serializers
from .Userdatamodel import Userdatamodel


class Userdataserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Userdatamodel
        fields = "__all__"

