import pymongo
import certifi


conn = "mongodb+srv://user0:<password>@cluster0.lpjwx46.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(conn, tlsCAFile=certifi.where())
db = client.word
db.abc.insert_ond({"abc": 1})
print(db.abc.find_one({"abc": 1}))