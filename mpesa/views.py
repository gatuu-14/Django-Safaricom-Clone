from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , 'home.html')

def home(request):
    return render(request , 'base.html')

def payment(request):
    return render(request , 'payment.html')

def success(request):
    return render(request , 'success.html')

def index(request):
    return render(request , 'index.html')


def base(request):
    return render(request , 'base.html')