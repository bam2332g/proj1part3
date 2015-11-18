# doesn't include last season's retired players
# doesn't include mvp or allstar stats
# gets all the actual stats for the players

import requests
import json
import random
import time

class Player():
	def __init__(self,nbaKey,name,dob,position,team):
		self.years={}
		self.key=str(nbaKey)
		self.name=str(name)
		self.dob=str(dob)
		self.team=str(team)
		self.pos=str(position)

	def addYear(self,year,dic):
		if year not in self.years:
			self.years[year]=dic
		else:
			if (self.years[year]["GP"]!=dic["GP"]) and (self.years[year]["PTS"]!=dic["PTS"]):
				for key in self.years[year]:
					self.years[year][key]+=dic[key]

	def __repr__(self):
		exp=min(len(self.years)/10.0,1.0)
		output=self.key+" | "+self.name+" | "+ self.dob+" | "+self.team+" | "+self.pos+" | "+str(exp)
		return ((output,self.years))

	def __str__(self):
		exp=min(len(self.years)/10.0,1.0)
		output=self.key+" | "+self.name+" | "+ self.dob+" | "+self.team+" | "+self.pos+" | "+str(exp)
		return str((output,self.years))

# players={}
with open('playerInfo2','w') as f2:
	with open('playerKey','r') as f1:
		count=0
		for line in f1:
			curId=line.split(" : ")[0]
			url1="http://stats.nba.com/stats/playercareerstats?LeagueID=00&PerMode=Totals&PlayerID={playerId}".format(playerId=curId)
			url2="http://stats.nba.com/stats/commonplayerinfo?LeagueID=00&PlayerID={playerId}&SeasonType=Regular+Season".format(playerId=curId)
			r2=requests.get(url2)
			if r2.status_code == requests.codes.ok:
				data=json.loads(r2.text)
				info=data["resultSets"][0]["rowSet"][0]
				t=Player(curId,info[3],info[6],info[14],info[18])

				r1=requests.get(url1)
				if r1.status_code == requests.codes.ok:
					data=json.loads(r1.text)
					for year in data["resultSets"][0]["rowSet"]:
						y=str(year[1])
						dic={
							"GP":int(year[6]),
							"FGM":int(year[9]),
							"FGA":int(year[10]),
							"3PM":int(year[12]),
							"3PA":int(year[13]),
							"FTM":int(year[15]),
							"FTA":int(year[16]),
							"REB":int(year[20]),
							"AST":int(year[21]),
							"STL":int(year[22]),
							"BLK":int(year[23]),
							"TOV":int(year[24]),
							"PTS":int(year[26])
						}
						t.addYear(y,dic)
				else:
					print("R1 " +curId+ " "+ r1.status_code)

				
				if len(t.years)>0:
					# players[curId]=t
					f2.write(str(t))
					f2.write("\n")
				print("Succesfully added: " +t.name)
				count+=1
				print(str(count/448.0))
			else:
				print("R2 "+ curId+ " "+ r2.status_code)
			if count<100:
				sleepTime=random.randint(1,6)
				print("Entering sleep")
				time.sleep(sleepTime)
				print("Sleep over")
			elif count<200:
				sleepTime=random.randint(7,12)
				print("Entering sleep")
				time.sleep(sleepTime)
				print("Sleep over")
			elif count<300:
				sleepTime=random.randint(13,18)
				print("Entering sleep")
				time.sleep(sleepTime)
				print("Sleep over")
			else:
				sleepTime=random.randint(19,21)
				print("Entering sleep")
				time.sleep(sleepTime)
				print("Sleep over")





