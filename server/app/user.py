from flask import Flask, request, render_template
from pymongo import MongoClient
import json
import os

#initialize the app
from app import app

#connect to db
import db_connection
db = db_connection.get_connection()

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

@app.route("/load_doctor", methods=['POST'])
def load_doctor():
    username = request.form.get('username')
    doctor_name = request.form.get('doctor_name')
    doctor_address = request.form.get('doctor_address')
    doctor_phone = request.form.get('doctor_phone')
    put_doctor(username, doctor_name, doctor_address, doctor_phone)
    # if doctor_name:
    #     db.people.update(
    #        { "username": username },
    #        { '$set': {
    #               "doctor_name": doctor_name,
    #               "doctor_address": doctor_address
    #           }
    #        },
    #        { upsert: true }
    #     )

def put_doctor(username, doctor_name, doctor_address, doctor_phone):
    if doctor_name:
        db.users.update(
           { "username": username },
           { '$set': {
                  "doctor_name": doctor_name,
                  "doctor_address": doctor_address,
                  "doctor_phone": doctor_phone
              }
           },
           upsert=True)

@app.route("/get_doctor", methods=['GET'])
def get_doctor():
    username = request.args.get('username')
    user = db.users.find_one({"username": username})
    if user:
        data = {
            "doctor_name": user['doctor_name'],
            "doctor_address": user['doctor_address'],
            "doctor_phone": user['doctor_phone']
        }
        return json.dumps(data)
    return ""
