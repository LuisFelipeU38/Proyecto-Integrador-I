from django.shortcuts import render
from django.http import HttpResponse
#from .models import talentos
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')