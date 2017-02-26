from flask import Flask, request
from pymongo import MongoClient
from app import app
import os

#connect to db
db_url = os.environ.get("MONGODB_URI")
if db_url == None:
    secret_reader = open("./secret_key.txt", 'r');
    db_url = secret_reader.read().strip()
    # print db_url
client = MongoClient(db_url)
db = client.drdot

def get_connection():
    return db
