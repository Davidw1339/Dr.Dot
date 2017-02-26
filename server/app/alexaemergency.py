from flask import Flask, request, render_template
from flask_ask import Ask, statement, question, session
from app import app
import logging
import json
import requests
import twilioflask
import symptomsIMO as p
import db_connection
import user

db = db_connection.get_connection()
phone_num = "+14084258777"
#setup flask app
ask = Ask(app, "/")
vac = False
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

with open('IMOTitleToSpecialistMapping.json') as f:
    symptom_specialist_mapping = json.load(f)

def request_doctor(specialist_type):
    specialist_type = specialist_type.lower()

    sess = requests.Session()

    url = 'https://api.betterdoctor.com/2016-03-01/doctors?'
    location = 'location=40.120%2C-88.272%2C100' # hard coded to Champaign IL... TODO: use server
    user_location = 'user_location=40.120%2C-88.272'
    skip = 'skip=0'
    limit = 'limit=10'

    specialty_uid = 'specialty_uid=' + specialist_type
    #nsurance_uid = 'insurance_uid=medicaid-medicaid'

    sort = 'sort=distance-asc'
    user_key = 'user_key=9a652b68e9692e8b69892feb57e2a250'

    made_url = url + location + '&' + user_location + '&' + skip + '&' + limit + '&' + specialty_uid + '&' + sort + '&' + user_key

    html = sess.get(made_url)

    json_data = json.loads(html.content.decode('utf-8'))

    #doctor_data = []
    #practice_data = []

    #for data in json_data["data"]:
    #    doctor_data.append(data['profile'])
    #    practice_data.append('practices')

    first_data = json_data['data'][0]
    first_doctor = first_data['profile']
    first_practice = first_data['practices'][0]

    print('getting first practice')
    print (first_practice)

    visit = first_practice['visit_address']
    street = visit['street']
    city = visit['city']
    state = visit['state']

    address = street + ', ' + city + ', ' + state
    print(address)

    phone = first_practice['phones'][0]['number']
    print(phone)

    first_name = first_doctor['first_name']
    last_name = first_doctor['last_name']

    doctor_name = first_name + ' ' + last_name

    user.put_doctor("david", doctor_name, address, phone)

    if address and phone:
        return True
    return False


def find_specialist_with_symptom(symptom):
    symptom = symptom.lower()
    if symptom in symptom_specialist_mapping:
        print('good symptom')
        print(symptom)
        specialist = str(symptom_specialist_mapping[symptom])
        print(specialist)
        return request_doctor(specialist)

    print('fake symptom')
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
    global vac
    vac = True
    symp_msg = render_template('symptomes')
    return question(symp_msg)

@ask.intent("AnswerIntent",convert={'first': str})
def symp_list(first):
    print "THIS IS HAPPENING" , first
    global vac
    if not vac:
        nov = render_template('notcomm')
        return statement(nov)
    vac = False
    if(first == ''):
        nof = render_template('nofound')
        return statement(nof)
    mainStr = p.parseLookup(first)
    if(mainStr==0):
        nom = render_template('nomatch')
        return statement(nom)
    #insert code to find and get specialist here

    print 'GONNA LOOK FOR THE SPECIALIST NOW!!!'

    print(mainStr)
    hasFoundSpecialist = find_specialist_with_symptom(mainStr)
    #print("json")
    #print(data)

    if hasFoundSpecialist:
        sv = render_template('saved')
    else:
        sv = render_template('nomatch')
    return statement(sv)
