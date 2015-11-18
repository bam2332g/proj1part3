import glob

allStarInfo={}

for fileName in glob.glob("/Users/rahulkhanna/Documents/columbia/7th/databases/project1Part3/nba/allstars/allstar*"):
	with open(fileName) as f:
		for line in f:
			# print(line)
			name=line.split(",")[0]
			# print(name)
			if name!="" and name!="Starters" and name!="Reserves" and name!="Team Totals" and name!="\n":
				parts=fileName.split("_")
				year=parts[2]
				if name in allStarInfo:
					allStarInfo[name].append(year)
				else:
					allStarInfo[name]=[year]
	print(fileName)

with open("allStarInfo","w") as f:
	for key in allStarInfo:
		f.write(str(key)+" | "+str(allStarInfo[key]))
		f.write("\n")