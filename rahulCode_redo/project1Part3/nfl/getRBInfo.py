import requests
from lxml import html
import xml.etree.ElementTree as ET
import random
import time

class rb():
	def __init__(self,url,name,dob,team):
		self.recievingInfo={}
		self.rushingInfo={}
		self.name=str(name)
		self.dob=str(dob)
		self.team=str(team)
		self.url=str(url)

	def addRecievingInfo(self,dic):
		self.recievingInfo=dic

	def addRushingInfo(self,dic):c
		self.rushingInfo=dic

	def __repr__(self):
		exp=min(max(len(self.recievingInfo),len(self.rushingInfo))/10.0,1.0)
		output=self.url+" | "+self.name+" | "+ self.dob+" | "+self.team+" | "+str(exp)
		return ((output,self.recievingInfo,self.rushingInfo))

	def __str__(self):
		exp=min(max(len(self.recievingInfo),len(self.rushingInfo))/10.0,1.0)
		output=self.url+" | "+self.name+" | "+ self.dob+" | "+self.team+" | "+str(exp)
		return str((output,self.recievingInfo,self.rushingInfo))

# pulling qb
with open('rbInfo','w') as f1:
	with open('rbLinks','r') as f2:
		count=1
		for line in f2:
			url='http://sports.yahoo.com'+line
			r=requests.get(url)
			tree = html.fromstring(r.content)

			nameAndTeam=tree.xpath('//div[@class="player-info"]')
			name=str(nameAndTeam[0].cssselect('h1')[0].get('data-name'))
			team=str(nameAndTeam[0].cssselect('a')[0].get('title'))
			dob=tree.xpath('//li[@class="born"]')
			dob=str(dob[0].cssselect('dd')[0].text_content())

			runningBack=rb(url,name,dob,team)

			stats=tree.xpath('//div[@class="data-container"]')
			newStats={}
			for i in range(0,len(stats)):
				if stats[i].cssselect('table')[0].get('summary')=="Rushing" or stats[i].cssselect('table')[0].get('summary')=="Receiving":
					newStats[stats[i].cssselect('table')[0].get('summary')]=stats[i]

			if len(newStats)>0:
				for stat in newStats:
					if stat=="Rushing":
						body=newStats[stat].cssselect('table')[0].cssselect('tbody')
						root=ET.fromstring(html.tostring(body[0]))
						rushingInfo={
							"Years":[],
							"Games":[],
							"Rushes":[],
							"Yards":[],
							"Touchdowns":[]
						}
						for tr in root:
							for entry in tr:
								if entry.tag=="th":
									if entry.attrib["class"]=="season":
										rushingInfo["Years"].append(entry.text)
									else:
										break
								else:
									if entry.attrib["title"] in rushingInfo:
										rushingInfo[entry.attrib["title"]].append(entry.text)

						runningBack.addRushingInfo(rushingInfo)
					else:
						body=newStats[stat].cssselect('table')[0].cssselect('tbody')
						root=ET.fromstring(html.tostring(body[0]))
						receivingInfo={
							"Years":[],
							"Games":[],
							"Receptions":[],
							"Yards":[],
							"Touchdowns":[]
						}
						for tr in root:
							for entry in tr:
								if entry.tag=="th":
									if entry.attrib["class"]=="season":
										receivingInfo["Years"].append(entry.text)
									else:
										break
								else:
									if entry.attrib["title"] in receivingInfo:
										receivingInfo[entry.attrib["title"]].append(entry.text)
						runningBack.addRecievingInfo(receivingInfo)
				f1.write(str(runningBack))
				f1.write("\n")
				print("Succesfully added: " +runningBack.name)
				print(str(count/139.0))
			else:
				print("no stats")
				print(url)

			if count<100:
				sleepTime=random.randint(1,6)
				print("Entering sleep")
				time.sleep(sleepTime)
				print("Sleep over")
			else:
				sleepTime=random.randint(7,12)
				print("Entering sleep")
				time.sleep(sleepTime)
				print("Sleep over")

			count+=1