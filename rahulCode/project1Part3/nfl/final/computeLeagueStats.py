import datetime
from datetime import date

avgAgeOfPlayer=-1
avgAgeOfTeam=-1
avgWinPct=-1
avgYrsOfExp=-1

with open("nflTeamInfo") as f:
	total=0
	for line in f:
		total=total+(float(eval(line)[4])/float(eval(line)[4]+eval(line)[5]))
	avgWinPct=total/32.0
	print(str(avgWinPct))

with open("nflPlayerInfo") as f:
	totalExp=0
	totalAgePlayer=0
	ageOfTeam={}
	now=date.today()
	for line in f:
		tup=eval(line)
		dob=tup[4]
		age=((now-dob).days)/365.0
		totalAgePlayer+=age
		totalExp+=(tup[5]*10.0)

		if tup[2] in ageOfTeam:
			ageOfTeam[tup[2]][0]+=age
			ageOfTeam[tup[2]][1]+=1.0
		else:
			ageOfTeam[tup[2]]=[age,1.0]

	avgYrsOfExp=totalExp/471.0
	avgAgeOfPlayer=totalAgePlayer/471.0
	totalAgePlayer=0
	for key in ageOfTeam:
		totalAgePlayer+=ageOfTeam[key][0]/ageOfTeam[key][1]
	avgAgeOfTeam=totalAgePlayer/32.0
	print(str(avgYrsOfExp))
	print(str(avgAgeOfPlayer))
	print(str(avgAgeOfTeam))
