from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
import json

#Connect to twilio with Alex's keys
phone_num = "+14084258777"
with open('twilio_keys.json') as f:
    data = json.load(f)
account_sid = data['twilio_sid']
auth_token = data['twilio_api_key']
client = TwilioRestClient(account_sid, auth_token)

def message_phone(contact,message):
    try:
        output = client.messages.create(to=contact, from_="+17087628282",body=message)
        print "we sent the txt boy"
    except TwilioRestException as e:
        print(e)
