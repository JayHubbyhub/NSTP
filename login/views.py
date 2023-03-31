from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User
from .forms import UserForm

# Create your views here.

def add(request): # signup
    if request.method == "POST":
        userForm = UserForm(request.POST, request.FILES)
        if userForm.is_valid():
            new_user = userForm.save()
            return redirect("login:login")
    else:
        userForm = UserForm()
        return render(request, "add.html", 
            {"userForm": userForm})

def login(request): # sign in
    if request.method == "POST":
        id_num = request.POST.get('id_num')
        password = request.POST.get('password')
        try:
            user = User.objects.get(id_num=id_num)
            if password == user.password:
                return redirect("login:homepage")
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')

def homepage(request):
    return render(request, "homepage.html")
