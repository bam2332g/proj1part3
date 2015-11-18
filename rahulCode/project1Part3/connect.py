import psycopg2
import sys
import datetime
from datetime import date

psd=sys.argv[1]
option=int(sys.argv[2])
try:
	conn=psycopg2.connect(database="proj1part2",user="rk2658",password=psd,host="w4111db1.cloudapp.net")
	conn.autocommit = True
except:
	print "I am unable to connect"

cur=conn.cursor()
# stmt="SELECT * FROM sportsleague"
if option==1:
	print("hi")
	stmt="INSERT INTO sportsleague (leagueID,name,avgYrsOfExp,numOfPlyrOnTeam,avgAgeOfPlyr,avgAgeOfTeam,avgWinPct) VALUES (%s,%s,%s,%s,%s,%s,%s)"
	data=(1,'NBA',5.3,15,27.68,27.62,0.494)
	try:
		cur.execute(stmt,data)
	except:
		print "I didn't work"

	stmt="INSERT INTO team (teamID,name,leagueID,ties,wins,losses,numberofchampionships) VALUES (%s,%s,%s,%s,%s,%s,%s)"
	data=[]
	with open("/home/azureuser/project/nba/final/nbaTeamInfo","r") as f:
		for line in f:
			data.append(eval(line))
	# print(data[0])
	try:
		cur.executemany(stmt,data)
	except:
		print "I didn't work"

	stmt="INSERT INTO player (playerid,leagueid,teamid,name,dateofbirth,expinleague,position,numberofchampionships) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
	data=[]
	with open("/home/azureuser/project/nba/final/nbaPlayerInfo","r") as f:
		for line in f:
			data.append(eval(line))
		print(data[0])
	try:
		cur.executemany(stmt,data)
	except:
		print "I didn't work"

	stmt="INSERT INTO nbaplayerstats (playerid,year,games,turnovers,steals,blks,pts,fgm,fga,tpm,tpa,ftm,fta,rebs,assists,allstar,mvp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	data=[]
	with open("/home/azureuser/project/nba/final/nbaPlayerStats","r") as f:
		for line in f:
			data.append(eval(line))
		print(data[0])
	for d in data:
		try:
			if d[1]>=2005:
				cur.execute(stmt,d)
		except:
			print "I didn't work"
			print(d)
			break

	stmt="INSERT INTO topplayer (topplayerid,leagueid,name,numOfChamps,position,numofallstar,numofmvp) VALUES (%s,%s,%s,%s,%s,%s,%s)"
	data=[]
	with open("/home/azureuser/project/nba/final/nbaTopPlayersInfo","r") as f:
		for line in f:
			data.append(eval(line))
		print(data[0])
	for d in data:
		try:
			cur.execute(stmt,d)
		except:
			print "I didn't work"
			print(d)
			break

	stmt="INSERT INTO topnbaplayerstats (topplayerid,stlpg,blkpg,ppg,fgpg,tppg,ftpg,rbspg,astpg) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	data=[]
	with open("/home/azureuser/project/nba/final/nbaTopPlayersStats","r") as f:
		for line in f:
			data.append(eval(line))
		print(data[0])
	for d in data:
		try:
			cur.execute(stmt,d)
		except:
			print "I didn't work"
			print(d)
			break

	stmt="INSERT INTO predictions (playerid,topplayerid,similarityScore,probofallstar,probofmvp) VALUES (%s,%s,%s,%s,%s)"
	data=[]
	with open("/home/azureuser/project/nba/final/probs","r") as f:
		for line in f:
			data.append(eval(line))
		print(data[0])
	for d in data:
		try:
			cur.execute(stmt,d)
		except:
			print "I didn't work"
			print(d)
			break

else:
	stmt="INSERT INTO sportsleague (leagueID,name,avgYrsOfExp,numOfPlyrOnTeam,avgAgeOfPlyr,avgAgeOfTeam,avgWinPct) VALUES (%s,%s,%s,%s,%s,%s,%s)"
	data=(0,'NFL',5.06,53,27.01,27.02,0.501)
	try:
		cur.execute(stmt,data)
	except:
		print "I didn't work"

	stmt="INSERT INTO team (teamID,name,leagueID,ties,wins,losses,numberofchampionships) VALUES (%s,%s,%s,%s,%s,%s,%s)"
	data=[]
	with open("/home/azureuser/project/nfl/final/nflTeamInfo","r") as f:
		for line in f:
			data.append(eval(line))
	# print(data[0])
	try:
		cur.executemany(stmt,data)
	except:
		print "I didn't work"

	stmt="INSERT INTO player (playerid,leagueid,teamid,name,dateofbirth,expinleague,position,numberofchampionships) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
	data=[]
	with open("/home/azureuser/project/nfl/final/nflPlayerInfo","r") as f:
		for line in f:
			data.append(eval(line))
		print(data[0])
	try:
		cur.executemany(stmt,data)
	except:
		print "I didn't work"

	stmt="INSERT INTO nflplayerstats (playerid,year,games,qbYards,qbInter,qbSacks,qbCompl,qbAtt,qbRating,rushingAtt,rushingYds,receptions,receivingYds,td,probowl,mvp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	data=[]
	with open("/home/azureuser/project/nfl/final/nflPlayerStats","r") as f:
		for line in f:
			data.append(eval(line))
		print(data[0])
	for d in data:
		try:
			cur.execute(stmt,d)
		except:
			print "I didn't work"
			print(d)
			break

	stmt="INSERT INTO topplayer (topplayerid,leagueid,name,numOfChamps,position,numofallstar,numofmvp) VALUES (%s,%s,%s,%s,%s,%s,%s)"
	data=[]
	with open("/home/azureuser/project/nfl/final/nflTopPlayersInfo","r") as f:
		for line in f:
			data.append(eval(line))
		print(data[0])
	for d in data:
		try:
			cur.execute(stmt,d)
		except:
			print "I didn't work"
			print(d)
			break

	stmt="INSERT INTO topnflplayerstats (topplayerid,qbYards,qbInter,qbSacks,qbCompl,qbAtt,qbRating,rushingAtt,rushingYds,receptions,receivingYds,td) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	data=[]
	with open("/home/azureuser/project/nfl/final/nflTopPlayersStats","r") as f:
		for line in f:
			data.append(eval(line))
		print(data[0])
	for d in data:
		try:
			cur.execute(stmt,d)
		except:
			print "I didn't work"
			print sys.exc_info()[0]
			print(d)
			break

	stmt="INSERT INTO predictions (playerid,topplayerid,similarityScore,probofallstar,probofmvp) VALUES (%s,%s,%s,%s,%s)"
	data=[]
	with open("/home/azureuser/project/nfl/final/probs","r") as f:
		for line in f:
			data.append(eval(line))
		print(data[0])
	for d in data:
		try:
			cur.execute(stmt,d)
		except:
			print "I didn't work"
			print(d)
			break