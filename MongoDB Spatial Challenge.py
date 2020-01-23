import pymongo
from pymongo import MongoClient 


# connect to database
connection = MongoClient('localhost', 27017)

db = connection.master

list_place = list(db.restaurants.find({},{"_id":1}))
                
list_neigh = list(db.neighborhoods.find())

list_in_id = []
list_not_in_id = [] 

def solution():
    for i in list_neigh:
        data = list(db.restaurants.find(
        { "location": { "$geoWithin":{ "$geometry": i["geometry"]}}},{"_id":1}))
        for x in data:
            list_in_id.append(x)
    for item in list_place:
        if item not in list_in_id:
            list_not_in_id.append(item)
    print(list_not_in_id)
    print(len(list_not_in_id))
    
solution()

