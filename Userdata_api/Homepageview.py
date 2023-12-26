from django.shortcuts import render


def homepageview(request):
    return render(request, 'Homepage.html')
