from flask import Flask, request, render_template
from flask_ask import Ask, statement, question, session
from app import app
import logging
import twilioflask
import symptomsIMO as p

phone_num = "+14084258777"
lpcount = 0
mainStr = ''
#setup flask app
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

with open('IMOTitleToSpecialistMapping.json') as f:
    symptom_specialist_mapping = json.load(f)

def request_doctor(specialist_type):
    sess = requests.Session()
    
    url = 'https://api.betterdoctor.com/2016-03-01/doctors?'
    location = 'location=40.120%2C-88.272%2C100' # hard coded to Champaign IL... TODO: use server 
    user_location = 'user_location=40.120%2C-88.272'
    skip = 'skip=0'
    limit = 'limit=10'
    
    specialty_uid = 'specialty_uid=' + specialist_type
    insurance_uid = 'insurance_uid=medicaid-medicaid'

    sort = 'sort=distance-asc'
    user_key = 'user_key=9a652b68e9692e8b69892feb57e2a250'

    made_url = url + location + '&' + user_location + '&' + skip + '&' + limit + '&' + specialty_uid + '&' + insurance_uid + '&' + sort + '&' + user_key

    html = sess.get(made_url)

    json_data = json.loads(html.content.decode('utf-8'))

    doctor_data = []
    practice_data = []

    for data in json_data["data"]:
        doctor_data.append(data['profile'])
        practice_data.append('practices')
    
    return doctor_data

def find_specialist_with_symptom(symptom):
    if symptom in symptom_specialist_mapping:
        return symptom_specialist_mapping[symptom]
    return ''

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
    print "THIS IS HAPPENING" , first
    if(first == ''):
        nof = render_template('nofound')
        return statement(nof)
    mainStr = p.parseLookup(first)
    if(mainStr==0):
        nom = render_template('nomatch')
        return statement(nom)
    #insert code to find and get specialist here
    sv = render_template('saved')
    return statement(sv)
