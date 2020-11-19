import json
from pymongo import MongoClient

client = MongoClient('mongodb://kandalf123:db7575@3.34.181.37', 27017)
db = client.STGpoke

data = {}
with open("../data/gamemaster.json", "r", encoding='utf-8') as f:
    data = json.load(f)
# print(data)
if isinstance(data, list):
    db.gamemaster.insert_many(data)
    print(data)
else:
    db.gamemaster.insert_one(data)