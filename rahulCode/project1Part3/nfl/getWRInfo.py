import requests
from lxml import html
import xml.etree.ElementTree as ET
import random
import time

class wr():
	def __init__(self,url,name,dob,team):
		self.recievingInfo={}
		self.rushingInfo={}
		self.name=str(name)
		self.dob=str(dob)
		self.team=str(team)
		self.url=str(url)

	def addRecievingInfo(self,dic):
		self.recievingInfo=dic

	def addRushingInfo(self,dic):
		self.rushingInfo=dic

	def __repr__(self):
		exp=min(max(len(self.recievingInfo),len(self.rushingInfo))/10.0,1.0)
		# output=self.name+" | "+ self.dob+" | "+self.team+" | "+str(exp)
		output=self.url+" | "+self.name+" | "+ self.dob+" | "+self.team+" | "+str(exp)
		return ((output,self.recievingInfo,self.rushingInfo))

	def __str__(self):
		exp=min(max(len(self.recievingInfo),len(self.rushingInfo))/10.0,1.0)
		output=self.url+" | "+self.name+" | "+ self.dob+" | "+self.team+" | "+str(exp)
		# output=self.name+" | "+ self.dob+" | "+self.team+" | "+str(exp)
		return str((output,self.recievingInfo,self.rushingInfo))

# pulling qb
with open('wrInfo','a') as f1:
	with open('wrLinks','r') as f2:
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

			wideReciever=wr(url,name,dob,team)

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

						wideReciever.addRushingInfo(rushingInfo)
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
						wideReciever.addRecievingInfo(receivingInfo)
				f1.write(str(wideReciever))
				f1.write("\n")
				print("Succesfully added: " +wideReciever.name)
				print(str(count/292.0))
			else:
				print("no stats")
				print(url)

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
			else:
				sleepTime=random.randint(13,18)
				print("Entering sleep")
				time.sleep(sleepTime)
				print("Sleep over")

			count+=1



			# if len(stats)>2:
			# 	stats=[stats[1],stats[2]]
			# if len(stats)>1:
			# 	# print((stats[0].cssselect('table')[0].get('summary')).split()[0])
			# 	if stats[0].cssselect('table')[0].get('summary') == "Passing":
			# 		body=stats[0].cssselect('table')[0].cssselect('tbody')
			# 		root=ET.fromstring(html.tostring(body[0]))
			# 		passingInfo={
			# 			"Years":[],
			# 			"Games":[],
			# 			"QB Rating":[],
			# 			"Completions":[],
			# 			"Attempts":[],
			# 			"Yards":[],
			# 			"Touchdowns":[],
			# 			"Interceptions":[],
			# 			"Fumbles":[] #really a sack, or at least a proxy for sacks
			# 		}
			# 		# accessing each table row
			# 		for tr in root:
			# 			for entry in tr:
			# 				if entry.tag=="th":
			# 					if entry.attrib["class"]=="season":
			# 						passingInfo["Years"].append(entry.text)
			# 					else:
			# 						break
			# 				else:
			# 					if entry.attrib["title"] in passingInfo:
			# 						passingInfo[entry.attrib["title"]].append(entry.text)

			# 		# print(stats[1].cssselect('table')[0].get('summary').split)
			# 		if stats[1].cssselect('table')[0].get('summary') == "Rushing":
			# 			body=stats[1].cssselect('table')[0].cssselect('tbody')
			# 			root=ET.fromstring(html.tostring(body[0]))
			# 			rushingInfo={
			# 				"Years":[],
			# 				"Games":[],
			# 				"Rushes":[],
			# 				"Yards":[],
			# 				"Touchdowns":[]
			# 			}

			# 			# accessing each table row
			# 			for tr in root:
			# 				for entry in tr:
			# 					if entry.tag=="th":
			# 						if entry.attrib["class"]=="season":
			# 							rushingInfo["Years"].append(entry.text)
			# 						else:
			# 							break
			# 					else:
			# 						if entry.attrib["title"] in rushingInfo:
			# 							rushingInfo[entry.attrib["title"]].append(entry.text)
			# 			if len(passingInfo["Years"])>0 and len(rushingInfo["Years"])>0:
			# 				quarterBack.addPassingInfo(passingInfo)
			# 				quarterBack.addRushingInfo(rushingInfo)
			# 				f1.write(str(quarterBack))
			# 				f1.write("\n")
			# 				print("Succesfully added: " +quarterBack.name)
			# 				print(str(count/81.0))
			# 			else:
			# 				print("Something wrong with table parsing")
			# 				print(url)
			# 		else:
			# 			print("No Rushing Stats")
			# 			print(url)
			# 	else:
			# 		print("No Passsing Stats")
			# 		print(url)
			# else:
			# 	print("Only one table?")
			# 	print(url)