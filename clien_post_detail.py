#-*- coding: utf-8 -*-

import json
import urllib2

from bs4 import BeautifulSoup
from data.clien_detail_data import ClienDetailData


def getPostDetailData(post_url):
	page = urllib2.urlopen(post_url)
	soup = BeautifulSoup(page.read(), 'html.parser')
	page.close()
	#print soup

	info = soup.find_all('span', 'view_info')
	info_txt = info
	print info_txt[0].text
	title = soup.find_all('div', 'post_tit scalable')
	print title[0].string

	post_content = soup.find_all('div', 'post_ct scalable')
	print post_content[0].text

	#for item in post_content[0].a.next_siblings:
	#	if isinstance(item, Tag):			
	#		print item

	c_detail_data = ClienDetailData()
	c_detail_data.viewinfo = info_txt[0].text
	c_detail_data.title = title[0].text
	c_detail_data.text = post_content[0].text

	retVal = {
		'title' : c_detail_data.title,
		'text' : c_detail_data.text,
		'viewinfo' : c_detail_data.viewinfo
	}
	print retVal

	return json.dumps( retVal, ensure_ascii=False )


def getReplyData(post_url):
	page = urllib2.urlopen(post_url)
	soup = BeautifulSoup(page.read(), 'html.parser')
	page.close()

	reply_txt = soup.find_all('div', 'reply_txt scalable')
	reply_user = soup.find_all('span', 'reply_user')
	reply_date = soup.find_all('span', 'reply_date')

	for i in range(len(reply_txt)):
		print reply_txt[i].text
		print reply_user[i]