from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import gamesCollection, userCollection, reviewsCollection
# Create your views here.

def index(request, gameName):
    if request.method == 'POST':
        #create the view for the game:
        #print("request: ", request.body)
        #from stack overflow: https://stackoverflow.com/questions/29780060/trying-to-parse-request-body-from-post-in-django
        dataDecode = request.body.decode('utf-8')
        dataJsonify = json.loads(dataDecode)
        print("data: ", dataJsonify)
        print("name: ", dataJsonify.get('gameName', None))
        #getting all user reviews:
    
    
    items = list(reviewsCollection.find({'gameName':gameName})) #mapped to comments then returned during render    
    selectedGame = gamesCollection.find_one({"gameName":gameName})
    selectedGameData = selectedGame
    print("selectedGame: ", selectedGameData["gameName"])
    return render(request, 'review.html', {'gameName': selectedGameData["gameName"], 'gameImageUrl':selectedGameData["gameImageUrl"], 'avgGameRating': selectedGameData["avgGameRating"], 'comments': items, 'currUser':request.session.get("sessionUsername", False),'gameOwner':selectedGameData["owner"],})
