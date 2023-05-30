import pymongo
from pymongo.mongo_client import MongoClient
import json

uri = "mongodb+srv://solomon_conn:z7aMb7aSr050eofZ@saiqe.kbpagkn.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(host=uri)
db = client.saiqe
users_coll = db.users

with open("/home/tscrt/Desktop/saiqe/db_users/index.json", "r") as f:
    index_json = json.load(f)

def on_add(name, email, passw, ip, xf):
    users_coll.insert_one({"_id": index_json['index'], "name": str(name), "email": str(email), "passw": str(passw), "ip_addresses": [str(ip), ], "XFingerprint": str(xf)})
    index_json['index'] += 1

def on_check(name, email=None, passw=None, ip=None):
    if email is not None:
        if users_coll.find({"email": str(email)}):
            for x in users_coll.find({"email": str(email)}):
                if email in x:
                    return 0
                else:
                    pass
    if users_coll.find({"name": str(name)}):
        for x in users_coll.find({"name": str(name)}):
            if name in str(x):
                if passw is not None:
                    if passw in str(x):
                        if ip is not None:
                            if ip in x['ip_addresses']:
                                return 4
                            else:
                                return 3
                        else:
                            return 3
                    else:
                        return 1
                else:
                    return 1
                
            else:
                pass
    else:
        return 2

def on_email_find(name):

    for x in users_coll.find({"name": str(name)}):
        email = x['email']
        return email
    
def on_update(name, ip):

    for x in users_coll.find({"name": str(name)}):

        previous = {"name": str(name)}
        new = {"$push": {"ip_addresses": str(ip)}}

        users_coll.update_one(previous, new)