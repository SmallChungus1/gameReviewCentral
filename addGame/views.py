from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.http import HttpResponse
import json
from .models import gamesCollection, userCollection, reviewsCollection

def index(request):
    return render(request, 'addGame.html')

def addGameProcessing(request):
    gamename = request.POST["addGameName"]
    gameImageUrl = request.POST["addGameUrl"]
    gameData ={
        'gameName':gamename,
        'avgGameRating':"No Reviews Yet",
        'gameImageUrl':gameImageUrl,
        'owner':request.session.get("sessionUsername", False)
    }
    gamesCollection.insert_one(gameData)
    return redirect ("/")