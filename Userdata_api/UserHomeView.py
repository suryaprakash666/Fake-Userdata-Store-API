from django.shortcuts import render


def userhomeview(request):
    return render(request, 'UserHome.html')
