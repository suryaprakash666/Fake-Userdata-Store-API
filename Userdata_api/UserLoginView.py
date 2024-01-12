from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('Name')
        password = request.POST.get('Password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Userhomeview')
        else:
            return render(request, 'UserLoginPage.html', {'error': 'Invalid credentials'})

    elif request.method == 'GET':
        return render(request, 'UserLoginPage.html')
