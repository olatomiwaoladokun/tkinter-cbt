import json

file = 'questions_data.json'
with open(file) as f:
	obj = json.load(f)

qsts = obj['questions']
opts = obj['options']
asws = obj['answers']


	