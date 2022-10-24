import json

with open('data.json') as f:
	obj = json.load(f)
	
def questions():
	for key, value in obj.items():
		for propt in value:
			for k, v in propt.items():
				if k == 'question':
					return (f'{v}')

m = questions()
print(m)
