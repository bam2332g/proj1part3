import requests
from lxml import html

with open('qbLinks','w') as f:
	url= "http://sports.yahoo.com/nfl/players?type=position&c=NFL&pos=QB"
	r=requests.get(url)

	tree = html.fromstring(r.content)

	oneHalf=tree.xpath('//tr[@class="ysprow1"]')
	secondHalf=tree.xpath('//tr[@class="ysprow2"]')

	for element in oneHalf:
		temp=element[0].cssselect('a')[0].get('href')
		f.write(temp)
		f.write("\n")

	for element in secondHalf:
		temp=element[0].cssselect('a')[0].get('href')
		f.write(temp)
		f.write("\n")

with open('rbLinks','w') as f:
	url= "http://sports.yahoo.com/nfl/players?type=position&c=NFL&pos=RB"
	r=requests.get(url)

	tree = html.fromstring(r.content)

	oneHalf=tree.xpath('//tr[@class="ysprow1"]')
	secondHalf=tree.xpath('//tr[@class="ysprow2"]')

	for element in oneHalf:
		temp=element[0].cssselect('a')[0].get('href')
		f.write(temp)
		f.write("\n")

	for element in secondHalf:
		temp=element[0].cssselect('a')[0].get('href')
		f.write(temp)
		f.write("\n")

with open('wrLinks','w') as f:
	url= "http://sports.yahoo.com/nfl/players?type=position&c=NFL&pos=WR"
	r=requests.get(url)

	tree = html.fromstring(r.content)

	oneHalf=tree.xpath('//tr[@class="ysprow1"]')
	secondHalf=tree.xpath('//tr[@class="ysprow2"]')

	for element in oneHalf:
		temp=element[0].cssselect('a')[0].get('href')
		f.write(temp)
		f.write("\n")

	for element in secondHalf:
		temp=element[0].cssselect('a')[0].get('href')
		f.write(temp)
		f.write("\n")

	url= "http://sports.yahoo.com/nfl/players?type=position&c=NFL&pos=TE"
	r=requests.get(url)

	tree = html.fromstring(r.content)

	oneHalf=tree.xpath('//tr[@class="ysprow1"]')
	secondHalf=tree.xpath('//tr[@class="ysprow2"]')

	for element in oneHalf:
		temp=element[0].cssselect('a')[0].get('href')
		f.write(temp)
		f.write("\n")

	for element in secondHalf:
		temp=element[0].cssselect('a')[0].get('href')
		f.write(temp)
		f.write("\n")

