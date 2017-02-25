from flask import Flask, request, render_template
from flask_ask import Ask, statement, question, session
from app import app
import logging

#setup flask app
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def new_game():
    confirm_msg = render_template('confirm')
    return question(confirm_msg)


@ask.intent("YesIntent")
def send_msg():
    #change data to
    sent_msg = render_template('sent')
    return statement(sent_msg)

#Say the phrase "Cancel using emergency" to cancel instead
@ask.intent("NoIntent")
def no_request():
    canceled_msg = render_template('cancel')
    #set database to cancel emergency
    return statement(canceled_msg)
