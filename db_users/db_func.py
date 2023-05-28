import pymongo
from pymongo.mongo_client import MongoClient
import json

uri = "mongodb+srv://solomon_conn:z7aMb7aSr050eofZ@saiqe.kbpagkn.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(host=uri)
db = client.saiqe
users_coll = db.users

index_json = open("/home/tscrt/Desktop/saiqe/db_users/index.json", "r")

def on_add(name, email, passw, ip, xf):
    users_coll.insert_one({"_id": index_json['index'], "name": str(name), "email": str(email), "passw": str(passw), "ip_addresses": [ip, ], "XFingerprint": str(xf)})

def on_check(name, email):
    if name == users_coll.name:
        return "Это имя уже занято"
    if email == users_coll.email:
        return "Аккаунт с такой почтой уже есть"
    