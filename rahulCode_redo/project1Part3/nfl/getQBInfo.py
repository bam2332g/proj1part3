import requests
from lxml import html
import xml.etree.ElementTree as ET
import random
import time

class qb():
	def __init__(self,url,name,dob,team):
		self.passingInfo={}
		self.rushingInfo={}
		self.name=str(name)
		self.dob=str(dob)
		self.team=str(team)
		self.url=str(url)

	def addPassingInfo(self,dic):
		self.passingInfo=dic

	def addRushingInfo(self,dic):
		self.rushingInfo=dic

	def __repr__(self):
		exp=min(len(set(self.passingInfo["Years"]))/10.0,1.0)
		output=self.url+" | "+self.name+" | "+ self.dob+" | "+self.team+" | "+str(exp)
		return ((output,self.passingInfo,self.rushingInfo))

	def __str__(self):
		exp=min(len(set(self.passingInfo["Years"]))/10.0,1.0)
		output=self.url+" | "self.name+" | "+ self.dob+" | "+self.team+" | "+str(exp)
		return str((output,self.passingInfo,self.rushingInfo))

# pulling qb
with open('qbInfo','w') as f1:
	with open('qbLinks','r') as f2:
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

			quarterBack=qb(url,name,dob,team)

			stats=tree.xpath('//div[@class="data-container"]')
			print(len(stats))
			if len(stats)>2:
				stats=[stats[1],stats[2]]
			if len(stats)>1:
				# print((stats[0].cssselect('table')[0].get('summary')).split()[0])
				if stats[0].cssselect('table')[0].get('summary') == "Passing":
					body=stats[0].cssselect('table')[0].cssselect('tbody')
					root=ET.fromstring(html.tostring(body[0]))
					passingInfo={
						"Years":[],
						"Games":[],
						"QB Rating":[],
						"Completions":[],
						"Attempts":[],
						"Yards":[],
						"Touchdowns":[],
						"Interceptions":[],
						"Fumbles":[] #really a sack, or at least a proxy for sacks
					}
					# accessing each table row
					for tr in root:
						for entry in tr:
							if entry.tag=="th":
								if entry.attrib["class"]=="season":
									passingInfo["Years"].append(entry.text)
								else:
									break
							else:
								if entry.attrib["title"] in passingInfo:
									passingInfo[entry.attrib["title"]].append(entry.text)

					# print(stats[1].cssselect('table')[0].get('summary').split)
					if stats[1].cssselect('table')[0].get('summary') == "Rushing":
						body=stats[1].cssselect('table')[0].cssselect('tbody')
						root=ET.fromstring(html.tostring(body[0]))
						rushingInfo={
							"Years":[],
							"Games":[],
							"Rushes":[],
							"Yards":[],
							"Touchdowns":[]
						}

						# accessing each table row
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
						if len(passingInfo["Years"])>0 and len(rushingInfo["Years"])>0:
							quarterBack.addPassingInfo(passingInfo)
							quarterBack.addRushingInfo(rushingInfo)
							f1.write(str(quarterBack))
							f1.write("\n")
							print("Succesfully added: " +quarterBack.name)
							print(str(count/81.0))
						else:
							print("Something wrong with table parsing")
							print(url)
					else:
						print("No Rushing Stats")
						print(url)
				else:
					print("No Passsing Stats")
					print(url)
			else:
				print("Only one table?")
				print(url)

			sleepTime=random.randint(1,6)
			print("Entering sleep")
			time.sleep(sleepTime)
			print("Sleep over")
			count+=1






