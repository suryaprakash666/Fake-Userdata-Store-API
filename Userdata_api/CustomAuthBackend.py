# backends.py
from django.contrib.auth.backends import ModelBackend
from Userdata_api.UserdataModel import Userdatamodel


class MyCustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Userdatamodel.objects.get(username=username)
        except Userdatamodel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
