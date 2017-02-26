from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
import twilio.twiml
import json, time, alexaemergency

#Connect to twilio with Alex's keys

with open('twilio_keys.json') as f:
    data = json.load(f)
account_sid = data['twilio_sid']
auth_token = data['twilio_api_key']
client = TwilioRestClient(account_sid, auth_token)
def message_phone(contact,message):
    try:
        output = client.messages.create(to=contact, from_="+17087628282",body=message)
        #print "we sent the txt boy"
    except TwilioRestException as e:
        print(e)

def sendEmergencyText(user):
    global emergency
    i = 0
    message_phone("+17737108632","You are an emergency contact for "+ user +", please call 911.")
    resp = twilio.twiml.Response()
    while i < TIME_LIMIT:
        if len(str(resp)) != 50:
            return str(resp)
        time.sleep(1)
        i+=1
    message_phone("+14084258777", "You are an emergency contact for David, please call 911.")
