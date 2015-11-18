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

with open("probs") as f1:
	playerTeam={}
	with open("nflPlayerInfo") as f2:
		for line in f2:
			tup=eval(line)
			playerTeam[tup[0]]=tup[2]
	teams={}
	for line in f1:
		tup=eval(line)
		if playerTeam[tup[0]] in teams:
			teams[playerTeam[tup[0]]]+=6.0*tup[4]+4.0*tup[3]
		else:
			teams[playerTeam[tup[0]]]=6.0*tup[4]+4.0*tup[3]

	mi=100
	ma=0

	for team in teams:
		if teams[team]>ma:
			ma=teams[team]
		if teams[team]<mi:
			mi=teams[team]

	length=ma-mi

	for team in teams:
		teams[team]=((teams[team]-mi)/(length)*65)+20

with open("teamProb","w") as f:
	for team in teams:
		f.write(str(teams[team])+","+str(team))
		f.write("\n")
