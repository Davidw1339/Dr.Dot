from flask import Flask, send_file
# from pymongo import MongoClient
import json
import os

#initialize the app
from app import app

# #connect to db
# db_url = os.environ.get("MONGODB_URI")
# if db_url == None:
#     secret_reader = open("./secret_key.txt", 'r');
#     db_url = secret_reader.read().strip()
#     # print db_url
# client = MongoClient(db_url)
# db = client.drdot

#declare route
@app.route("/")
def hello():
    print "we are sending over the fracking file"
    return send_file("templates/index.html")
