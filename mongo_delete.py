import pymongo
import csv
client=pymongo.MongoClient('172.28.171.13',27017)
database=client['BDBK']
print(database.collection_names())
coll1=database['bdbk_shengfen']
# coll1.remove()
# print(database.collection_names())
headline=[]
with open('省份.csv','r') as readfile:
    csv_reader=csv.reader(readfile)
    for line in csv_reader:
        if csv_reader.line_num == 1:
            headline=line
            continue
        insert_it = {}
        for i in range(len(line)):
            insert_it[headline[i]]=line[i]
        coll1.insert(insert_it)