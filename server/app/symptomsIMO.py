import requests
import json
from itertools import *


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1, 1, -1))

#lookup the symptom in IMO
def lookup(symptRaw):
	sympt = json.dumps({"Problems": [{"FreeText":symptRaw}]})
	
	headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
	auth = ('29740865e46a477fbccbac990a808944',
	 '13E8A349D7DF0CC2318C7E5F9B576879BB017BDA88DE016B220C4D60A8797A6B')
	 
	r = requests.post("https://ipl-nonproduction-customer_validation.e-imo.com/api/v3/actions/categorize",
	auth = auth,
	headers = headers,
	data = sympt)
	
	return r.text

#checks if IMO returned a categorized symptom
def checkFound(res):
		jsonRes = json.loads(res)
		
		if(jsonRes["Categories"][0]["Name"] == "Uncategorized"):
			return 0
		return 1
	
#try to find a sympton in a string	
def parseLookup(input):
	data = json.loads(lookup(input))
	return data["Categories"][0]["Problems"][0]["Details"]["IMOTitle"]

	# ls = input.split(" ")
	
	# for i in ls:
	# 	if(len(i) <= 2):
	# 		ls.remove(i)

	# sets = list(powerset(ls))
	
	# for i in sets:
	# 	res = lookup(" ".join(i))
	# 	if(checkFound(res)):
	# 		jsonRes = json.loads(res)
	# 		return jsonRes["Categories"][0]["Problems"][0]["Details"]["CategoryTitle"]
	# return 0

print(parseLookup('I am feeling sad'))
print(parseLookup('chest pain'))
print(parseLookup('skin pain'))
print(parseLookup('tummy hurts'))
print(parseLookup('stomach ache'))
print(parseLookup('leg broken'))
print(parseLookup('bullet wound'))
print(parseLookup('cold'))
print(parseLookup('flu'))
print(parseLookup('back pain'))
print(parseLookup('earache'))
print(parseLookup('headache'))
print(parseLookup('chronic pelvic pain'))
print(parseLookup('toothache'))
print(parseLookup('vaginal pain'))
print(parseLookup('rectal pain'))
print(parseLookup('dermatomal pain'))
print(parseLookup('chills'))
print(parseLookup('fever'))
print(parseLookup('light-headed'))
print(parseLookup('dizzy'))
print(parseLookup('dry mouth'))
print(parseLookup('nauseated'))
print(parseLookup('short of breath'))
print(parseLookup('chronic drowsiness'))
print(parseLookup('dry mouth'))
print(parseLookup('I am feeling depressed'))

