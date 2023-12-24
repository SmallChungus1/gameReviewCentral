from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
import json
from .models import gamesCollection, userCollection, reviewsCollection      
# Create your views here.

def addComment(request):
 
    if request.method == 'POST':
        reviewerName = request.POST['reviewerName']
        reviewerRating = request.POST['ratingVal']
        reviewerComment = request.POST['reviewerComment']
        gameName = request.POST['gameName']
        dataJsonify = {
            'gameName':gameName,
            'username':reviewerName,
            'rating':reviewerRating,
            'comment':reviewerComment,
        }
        reviewsCollection.insert_one(dataJsonify)

        avgRating = calcRating(dataJsonify)
        if avgRating is not False:
           
            gamesCollection.update_one({'gameName':gameName},{'$set':{'avgGameRating':avgRating}})
        else:
            print("Error: Could not calculate average rating")
    return redirect(reverse('viewreview', args=[gameName]))

def delUserComment(request):
    userName = request.POST['delComment']
    userComment = request.POST['userComment']
    gameName = request.POST['gameName']
    userRating = request.POST["userRating"]
    reviewsCollection.delete_one({'username':userName, 'comment':userComment, 'rating':userRating})

    #we need to build a json variable as it is an argument in calcRating function
    dataJsonify = {
            'gameName':gameName,
            'username':userName,
            'rating':userRating,
            'comment':userComment,
    }

    avgRating = calcRating(dataJsonify)
    if avgRating is not False:
           
        gamesCollection.update_one({'gameName':gameName},{'$set':{'avgGameRating':avgRating}})
    else:
        print("Error: Could not calculate average rating")
    
    return redirect(reverse('viewreview', args=[gameName]))
def calcRating(dataJsonify):
    passedInName = dataJsonify['gameName']
    passedInRating = dataJsonify['rating']
    reviewsForThisGame = reviewsCollection.find({'gameName':passedInName})
    ratingsSum = 0
    avgRating = 0
    numOfRatings = 0
    if not reviewsForThisGame:
        return False
    else:
        for aReview in reviewsForThisGame:
            if(aReview.get("rating") is "No Reviews Yet"):
                return aReview
            ratingsSum += int(aReview.get("rating"))
            numOfRatings += 1
        if numOfRatings == 0:
            return "No Reviews Yet"
        else:
            avgRating = float(ratingsSum/numOfRatings)
            return round(avgRating, 2)
