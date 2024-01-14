from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from Userdata_api.models import Userdatamodel


@permission_classes([IsAuthenticated])
def datasubmission(request):
    if request.method == 'POST':
        Username = request.POST.get('Name')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')

        Userdatamodel.objects.create(username=Username, email=Email, password=Password)

        return HttpResponseRedirect('/Userhomeview/')

    elif request.method == 'GET':
        return render(request, 'UserRegistrationPage.html')
