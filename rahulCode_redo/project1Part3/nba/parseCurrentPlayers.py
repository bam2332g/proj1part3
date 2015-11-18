# parsing the dump to get all the keys for the current players
import json
dic={}
with open('currentPlayerDump.json','r') as f:
	data=json.load(f)
	print data["resultSets"][0]["headers"]
	print len(data["resultSets"][0]["rowSet"])
	for obj in data["resultSets"][0]["rowSet"]:
		if obj[0] not in dic:
			dic[obj[0]]=obj[1]
	with open('playerKey','w') as f1:
		for key in dic:
			f1.write(str(key)+" : "+ str(dic[key])+"\n")