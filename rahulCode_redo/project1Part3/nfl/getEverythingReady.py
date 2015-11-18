import csv
from datetime import date

def atLeastZero(integer):
	if integer<0:
		return 0
	else:
		return integer

class nflPlayer():
	def __init__(self,key,name,dob,exp,pos):
		self.leagueID=0
		self.key=key
		self.name=name
		self.exp=exp
		self.pos=pos
		self.chmps=0
		self.teamID=-1
		self.stats={}
		self.allStars=[]
		self.mvps=[]
		self.dob=date(int(dob.split()[2]),int(months[dob.split()[0]]),int(dob.split()[1].replace(",","")))

	def addChmpInfo(self,chmps):
		self.chmps=chmps

	def addTeamInfo(self,teamID):
		self.teamID=teamID

	def addAllStars(self,allStars):
		self.allStars=allStars

	def addMVPs(self,mvps):
		self.mvps=mvps

	def addStats(self,pStats,rStats):
		if self.pos=="QB":
			if "Years" in pStats.keys():
				for i in range(0,len(pStats["Years"])):
					year=int(pStats["Years"][i])

					a=False
					m=False
					if year>=2005:
						if year in self.mvps:
							m=True
						if year in self.allStars:
							a=True
						if year in rStats["Years"]:
							j=rStats["Years"].index(str(year))
							self.stats[year]=(self.key, year, max(int(pStats["Games"][i]),int(rStats["Games"][j])), atLeastZero(int(pStats["Yards"][i])),
								int(pStats["Interceptions"][i]), int(pStats["Fumbles"][i])*3, int(pStats["Completions"][i]), int(pStats["Attempts"][i]),
								float(pStats["QB Rating"][i]), int(rStats["Rushes"][j]), atLeastZero(int(rStats["Yards"][j])),0,0,
								int(pStats["Touchdowns"][i])+int(rStats["Touchdowns"][j]),a,m)

						else:
							self.stats[year]=(self.key, year, int(pStats["Games"][i]), atLeastZero(int(pStats["Yards"][i])),
								int(pStats["Interceptions"][i]), int(pStats["Fumbles"][i])*3, int(pStats["Completions"][i]), int(pStats["Attempts"][i]),
								float(pStats["QB Rating"][i]), 0, 0, 0, 0, int(pStats["Touchdowns"][i]),a,m)

			if "Years" in rStats.keys():
				for i in range(0,len(rStats["Years"])):
					year=int(rStats["Years"][i])

					a=False
					m=False
					if year>=2005:
						if year in self.mvps:
							m=True
						if year in self.allStars:
							a=True
						if year not in self.stats:
							self.stats[year]=(self.key,year,rStats["Games"][i],0,0,0,0,0,0,int(rStats["Rushes"][i]), atLeastZero(int(rStats["Yards"][i])),0,0,int(rStats["Touchdowns"][i]),a,m)

		else:
			if "Years" in pStats.keys():
				for i in range(0,len(pStats["Years"])):
					year=int(pStats["Years"][i])

					a=False
					m=False
					if year>=2005:
						if year in self.mvps:
							m=True
						if year in self.allStars:
							a=True
						if "Years" in rStats.keys():
							if year in rStats["Years"]:
								j=rStats["Years"].index(str(year))
								self.stats[year]=(self.key, year, max(int(pStats["Games"][i]),int(rStats["Games"][j])), 0, 0, 0, 0, 0, 0, int(rStats["Rushes"][j]), atLeastZero(int(rStats["Yards"][j])),
									int(pStats["Receptions"][i]), atLeastZero(int(pStats["Yards"][i])), int(pStats["Touchdowns"][i])+int(rStats["Touchdowns"][j]),a,m)

							else:
								self.stats[year]=(self.key, year, int(pStats["Games"][i]), 0, 0, 0, 0, 0, 0, 0, 0,
									int(pStats["Receptions"][i]), atLeastZero(int(pStats["Yards"][i])), int(pStats["Touchdowns"][i]),a,m)
						else:
							self.stats[year]=(self.key, year, int(pStats["Games"][i]), 0, 0, 0, 0, 0, 0, 0, 0,
								int(pStats["Receptions"][i]), atLeastZero(int(pStats["Yards"][i])), int(pStats["Touchdowns"][i]),a,m)

			if "Years" in rStats.keys():
				for i in range(0,len(rStats["Years"])):
					year=int(rStats["Years"][i])

					a=False
					m=False
					if year>=2005:
						if year in self.mvps:
							m=True
						if year in self.allStars:
							a=True
						if year not in self.stats:
							self.stats[year]=(self.key,year,rStats["Games"][i],0,0,0,0,0,0,int(rStats["Rushes"][i]), atLeastZero(int(rStats["Yards"][i])),0,0,int(rStats["Touchdowns"][i]),a,m)

	def __repr__(self):
		output=(self.key, self.leagueID, self.teamID, self.name, self.dob, self.exp, self.pos, self.chmps)
		return str(output)

	def __str__(self):
		output=(self.key, self.leagueID, self.teamID, self.name, self.dob, self.exp, self.pos, self.chmps)
		return str(output)

class nflStat():
	def __init__(self,stats):
		self.stats=stats

	def __repr__(self):
		return str(self.stats)

	def __str__(self):
		return str(self.stats)

class topnflPlayer():
	def __init__(self,key,name,chmps,pos,allStars,mvps):
		self.leagueID=0
		self.key=key
		self.name=name
		self.chmps=chmps
		self.pos=pos
		self.allStars=allStars
		self.mvps=mvps

	def __repr__(self):
		output=(self.key, self.leagueID, self.name, self.chmps, self.pos, self.allStars, self.mvps)
		return str(output)

	def __str__(self):
		output=(self.key, self.leagueID, self.name, self.chmps, self.pos, self.allStars, self.mvps)
		return str(output)

class topnflPlayerStats():
	def __init__(self,key,qbYards,qbInter,qbSacks,qbCompl,qbAtt,qbRating,rushingAtt,rushingYds,receptions,receivingYds,td):
		self.stats=(key,atLeastZero(float(qbYards)),float(qbInter),float(qbSacks),float(qbCompl),float(qbAtt),float(qbRating),float(rushingAtt),atLeastZero(float(rushingYds)),float(receptions),atLeastZero(float(receivingYds)),float(td))

	def __repr__(self):
		return str(self.stats)

	def __str__(self):
		return str(self.stats)

class team():
	def __init__(self,key,name,ties,wins,losses,chmps):
		self.key=key
		self.name=name
		self.ties=ties
		self.wins=wins
		self.losses=losses
		self.chmps=chmps
		self.leagueID=0

	def __repr__(self):
		output=(self.key, self.name, self.leagueID, self.ties, self.wins, self.losses, self.chmps)
		return str(output)

	def __str__(self):
		output=(self.key, self.name, self.leagueID, self.ties, self.wins, self.losses, self.chmps)
		return str(output)


months={
	"January":1,
	"February":2,
	"March":3,
	"April":4,
	"May":5,
	"June":6,
	"July":7,
	"August":8,
	"September":9,
	"October":10,
	"November":11,
	"December":12
}

teams={}
players={}
topPlayers={}
nflStats={}
topPlayersStats={}

playersCount=385
topPlayersCount=50
teamsCount=0

mvpInfo={}
with open("mvp.txt") as f:
	for line in f:
		name=line.split(",")[0]
		year=int(line.split(",")[1])
		if name in mvpInfo:
			mvpInfo[name].append(year)
		else:
			mvpInfo[name]=[year]

allStarInfo={}
with open("pb.txt") as f:
	for line in f:
		name=line.split(", ")[0].replace("+","").replace("%","")
		year=int(line.split(", ")[1])

		if name in allStarInfo:
			allStarInfo[name].append(year)
		else:
			allStarInfo[name]=[year]

championshipInfo={}
with open("sb.txt") as f:
	for line in f:
		name=line.split(", ")[0].replace("+","").replace("*","").strip()
		if name in championshipInfo:
			championshipInfo[name]+=1
		else:
			championshipInfo[name]=1

with open("teamInfo.csv",'rU') as f:
	doc=csv.reader(f,delimiter=",")
	first=True
	for line in doc:
		if not first:
			temp=team(int(line[0]),line[1],int(line[2]),int(line[3]),int(line[4]),int(line[5]))
			teams[line[1]]=temp
		else:
			first=False

with open("qbInfo") as f:
	for line in f:
		bio=eval(line)[0]
		passingStats=eval(line)[1]
		rushingStats=eval(line)[2]
		bioSplit=bio.split(" | ")
		# print(line)
		temp=nflPlayer(int(playersCount),bioSplit[0],bioSplit[1],float(bioSplit[3]),"QB")
		team=bioSplit[2]
		# if team not in teams:
		# 	teams[team]=teamsCount
		# 	teamsCount+=1
	# print(teams)
		temp.addTeamInfo(teams[team].key)
		if temp.name in mvpInfo:
			print(temp.name+" - m")
			temp.addMVPs(mvpInfo[temp.name])
			print(mvpInfo[temp.name])
		if temp.name in allStarInfo:
			print(temp.name+" - a")
			temp.addAllStars(allStarInfo[temp.name])
			print(allStarInfo[temp.name])
		if temp.name in championshipInfo:
			print(temp.name+" -c")
			temp.addChmpInfo(championshipInfo[temp.name])
			print(championshipInfo[temp.name])

		temp.addStats(passingStats,rushingStats)
		if temp.teamID!=-1:
			players[playersCount]=temp
			playersCount+=1
		else:
			print("Team Problem")
			print(line)

with open("wrInfo") as f:
	for line in f:
		bio=eval(line)[0]
		recStats=eval(line)[1]
		rushStats=eval(line)[2]
		bioSplit=bio.split(" | ")
		# print(line)
		temp=nflPlayer(int(playersCount),bioSplit[0],bioSplit[1],float(bioSplit[3]),"WR")
		team=bioSplit[2]
		# if team not in teams:
		# 	teams[team]=teamsCount
		# 	teamsCount+=1
	# print(teams)
		temp.addTeamInfo(teams[team].key)
		if temp.name in mvpInfo:
			print(temp.name+" - m")
			temp.addMVPs(mvpInfo[temp.name])
			print(mvpInfo[temp.name])
		if temp.name in allStarInfo:
			print(temp.name+" - a")
			temp.addAllStars(allStarInfo[temp.name])
			print(allStarInfo[temp.name])
		if temp.name in championshipInfo:
			print(temp.name+" -c")
			temp.addChmpInfo(championshipInfo[temp.name])
			print(championshipInfo[temp.name])
		temp.addStats(recStats,rushStats)
		if temp.teamID!=-1:
			players[playersCount]=temp
			playersCount+=1
		else:
			print("Team Problem")
			print(line)

with open("rbInfo") as f:
	for line in f:
		bio=eval(line)[0]
		recStats=eval(line)[1]
		rushStats=eval(line)[2]
		bioSplit=bio.split(" | ")
		# print(line)
		temp=nflPlayer(int(playersCount),bioSplit[0],bioSplit[1],float(bioSplit[3]),"RB")
		team=bioSplit[2]
		# if team not in teams:
		# 	teams[team]=teamsCount
		# 	teamsCount+=1
	# print(teams)
		temp.addTeamInfo(teams[team].key)
		temp.addStats(recStats,rushStats)
		if temp.name in mvpInfo:
			print(temp.name+" - m")
			temp.addMVPs(mvpInfo[temp.name])
			print(mvpInfo[temp.name])
		if temp.name in allStarInfo:
			print(temp.name+" - a")
			temp.addAllStars(allStarInfo[temp.name])
			print(allStarInfo[temp.name])
		if temp.name in championshipInfo:
			print(temp.name+" -c")
			temp.addChmpInfo(championshipInfo[temp.name])
			print(championshipInfo[temp.name])
		temp.addStats(recStats,rushStats)
		if temp.teamID!=-1:
			players[playersCount]=temp
			playersCount+=1
		else:
			print("Team Problem")
			print(line)
print("Other Players should start here: "+str(playersCount))

for playerID in players:
	stats=players[playerID].stats
	for year in stats:
		nflStats[(int(playerID),year)]=stats[year]

with open("topQB.csv","rU") as f:
	doc=csv.reader(f,delimiter=",")
	first=False
	for line in doc:
		if first:
			temp1=topnflPlayer(topPlayersCount,line[0],int(line[12]),"QB",int(line[14]),int(line[13]))
			temp2=topnflPlayerStats(topPlayersCount,line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11])
			topPlayers[topPlayersCount]=temp1
			topPlayersStats[topPlayersCount]=temp2
			topPlayersCount+=1
		else:
			first=True

with open("topRB.csv","rU") as f:
	doc=csv.reader(f,delimiter=",")
	first=False
	for line in doc:
		if first:
			# print(line)
			temp1=topnflPlayer(topPlayersCount,line[0],int(line[12]),"RB",int(line[14]),int(line[13]))
			temp2=topnflPlayerStats(topPlayersCount,line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11])
			topPlayers[topPlayersCount]=temp1
			topPlayersStats[topPlayersCount]=temp2
			topPlayersCount+=1
		else:
			first=True

with open("topWR.csv","rU") as f:
	doc=csv.reader(f,delimiter=",")
	first=False
	for line in doc:
		if first:
			temp1=topnflPlayer(topPlayersCount,line[0],int(line[12]),"WR",int(line[14]),int(line[13]))
			temp2=topnflPlayerStats(topPlayersCount,line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11])
			topPlayers[topPlayersCount]=temp1
			topPlayersStats[topPlayersCount]=temp2
			topPlayersCount+=1
		else:
			first=True

print("Other NFL Players should start here: "+str(topPlayersCount))


with open("/Users/rahulkhanna/Documents/columbia/7th/databases/project1Part3/nfl/final/nflPlayerInfo","w") as f:
	for key in players:
		f.write(str(players[key]))
		f.write("\n")

with open("/Users/rahulkhanna/Documents/columbia/7th/databases/project1Part3/nfl/final/nflTeamInfo","w") as f:
	for key in teams:
		f.write(str(teams[key]))
		f.write("\n")

with open("/Users/rahulkhanna/Documents/columbia/7th/databases/project1Part3/nfl/final/nflTopPlayersInfo","w") as f:
	for key in topPlayers:
		f.write(str(topPlayers[key]))
		f.write("\n")

with open("/Users/rahulkhanna/Documents/columbia/7th/databases/project1Part3/nfl/final/nflTopPlayersStats","w") as f:
	for key in topPlayersStats:
		f.write(str(topPlayersStats[key]))
		f.write("\n")

with open("/Users/rahulkhanna/Documents/columbia/7th/databases/project1Part3/nfl/final/nflPlayerStats","w") as f:
	for key in nflStats:
		f.write(str(nflStats[key]))
		f.write("\n")