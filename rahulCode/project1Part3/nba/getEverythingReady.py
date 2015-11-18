import csv
from datetime import date
class nbaPlayer():
	def __init__(self,key,name,dob,exp,pos):
		self.leagueID=1
		self.key=key
		self.name=name
		self.exp=exp
		self.pos=pos
		self.chmps=0
		self.teamID=-1
		self.stats={}
		self.allStars=[]
		self.mvps=[]
		self.dob=date(int(dob.split("-")[0]),int(dob.split("-")[1]),int(dob.split("-")[2]))

	def addChmpInfo(self,chmps):
		self.chmps=chmps

	def addTeamInfo(self,teamID):
		self.teamID=teamID

	def addAllStars(self,allStars):
		self.allStars=allStars

	def addMVPs(self,mvps):
		self.mvps=mvps

	def addStats(self,stats):
		self.stats=stats

	def __repr__(self):
		output=(self.key, self.leagueID, self.teamID, self.name, self.dob, self.exp, self.pos, self.chmps)
		return str(output)

	def __str__(self):
		output=(self.key, self.leagueID, self.teamID, self.name, self.dob, self.exp, self.pos, self.chmps)
		return str(output)

class nbaStat():
	def __init__(self,playerID,year,games,turnover,steals,blks,pts,fgm,fga,tpm,tpa,ftm,fta,rebs,assists,allStar,mvp):
		self.playerID=playerID
		self.year=year
		self.games=games
		self.turnover=turnover
		self.steals=steals
		self.blks=blks
		self.pts=pts
		self.fgm=fgm
		self.fga=fga
		self.tpm=tpm
		self.tpa=tpa
		self.ftm=ftm
		self.fta=fta
		self.rebs=rebs
		self.assists=assists
		self.allStar=allStar
		self.mvp=mvp

	def __repr__(self):
		output=(self.playerID, self.year, self.games, self.turnover, self.steals, self.blks, self.pts, self.fgm, self.fga, self.tpm, self.tpa, self.ftm, self.fta, self.rebs, self.assists, self.allStar, self.mvp)
		return str(output)

	def __str__(self):
		output=(self.playerID, self.year, self.games, self.turnover, self.steals, self.blks, self.pts, self.fgm, self.fga, self.tpm, self.tpa, self.ftm, self.fta, self.rebs, self.assists, self.allStar, self.mvp)
		return str(output)

class topNbaPlayer():
	def __init__(self,key,name,chmps,pos,allStars,mvps):
		self.leagueID=1
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

class topNbaPlayerStats():
	def __init__(self,key,ppg,rbspg,astpg,stlpg,blkpg,fgpg,tppg,ftpg):
		self.key=key
		self.stlpg=stlpg
		self.blkpg=blkpg
		self.ppg=ppg
		self.fgpg=fgpg
		self.tppg=tppg
		self.ftpg=ftpg
		self.rbspg=rbspg
		self.astpg=astpg

	def __repr__(self):
		output=(self.key, self.stlpg, self.blkpg, self.ppg, self.fgpg, self.tppg, self.ftpg, self.rbspg, self.astpg)
		return str(output)

	def __str__(self):
		output=(self.key, self.stlpg, self.blkpg, self.ppg, self.fgpg, self.tppg, self.ftpg, self.rbspg, self.astpg)
		return str(output)

class team():
	def __init__(self,key,name,ties,wins,losses,chmps):
		self.key=key
		self.name=name
		self.ties=ties
		self.wins=wins
		self.losses=losses
		self.chmps=chmps
		self.leagueID=1

	def __repr__(self):
		output=(self.key, self.name, self.leagueID, self.ties, self.wins, self.losses, self.chmps)
		return str(output)

	def __str__(self):
		output=(self.key, self.name, self.leagueID, self.ties, self.wins, self.losses, self.chmps)
		return str(output)

teams={}
players={}
topPlayers={}
nbaStats={}
topPlayersStats={}

playersCount=0
topPlayersCount=0
teamsCount=0

allStarInfo={}
with open("allStarInfo") as f:
	for line in f:
		allStarInfo[line.split(" | ")[0]]=line.split(" | ")[1]

championshipInfo={}
with open("championshipInfo") as f:
	for line in f:
		championshipInfo[line.split(" | ")[0]]=line.split(" | ")[1]

mvpInfo={}
with open("mvp") as f:
	for line in f:
		mvpInfo[line.split(" | ")[0]]=line.split(" | ")[1]

with open("teamInfo.csv",'rU') as f:
	doc=csv.reader(f,delimiter=",")
	first=True
	for line in doc:
		if not first:
			temp=team(int(line[0]),line[1],int(line[2]),int(line[3]),int(line[4]),int(line[5]))
			teams[line[1]]=temp
		else:
			first=False

with open("playerInfo") as f:
	for line in f:
		bio=eval(line)[0]
		stats=eval(line)[1]
		bioSplit=bio.split(" | ")
		# print(line)
		temp=nbaPlayer(int(playersCount),bioSplit[1],bioSplit[2].split("T")[0],float(bioSplit[5]),bioSplit[4][0])
		team=bioSplit[3]
		# if team not in teams:
		# 	teams[team]=teamsCount
		# 	teamsCount+=1
	# print(teams)
		temp.addTeamInfo(teams[team].key)
		temp.addStats(stats)
		if temp.name in mvpInfo:
			print(temp.name+" - m")
			temp.addMVPs(mvpInfo[temp.name])
		if temp.name in allStarInfo:
			print(temp.name+" - a")
			temp.addAllStars(allStarInfo[temp.name])
		if temp.name in championshipInfo:
			print(temp.name+" -c")
			temp.addChmpInfo(championshipInfo[temp.name])
		if temp.teamID!=-1:
			players[playersCount]=temp
			playersCount+=1
		else:
			print("Team Problem")
			print(line)
print("Count for NFL Players should start here: "+str(playersCount))

for playerID in players:
	stats=players[playerID].stats
	name=players[playerID].name
	for year in stats:
		y=year.split("-")[0]
		if y in players[playerID].allStars:
			a=True
		else:
			a=False

		if y in players[playerID].mvps:
			m=True
		else:
			m=False
		temp=nbaStat(int(playerID),int(y),int(stats[year]["GP"]),int(stats[year]["TOV"]),int(stats[year]["STL"]),int(stats[year]["BLK"]),int(stats[year]["PTS"]),
				int(stats[year]["FGM"]),int(stats[year]["FGA"]),int(stats[year]["3PM"]),int(stats[year]["3PA"]),
				int(stats[year]["FTM"]),int(stats[year]["FTA"]),int(stats[year]["REB"]),int(stats[year]["AST"]),
				a,m)

		nbaStats[(int(playerID),int(y))]=temp


with open("awards_nba_50_greatest_stats2.csv","rU") as f:
	doc=csv.reader(f,delimiter=",")
	first=False
	second=False
	for line in doc:
		if first and second:
			# print(line)
			temp1=topNbaPlayer(topPlayersCount,line[0],int(line[16]),line[15],int(line[17]),int(line[18]))
			temp2=topNbaPlayerStats(topPlayersCount,float(line[5]),float(line[6]),float(line[7]),float(line[8]),float(line[9]),float(line[10]),float(line[11]),float(line[12]))
			topPlayers[topPlayersCount]=temp1
			topPlayersStats[topPlayersCount]=temp2
			topPlayersCount+=1
		else:
			if first:
				second=True
			else:
				first=True
print("Count for Top NFL Players should start here: "+str(topPlayersCount))


with open("/Users/rahulkhanna/Documents/columbia/7th/databases/project1Part3/nba/final/nbaPlayerInfo","w") as f:
	for key in players:
		f.write(str(players[key]))
		f.write("\n")

with open("/Users/rahulkhanna/Documents/columbia/7th/databases/project1Part3/nba/final/nbaTeamInfo","w") as f:
	for key in teams:
		f.write(str(teams[key]))
		f.write("\n")

with open("/Users/rahulkhanna/Documents/columbia/7th/databases/project1Part3/nba/final/nbaTopPlayersInfo","w") as f:
	for key in topPlayers:
		f.write(str(topPlayers[key]))
		f.write("\n")

with open("/Users/rahulkhanna/Documents/columbia/7th/databases/project1Part3/nba/final/nbaTopPlayersStats","w") as f:
	for key in topPlayersStats:
		f.write(str(topPlayersStats[key]))
		f.write("\n")

with open("/Users/rahulkhanna/Documents/columbia/7th/databases/project1Part3/nba/final/nbaPlayerStats","w") as f:
	for key in nbaStats:
		f.write(str(nbaStats[key]))
		f.write("\n")



