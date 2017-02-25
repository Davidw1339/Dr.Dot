from flask import Flask, request, render_template
from pymongo import MongoClient
import json
import os

#initialize the app
from app import app

#connect to db
db_url = os.environ.get("MONGODB_URI")
if db_url == None:
    secret_reader = open("./secret_key.txt", 'r');
    db_url = secret_reader.read().strip()
    # print db_url
client = MongoClient(db_url)
db = client.drdot

@app.route("/register_user", methods=['POST'])
def register_user():
    user_id = request.form['userid']
    cursor = db.users.find({'userid': user_id})
    if cursor:
        for user in cursor:
            return 'already-registered'

    #get credentials
    address = request.form['address']
    name = request.form['name']
    assistant_phone = request.form['assistantphone']
    emergency_phone = request.form['emergencyphone']

    user = db.users.insert_one(
    {
        "userid": user_id,
        "address": address,
        "assistantphone": assistant_phone,
        "emergencyphone" : emergency_phone,
    })
    if user:
        return "registered"
    else:
        return "register-fail"

@app.route("/get_user", methods=['GET'])
def get_user():
    userid = request.args.get('userid')
    user = db.users.find_one({"userid": userid})
    if user:
        user_json = {
            "userid": userid,
            "address": user["address"],
            "assistantphone": user["assistantphone"],
            "emergencyphone": user["emergencyphone"]
        }
    else:
        return "no user found"
    return json.dumps(user_json)
