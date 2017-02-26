from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
import json

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
    message_phone("+17737108632","You are an emergency contact for "+ user +", please call 911.")
    message_phone("+14084258777", "You are an emergency contact for "+ user +", please call 911.")

def endEmergencyText(user):
    message_phone("+17737108632",user +"'s emergency is over, thank you.")
    message_phone("+14084258777",user +"'s emergency is over, thank you.")