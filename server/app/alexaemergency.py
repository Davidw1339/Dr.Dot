from flask_ask import Ask, statement, question, session
from app import app
import logging


#setup flask app
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)
