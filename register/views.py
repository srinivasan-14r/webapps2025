from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Transaction

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


def transfer_money(request):
    if request.method == 'POST':
        recipient_username = request.POST.get('recipient')
        amount = float(request.POST.get('amount'))

        # Other fields
        currency = request.POST.get('currency')
        note = request.POST.get('note')

        try:
            recipient_user = User.objects.get(username=recipient_username)
        except User.DoesNotExist:
            messages.error(request, "Recipient does not exist.")
            return redirect('transfer_money')

        sender_profile = UserProfile.objects.get(user=request.user)
        recipient_profile = UserProfile.objects.get(user=recipient_user)

        # Check if sender has enough balance
        if sender_profile.balance < amount:
            messages.error(request, "Insufficient balance.")
            return redirect('transfer_money')

        # Update balances
        sender_profile.balance -= amount
        recipient_profile.balance += amount
        sender_profile.save()
        recipient_profile.save()

        # Save transaction
        Transaction.objects.create(
            sender=request.user,
            receiver=recipient_user.username,
            amount=amount
        )

        messages.success(request, f"£{amount} sent to {recipient_user.username} successfully!")
        return redirect('home')

    return render(request, 'register/transfer.html')