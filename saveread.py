import pymongo as pm
from bson.json_util import dumps
import time
import urllib.parse as up

def init():
    un = up.quote_plus('root')
    pa = up.quote_plus('example')
    client = pm.MongoClient("mongodb://%s:%s@172.17.0.2:27017" % (un, pa))
    db = client["electro"]
    col = db["primary"]
    return col

def parse(data):
    try:
        return json.loads(data.decode("utf-8"))
    except:
        return 0

def save(body):
    col = init()
    data = parse(body)
    data["dt"] = int(time.time())
    x = col.insert_one(data)
    return x.inserted_id

def read():
    col = init()
    return str(col.find_one())

def readspec(body):
    col = init()
    data = parse(body)
    return str(col.find_one(data))

def readall():
    col = init()
    return dumps(list(col.find()))

def count():
    col = init()
    return col.count_documents({})
