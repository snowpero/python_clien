#-*- coding: utf-8 -*-

import datetime
import json
import urllib2

from urlparse import parse_qs, urlparse
from bs4 import BeautifulSoup
from data.clien_post_data import ClienPostData

page_num = 1
img_page_num = 1

# 모바일 주소값 데이터
def getMobileData(input_url):
	parse_url = 'http://m.clien.net/cs3/board?bo_style=lists&bo_table=park&page='
	if len(input_url) > 1:
		parse_url = 'http://m.clien.net' + input_url + '&page='
	def_url_img = 'http://m.clien.net'
	def_url_post = 'http://m.clien.net/cs3/board?'

	print parse_url+str(page_num)

	page = urllib2.urlopen(parse_url+str(page_num))
	soup = BeautifulSoup(page.read(), 'html.parser')
	page.close()

	list_tit = soup.find_all('span', 'lst_tit')
	list_info = soup.find_all('span', 'lst_user')
	list_reply = soup.find_all('span', 'lst_reply')

	arrData = []
	if len(list_info) == len(list_tit):
		for i in range(len(list_tit)):
			c_post_data = ClienPostData()

			# Cell Type
			c_post_data.cell_type = 'LETTER_POST'

			cell_title = list_tit[i]
			cell_info = list_info[i]
			cell_reply = list_reply[i].text
			
			tit_parent = cell_title.parent['onclick']

			# Index
			if tit_parent.find('?') != -1:
				tempStr = tit_parent.replace("'", "")
				splitStr = tempStr.split('?')
				tempUrl = def_url_post + splitStr[1]
				cell_index = parse_qs(urlparse(tempUrl).query, keep_blank_values=True).get('wr_id')[0]
				c_post_data.index = cell_index

			# ID
			if cell_info.img != None:
				c_post_data.hasImgID = True
				c_post_data.imgUrl = def_url_img + str(cell_info.img['src'])
			else:
				c_post_data.hasImgID = False
				c_post_data.user = cell_info.text

			# Title
			c_post_data.title = cell_title.text

			# Link
			postUrl = cell_title.parent['onclick']
			if postUrl.find('?') != -1:
				tempStr = postUrl.replace("'", "")
				splitStr = tempStr.split('?')
				c_post_data.link = def_url_post + splitStr[1]

			# ReplyCount
			c_post_data.replyCount = cell_reply

			if( page_num > 1 ):
				# 두번째 페이지부터 공지사항 제외
				if( i > 2 ):
					arrData.append(c_post_data)
			else:
				arrData.append(c_post_data)

	arrRetVal = []
	for itemData in arrData:
		arrRetVal.append({
			'title' : itemData.title,
			'link' : itemData.link,
			'hasImgID' : itemData.hasImgID,
			'imgUrl' : itemData.imgUrl,
			'user' : itemData.user,
			'replyCount' : itemData.replyCount,
			'index' : itemData.index,
			'cell_type' : itemData.cell_type
			})

	return arrRetVal

# 웹페이지 데이터만 가져온다
def getWebData(input_url):
	parse_url = 'http://www.clien.net/cs2/bbs/board.php?bo_table=park&page='
	if len(input_url) > 1:
		parse_url = 'http://m.clien.net' + input_url + '&page='
	post_url = 'http://www.clien.net/cs2'

	page = urllib2.urlopen(parse_url+str(page_num))
	soup = BeautifulSoup(page.read(), 'html.parser')
	page.close()
	member_list = soup.find_all('span', 'member')

	retArr = []
	for member in member_list:
		user = member.text

		post_info = member.parent.parent
		title = post_info.a.string
		number = post_info.td.string
		link = post_info.a['href']
		link = link.replace('..', post_url)
		retArr.append({'user' : user, 
						 'title' : title,
						 'number' : number,
						 'link' : link
						})

	return retArr

# 첫 메인 페이지 데이터
def getData(input_url):
	page_num = 1
	return json.dumps( {'items' : getMobileData(input_url) }, ensure_ascii=False)

# 다음 페이지 데이터
def getNextPageData(input_url, page):
	page_num = page
	return json.dumps( {'items' : getMobileData(input_url) }, ensure_ascii=False)

def getImgPageData(input_url):
	return 'Test'

def getImgNextPageData(input_url, page):
	pass