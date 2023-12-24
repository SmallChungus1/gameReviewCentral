from django.shortcuts import render
from django.http import HttpResponse
import json
#from .models import gamesCollection
# Create your views here.

def index(request):
    
    return render(request, 'login.html')
