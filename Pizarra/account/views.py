from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as auth_login
from .models import User
# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        if email and password:
            user = authenticate(request, email = email, password = password)
            
            if user is not None:
                auth_login(request, user)
                
                return redirect('/')
    
    return render(request, 'account/login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2'] 

        if name and email and password1 and password2:
            user = User.objects.create_user(name,email,password1)
            
            return redirect('/login/')
        else: 
            print("error")
    
    return render(request, 'account/signup.html')