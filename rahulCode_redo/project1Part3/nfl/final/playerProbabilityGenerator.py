from sklearn import svm
import datetime
from datetime import date
import random
from scipy import spatial
# import numpy as np

playerPos={}

with open("nflPlayerInfo") as f:
	for line in f:
		tup=eval(line)
		playerPos[tup[0]]=tup[6]

topPlayerInfo={}
with open("nflTopPlayersInfo") as f:
	for line in f:
		tup=eval(line)
		topPlayerInfo[tup[0]]=[tup[4],tup[5],tup[6]]

allStar={
	"WR":[],
	"QB":[],
	"RB":[]
}

nonAllStar={
	"WR":[],
	"QB":[],
	"RB":[]
}

mvp={
	"WR":[],
	"QB":[],
	"RB":[]
}
nonMvp={
	"WR":[],
	"QB":[],
	"RB":[]
}
playerStats={}
with open("nflPlayerStats") as f:
	for line in f:
		tup=eval(line)
		# print(tup[2])
		# print(tup[7])
		# print(tup[9])
		# print(tup[11])
		temp=[float(tup[3])/float(tup[2]),float(tup[4])/float(tup[2]),float(tup[5])/float(tup[2]),float(tup[6])/max(float(tup[2]),1.0),float(tup[7])/max(float(tup[2]),1.0),float(tup[8])/max(float(tup[2]),1.0),float(tup[9]),float(tup[10])/float(tup[2]),float(tup[11])/float(tup[2]),float(tup[12])/float(tup[2]),float(tup[13])/float(tup[2])]
		if tup[1]==2014:
			if tup[0]==387:
				print(tup)
				print(temp)
			playerStats[tup[0]]=temp
		if tup[len(tup)-2]:
			allStar[playerPos[tup[0]]].append(temp)
		else:
			nonAllStar[playerPos[tup[0]]].append(temp)

		if tup[len(tup)-1]:
			mvp[playerPos[tup[0]]].append(temp)
		else:
			nonMvp[playerPos[tup[0]]].append(temp)

topPlayerStats={}
with open("nflTopPlayersStats") as f:
	for line in f:
		tup=eval(line)
		temp=[]
		for i in range(1,len(tup)):
			temp.append(tup[i])

		topPlayerStats[tup[0]]=temp

		if topPlayerInfo[tup[0]][1]>0:
			allStar[topPlayerInfo[tup[0]][0]].append(temp)
		else:
			nonAllStar[topPlayerInfo[tup[0]][0]].append(temp)

		if topPlayerInfo[tup[0]][2]>0:
			mvp[topPlayerInfo[tup[0]][0]].append(temp)
		else:
			nonMvp[topPlayerInfo[tup[0]][0]].append(temp)

allStarModels={
	"WR":None,
	"QB":None,
	"RB":None
}

mvpModels={
	"WR":None,
	"QB":None,
	"RB":None
}

for pos in allStarModels:
	X=[]
	y=[]
	for value in allStar[pos]:
		X.append(value)
		y.append(1)
	rand_smpl = [nonAllStar[pos][i] for i in sorted(random.sample(xrange(len(nonAllStar[pos])),len(allStar[pos])))]

	for value in rand_smpl:
		X.append(value)
		y.append(0)
	# print(X)
	# X=np.array(X)
	# y=np.array(y)
	clf=svm.SVC(probability=True)
	clf.fit(X,y)
	allStarModels[pos]=clf

for pos in mvpModels:
	X=[]
	y=[]
	for value in mvp[pos]:
		X.append(value)
		y.append(1)
	rand_smpl = [nonMvp[pos][i] for i in sorted(random.sample(xrange(len(nonMvp[pos])),len(mvp[pos])))]

	for value in rand_smpl:
		X.append(value)
		y.append(0)
	# print(X)
	# X=np.array(X)
	# y=np.array(y)
	clf=svm.SVC(probability=True)
	clf.fit(X,y)
	mvpModels[pos]=clf
probs={}
with open("probs","w") as f:
	for i in range(0,3):
		for player in playerPos:
			if player in playerStats:
				v=playerStats[player]
				amodel=allStarModels[playerPos[player]]
				mmodel=mvpModels[playerPos[player]]
				if player in probs:
					probs[player][0]+=mmodel.predict_proba(v)[0][1]
					probs[player][1]+=amodel.predict_proba(v)[0][1]
				else:
					probs[player]=[mmodel.predict_proba(v)[0][1],amodel.predict_proba(v)[0][1]]
			else:
				probs[player]=[0,0]

		if i<2:
			for pos in allStarModels:
				X=[]
				y=[]
				for value in allStar[pos]:
					X.append(value)
					y.append(1)
				rand_smpl = [nonAllStar[pos][i] for i in sorted(random.sample(xrange(len(nonAllStar[pos])),len(allStar[pos])))]

				for value in rand_smpl:
					X.append(value)
					y.append(0)
# print(X)
					# X=np.array(X)
					# y=np.array(y)
					clf=svm.SVC(probability=True)
					clf.fit(X,y)
					allStarModels[pos]=clf

			for pos in mvpModels:
				X=[]
				y=[]
				for value in mvp[pos]:
					X.append(value)
					y.append(1)
				rand_smpl = [nonMvp[pos][i] for i in sorted(random.sample(xrange(len(nonMvp[pos])),len(mvp[pos])))]

				for value in rand_smpl:
					X.append(value)
					y.append(0)
				# print(X)
				# X=np.array(X)
				# y=np.array(y)
				clf=svm.SVC(probability=True)
				clf.fit(X,y)
				mvpModels[pos]=clf

	for player in probs:
		cur=[0,0]
		if player in playerStats:
			cur=[-1,0]
			v1=playerStats[player]
			# print(v1)
			for player2 in topPlayerStats:
				# print(str(player2))
				v2=topPlayerStats[player2]
				result=1-spatial.distance.cosine(v1,v2)
				if result>cur[1]:
					cur[0]=player2
					cur[1]=result
			# print(player2)
			# break
		# break
		# 184
		temp=(player,cur[0],cur[1],(probs[player][1]/3),(probs[player][0]/4.5))
		f.write(str(temp))
		f.write("\n")