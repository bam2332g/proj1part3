# getting a sample of data to parse for the keys of the players
import requests
import xml.etree.ElementTree as ET

currentPlayerInfoUrl="http://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=1&LeagueID=00&Season=2015-16"

r=requests.get(currentPlayerInfoUrl)
if r.status_code == requests.codes.ok:
	with open('currentPlayerDump.json','w') as f:
		for line in r.text:
			f.write(line)

