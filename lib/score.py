import json


scores = []
def score(date_time, obj):
	obj["date_time"] = date_time
	scores.append(obj)
	with open("score.json", 'w') as file:
		json.dump(scores, file)
