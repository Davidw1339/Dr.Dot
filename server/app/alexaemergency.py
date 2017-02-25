from flask import Flask, request, render_template
from flask_ask import Ask, statement, question, session
from app import app
import logging
import twilioflask

phone_num = "+14084258777"

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
    twilioflask.message_phone(phone_num, "lick my butt you iranian beauty")
    sent_msg = render_template('sent')
    return statement(sent_msg)


@ask.intent("NoIntent")
def no_request():
    canceled_msg = render_template('cancel')
    #set database to cancel emergency
    return statement(canceled_msg)
