#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import json
import datetime

page = urllib2.urlopen('http://comic.naver.com/webtoon/weekday.nhn')
soup = BeautifulSoup(page.read(), 'html.parser')
page.close()
#print soup
titles = soup.find_all("a", "title")
imgs = soup.find_all('img')

strTime = "\n****** Build : "
strTime += str(datetime.datetime.now())
print strTime

retVal = ''
retArr = []

defineUrl = 'http://comic.naver.com'

#print 'Number of Title : ' + str(len(titles))
#print 'Number of Img : ' + str(len(imgs))

for title in titles:
#   print 'title:{0:10s} link:{1:20s}\n'.format(title['title'].encode('utf-8'), title['href'].encode('utf-8'))
	retVal += 'title:{0:10s} link:{1:20s}\n'.format(title['title'].encode('utf-8'), title['href'].encode('utf-8'))
	item_title = title['title'].encode('utf-8')
	item_link = title['href'].encode('utf-8')
	retArr.append({ 'title' : item_title, 
					'link' : (defineUrl + item_link)})

#print retVal

imgArr = []
for img in imgs:
	if hasattr(img, 'title'):
		imgArr.append(img['src'])

#print 'Number of ImgArr : ' + str(len(imgArr))

def getData():
	return json.dumps(retArr, ensure_ascii=False)
