#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import json
from urlparse import parse_qs, urlparse
from clien_detail_data import ClienDetailData

def getPostDetailData(post_url):
	try:
		page = urllib2.urlopen(post_url)
		soup = BeautifulSoup(page.read(), 'html.parser')
		page.close()
		#print soup

		info = soup.find_all('span', 'view_info')
		info_txt = info
		title = soup.find_all('div', 'post_tit scalable')
		titleTxt = title[0].text

		post_content = soup.find_all('div', 'post_ct scalable')

		c_detail_data = ClienDetailData()
		c_detail_data.viewinfo = info_txt[0].text
		c_detail_data.title = titleTxt
		c_detail_data.text = post_content[0].text

		retVal = {
			'title' : c_detail_data.title,
			'text' : c_detail_data.text,
			'viewinfo' : c_detail_data.viewinfo
		}

		return json.dumps( { 'data' : retVal }, ensure_ascii=False )
	except:
		return "Parse Error"

def getReplyData(post_url):
	page = urllib2.urlopen(post_url)
	soup = BeautifulSoup(page.read(), 'html.parser')
	page.close()

	reply_txt = soup.find_all('div', 'reply_txt scalable')
	reply_user = soup.find_all('div', 'reply_user')
	for reply in reply_txt:
		print reply