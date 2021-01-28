from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'Home/index.html')

def about(request):
    return render(request, 'Home/about.html')

def AISEC(request):
    return render(request, 'Home/AISEC.html')

def cit(request):
    return render(request, 'Home/cit.html')

def contact(request):
    return render(request, 'Home/contact.html')

def gallery(request):
    return render(request, 'Home/gallery.html')

def indtrip(request):
    return render(request, 'Home/indtrip.html')

def ITM(request):
    return render(request, 'Home/ITM.html')

def registration(request):
    return render(request, 'Home/registration.html')

def sponsors(request):
    return render(request, 'Home/sponsors.html')

def teachers(request):
    return render(request, 'Home/teachers.html')
   
