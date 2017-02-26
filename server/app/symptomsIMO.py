import requests
import json
import imoKeys
from itertools import *


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1, 1, -1))

#lookup the symptom in IMO
def lookup(symptRaw):
	sympt = json.dumps({"Problems": [{"FreeText":symptRaw}]})
	
	headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
	auth = imoKeys.auth
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
	ls = input.split(" ")
	
	for i in ls:
		if(len(i) <= 2):
			ls.remove(i)

	sets = list(powerset(ls))
	
	for i in sets:
		res = lookup(" ".join(i))
		if(checkFound(res)):
			jsonRes = json.loads(res)
			return jsonRes["Categories"][0]["Problems"][0]["Details"]["ICD10Title"]
	return 0
