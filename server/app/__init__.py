from flask import Flask
import os

# ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/')
# app = Flask(__name__, template_folder=ASSETS_DIR, static_folder=ASSETS_DIR)
app = Flask(__name__)
from app import user
from app import twilioflask
from app import alexaemergency
from app import webapp
