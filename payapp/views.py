from django.shortcuts import render

# Create your views here.
def payapp(request):
    return render(request, 'payapp/payapp.html')