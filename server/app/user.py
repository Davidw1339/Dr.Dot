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
    username = request.form['username']
    cursor = db.users.find({'username': username})
    if cursor:
        for user in cursor:
            return 'already-registered'

    #get credentials
    password = request.form['password']
    address = request.form['address']
    name = request.form['name']
    assistant_phone = request.form['assistantphone']
    emergency_phone = request.form['emergencyphone']

    user = db.users.insert_one(
    {
        "username": username,
        "password": password,
        "address": address,
        "assistantphone": assistant_phone,
        "emergencyphone" : emergency_phone,
    })
    if user:
        return "registered"
    else:
        return "register-fail"

@app.route("/login", methods=['GET'])
def login_user():
    username = request.args.get('username')
    password = request.args.get('password')
    user = db.users.find_one({"username": username, "password": password})
    if user:
        return "auth"
    return "no-auth"


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
