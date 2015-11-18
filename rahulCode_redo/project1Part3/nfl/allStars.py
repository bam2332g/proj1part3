# needs to be edited
allStarInfo={}
with open("pb.txt") as f:
		for line in f:
			# print(line)
			name=line.split(", ")[0].replace("+","").replace("%","")
			year=line.split(", ")[1]
			# print(name)
			if name in allStarInfo:
				allStarInfo[name].append(year)
			else:
				allStarInfo[name]=[year]
	print(fileName)

with open("allStarInfo","w") as f:
	for key in allStarInfo:
		f.write(str(key)+" | "+str(allStarInfo[key]))
		f.write("\n")