import pymongo
from connectionUrl import URLs

client = pymongo.MongoClient(URLs.mongoURL)

db = client['gamereview']
dbUser = client['user']
dbReviews = client['reviews']