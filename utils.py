import pymongo

url='mongodb+srv://123:123@cluster0.nuvlq6v.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(url)

db = client['gamereview']
dbUser = client['user']
dbReviews = client['reviews']