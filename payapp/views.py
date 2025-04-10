from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Transaction, UserProfile

@login_required
def make_payment_view(request):
    if request.method == 'POST':
        recipient_username = request.POST.get('recipient')
        try:
            amount = float(request.POST.get('amount'))
        except ValueError:
            messages.error(request, "Invalid amount.")
            return redirect('make_payment')

        # Optional fields
        currency = request.POST.get('currency', 'GBP')  # Default to GBP if not specified
        note = request.POST.get('note', '')

        if amount <= 0:
            messages.error(request, "Amount must be greater than zero.")
            return redirect('make_payment')

        try:
            recipient_user = User.objects.get(username=recipient_username)
        except User.DoesNotExist:
            messages.error(request, "Recipient does not exist.")
            return redirect('make_payment')

        # Handle the case where UserProfile might not exist
        try:
            sender_profile = UserProfile.objects.get(user=request.user)
            recipient_profile = UserProfile.objects.get(user=recipient_user)
        except UserProfile.DoesNotExist:
            messages.error(request, "Profile not found.")
            return redirect('make_payment')

        # Check if sender has enough balance
        if sender_profile.balance < amount:
            messages.error(request, "Insufficient balance.")
            return redirect('make_payment')

        # Update balances
        sender_profile.balance -= amount
        recipient_profile.balance += amount
        sender_profile.save()
        recipient_profile.save()

        # Save transaction
        Transaction.objects.create(
            sender=request.user,
            receiver=recipient_user.username,
            amount=amount,
            note=note
        )

        messages.success(request, f"£{amount} sent to {recipient_user.username} successfully!")
        return redirect('home')

    return render(request, 'payapp/makepayment.html')



def request_money_view(request):
    if request.method == 'POST':
        sender = request.POST.get('sender')
        amount = request.POST.get('amount')
        currency = request.POST.get('currency')
        note = request.POST.get('note')

        # Logic to handle the money request (e.g., save to the database or notify the sender)
        messages.success(request, f"Requested £{amount} from {sender} successfully!")

        return redirect('home')  # Redirect back to home page after successful request

    return render(request, 'payapp/request_money.html')


def transaction_history_view(request):
    transactions = Transaction.objects.filter(sender=request.user).order_by('-date_time')
    return render(request, 'payapp/transaction_history.html', {'transactions': transactions})


def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:  # Check if user is an admin
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'register/admin_login.html', {'error': 'Invalid credentials or not an admin.'})

    return render(request, 'register/admin_login.html')


@login_required
@user_passes_test(lambda u: u.is_staff)  # Only staff (admin) users can access
def admin_dashboard_view(request):
    users = User.objects.all()
    transactions = Transaction.objects.all().order_by('-date_time')

    return render(request, 'register/admin_dashboard.html', {
        'users': users,
        'transactions': transactions
    })


def payapp(request):
    return render(request, 'payapp/index.html')
