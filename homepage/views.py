from django.shortcuts import render
from django.http import HttpResponse
from .models import gamesCollection
import pymongo

# Create your views here.
def index(request):
    itemsNumerical = list(gamesCollection.find({"avgGameRating":{"$type": 1}}).sort('avgGameRating', pymongo.DESCENDING))
    itemsString = list(gamesCollection.find({"avgGameRating":{"$type": 2}}).sort('avgGameRating', pymongo.DESCENDING))
    items = itemsNumerical+itemsString
    itemsNoReview = list(gamesCollection.find({"avgGameRating":"No Reviews Yet"}))
    if(request.session.get("sessionUsername", False)):
        jsonItems = {
            'items': items,
            'itemsNoReview':itemsNoReview,
            'sessionUsername':request.session.get("sessionUsername", False),
    }
        return render(request, 'index.html', jsonItems)
    else:
        jsonItems = {
            'items': items,
            'itemsNoReview':itemsNoReview,
            'sessionUsername':'Not Logged In',
    }
        return render(request, 'index.html', jsonItems)

def searchGame(request):
    items = list(gamesCollection.find({'gameName':request.POST.get("gameSearchName", False)}))
    if(items):

        jsonItems = {
                'items': items,
                'sessionUsername':request.session.get("sessionUsername", False),
        }
        return render(request, 'gameSearch.html', jsonItems)
    else:
        return render(request, 'gameNotFound.html')
   
