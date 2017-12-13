import pymongo
client=pymongo.MongoClient('172.28.171.13',27017)
database=client['QNQ']
print(database.collection_names())
coll1=database['qnq_sn']
coll1.remove()
print(database.collection_names())