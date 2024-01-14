from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from Userdata_api.UserdataModel import Userdatamodel


@permission_classes([IsAuthenticated])
def datasubmission(request):
    if request.method == 'POST':
        username = request.POST.get('Name')
        email = request.POST.get('Email')
        password = request.POST.get('Password')

        user = Userdatamodel(username=username, email=email)
        user.set_password(password)
        user.save()
        return HttpResponseRedirect('/Userhome/')

    elif request.method == 'GET':
        return render(request, 'UserRegistrationPage.html')
