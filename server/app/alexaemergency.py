from flask import Flask, request, render_template
from flask_ask import Ask, statement, question, session
from app import app
import logging
import twilioflask
import symptomsIMO

phone_num = "+14084258777"
lpcount = 0
mainStr = ''
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

#Say the phrase "Cancel using emergency" to cancel instead
@ask.intent("NoIntent")
def no_request():
    canceled_msg = render_template('cancel')
    #set database to cancel emergency
    return statement(canceled_msg)

@ask.intent("SympIntent")
def symp_request():
    symp_msg = render_template('symptomes')
    return question(symp_msg)

@ask.intent("AnswerIntent",convert={'first': str})
def symp_list(first):
    if(first == ''):
        nof = render_template(nofound)
        return statement(nof)
    mainStr = parseLookup(first)
    if(mainStr==0):
        nom = render_template(nomatch)
        return statement(nom)
    #insert code to find and get specialist here
    sv = render_template(saved)
    return statement(sv)


