from rest_framework import serializers
from Userdata_api.models import Userdatamodel


class Userdataserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Userdatamodel
        fields = "__all__"

