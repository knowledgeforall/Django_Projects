
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def home(request):
    return render(request, 'Join_Us_e.html')
def login(request):
    if(request.method == 'POST'):
         user = auth.authenticate(username=request.POST['username'],
password=request.POST['password'])
    if User is not None:
        auth.login(request, user)
        return redirect('home')       
    else:
        return render(request, 'Join_Us_e.html', { 'error' : 'Incorrect username or password'})    
    else:        return render(request, 'Join_Us_e.html')

def signup(request):
    if(request.method == 'POST'):
        if(request.POST['password'] == request.POST['verifyPassword']):            
            try:
                user = User.objects.get(username=request.POST['username'])                
                return render(request, 'Join_Us_e.html', {'error': 'Username not available'})
            except User.DoesNotExist:
                 user = User.objects.create_user(request.POST['username'], password = request.POST['password'])                
                 auth.login(request, user)                
                 return redirect('home')
        else:
            return render(request, 'Join_Us_e.html', {'error': 'Mismatch passwords'})
    else:       
        return render(request, 'Join_Us_e.html')

def logout(request):
    return render(request, 'accounts/logout.html')

#in html {% csrf_token %}