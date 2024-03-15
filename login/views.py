from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def main(request):
    return render(request, 'main.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect("main")
        
        else:
            messages.info(request,'invalid credentials')
            return redirect("/")
                
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username =request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username taken')
            return redirect('signup')
            
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email taken')
            return redirect('signup')
            
        else:
            user= User.objects.create_user(username=username, email=email, password=password)
            user.save()
            print('new user created')
            return redirect('/')
        
    else:
        return render(request, 'signup.html')