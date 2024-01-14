from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                # Redirect to a success page or the user's intended destination
                return render(request, 'UserHome.html')  # Replace with your desired redirect
            else:
                # Incorrect credentials
                return render(request, 'UserLoginPage.html', {'error': 'Invalid username or password'})
    else:
        form = AuthenticationForm()
    return render(request, 'UserLoginPage.html', {'form': form})
