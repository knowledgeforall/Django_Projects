from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here
def home(request):
    return render(request, 'accounts/home.html')


def login(request):
    if(request.method == 'POST'):
        #see if it's an actual user
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if User is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', { 'error' : 'Incorrect username or password'})
    else:
        return render(request, 'accounts/login.html')







def signup(request):
    #TODO: Need to redirect to homepage, and log out
    if(request.method == 'POST'):
        if(request.POST['password'] == request.POST['verifyPassword']):
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username not available'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
             return render(request, 'accounts/signup.html', {'error': 'Mismatch passwords'})
    else:
        return render(request, 'accounts/signup.html')





def logout(request):
    #TODO: can also reroute user to Home page
    #after you LOG THEM OUT
    return render(request, 'accounts/logout.html')

