from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page on success
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'register/login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # This saves to the default User model and default DB
            return redirect('login')  # Redirect to login after registration
    else:
        form = UserCreationForm()
    return render(request, 'register/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    return render(request, 'home.html')
