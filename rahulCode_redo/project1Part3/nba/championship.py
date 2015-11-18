import glob
import re

championshipInfo={}

for fileName in glob.glob("/Users/rahulkhanna/Documents/columbia/7th/databases/project1Part3/nba/playoffs/playoffs*"):
	with open(fileName) as f:
		for line in f:
			# print(line)
			if line.split(",")[0] in ["1","2","3","4","5","6","7","8","9","10","11","12"]:
				# print(line)
				name=line.split(",")[1]
			# print(name)
				if name in championshipInfo:
					championshipInfo[name]+=1
				else:
					championshipInfo[name]=1
	# break
	print(fileName)

with open("championshipInfo","w") as f:
	for key in championshipInfo:
		f.write(str(key)+" | "+str(championshipInfo[key]))
		f.write("\n")