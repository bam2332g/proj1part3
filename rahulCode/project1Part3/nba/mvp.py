import re

mvp={}
with open("awards_mvp_NBA-mvp.csv") as f:
	i=0
	for line in f:
		if not (re.match(" ",line.split(",")[0]) or re.match("\n",line.split(",")[0])):
			if line.split(",")[2] in mvp:
				mvp[line.split(",")[2]].append(line.split(",")[0].split("-")[0])
			else:
				if line.split(",")[2]!="" and line.split(",")[2]!="Player":
					mvp[line.split(",")[2]]=[line.split(",")[0].split("-")[0]]
		i+=1
		if(i>17):
			break

# print(str(mvp))

with open("mvp","w") as f:
	for key in mvp:
		f.write(str(key)+" | "+str(mvp[key]))
		f.write("\n")