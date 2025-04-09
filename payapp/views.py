from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def payapp(request):
    return render(request, 'payapp/payapp.html')

def make_payment_view(request):
    if request.method == 'POST':
        recipient = request.POST.get('recipient')
        amount = request.POST.get('amount')
        currency = request.POST.get('currency')
        note = request.POST.get('note')

        # Payment logic can go here (e.g. save to DB, validation, etc.)
        messages.success(request, f"£{amount} sent to {recipient} successfully!")

        return redirect('home')

    return render(request, 'makepayment.html')

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

