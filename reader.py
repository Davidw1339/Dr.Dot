from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/reddit_reader")
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

data = request_doctor('pediatrician')
for profile in data:
	print(profile['first_name'])

def search_symptom(symptom):
	sess = requests.Session()
	sess.headers.update(
		{
			'Authorization' : 'Basic ODBhNDQyYTVjYTU3NDlmY2FkM2VlYWJjZWQyZWJlMDU6REZEQjk5NUY5MDQ0NkUwNzAwRDhFRDgzNDQ4RTg3MTZEQTc4ODRGRDQwQjc3NEYyNjM5MTRBRTg2MTZDMzIzNA==',
			'Content-Type': 'application/json'
		})
	symptom_arr = []
	# for symptom in symptoms:
	symptom_arr.append({
		"FreeText": symptom
	})
	patient_data_json = {
		"Problems" : symptom_arr
	}
	patient_data = str(patient_data_json)
	str(patient_data)

	url = 'https://ipl-nonproduction-customer_validation.e-imo.com/api/v3/actions/categorize'
	html = sess.post(url, data = patient_data)

	data = json.loads(html.content.decode('utf-8'))

	category = data["Categories"][0]["Problems"][0]["Details"]["IMOTitle"]
	category = category.lower()
	return category

def find_specialist_with_symptom(symptom):
	if symptom in symptom_specialist_mapping:
		return symptom_specialist_mapping[symptom]
	return ''

# data = search_symptom('heart attack')
# print(data)

@app.route('/')
def homepage():
	return "hi there, how ya doin?"

@ask.launch
def start_skill():
	welcome_message = 'Hello there, would you like the news?'
	return question(welcome_message)

@ask.intent("YesIntent")
def share_headlines():
	headlines = get_headlines()
	headlines_msg = 'The current world news headlines are ()'.format(headlines)

@ask.intent("NoIntent")
def no_intent():
	bye_text = 'I am not sure why you asked me to run then, but okay... bye'
	return statement(bye_text)

if __name__ == '__main__':
	app.run(debug=True)
