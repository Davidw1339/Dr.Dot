from flask import Flask
from pymongo import MongoClient
import os

#initialize the app
app = Flask(__name__)

#connect to db
db_url = os.environ.get("MONGODB_URI")
if db_url == None:
    secret_reader = open("./secret_key.txt", 'r');
    db_url = secret_reader.read().strip()
    print db_url
client = MongoClient(db_url)
db = client.drdot

#declare route
@app.route("/")
def hello():
    return "Welcome to Dr. Dot an integrative suite of features for health and wellness!"

if __name__ == "__main__":
    app.run(debug=True)
