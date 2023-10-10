import json
from datetime import datetime


def loadFile():
	try:
		with open("score.json", 'r') as file:
			return json.load(file)
	except Exception:
		with open("score.json", 'w') as file:
			json.dump([], file)

		with open("score.json", 'r') as file:
			return json.load(file)

def score(obj):
	date_time = str(datetime.now())
	scores = loadFile()
	obj["date_time"] = date_time
	scores.append(obj)
	with open("score.json", 'w') as file:
		json.dump(scores, file)
