#-*- coding: utf-8 -*-

import datetime
import json
import urllib2

from urlparse import parse_qs, urlparse
from bs4 import BeautifulSoup
from data.clien_post_data import ClienPostData
from data.clien_img_post_data import ClienImgPostData

page_num = 1

def getData(input_url):
	parse_url = 'http://m.clien.net/cs3/board?bo_style=lists&bo_table=park&page='
	if len(input_url) > 1:
		parse_url = 'http://m.clien.net' + input_url + '&page='
	def_url_img = 'http://m.clien.net'
	def_url_post = 'http://m.clien.net/cs3/board?'

	print parse_url+str(page_num)

	page = urllib2.urlopen(parse_url+str(page_num))
	soup = BeautifulSoup(page.read(), 'html.parser')
	page.close()

	# print soup

	list_photo_hd = soup.find_all('div', 'photo_hd')
	list_photo_img = soup.find_all('div', 'photo_img')
	list_photo_ct = soup.find_all('div', 'photo_ct')

	size = len(list_photo_hd)

	arrData = []
	if( len(list_photo_hd) == len(list_photo_img) ):
		for i in range(size) :
			c_image_post_data = ClienImgPostData()

			# Cell Type
			c_image_post_data.cell_type = 'IMAGE_POST'

			cell_hd = list_photo_hd[i]
			cell_img = list_photo_img[i]
			cell_ct = list_photo_ct[i]

			# Category
			c_image_post_data.category = cell_hd.find('span', 'photo_category').text

			# Title
			c_image_post_data.title = cell_hd.find('span', 'photo_tit scalable').text

			# Reply Count
			c_image_post_data.replyCount = cell_hd.find('span', 'photo_reply').text

			# Image Url			
			c_image_post_data.imgUrl = cell_img.img['src']

			# Link
			str_link = cell_img.a['href']
			c_image_post_data.link = str_link
			tmpUrl = def_url_img
			if( str_link.find('?') != -1 ):
				tmpUrl += '?'
				tmpUrl += str_link
			else:
				tmpUrl += str_link

			str_index = parse_qs(urlparse(tmpUrl).query, keep_blank_values=True).get('wr_id')[0]
			c_image_post_data.index = str_index

			# ID
			if cell_ct.find('span', 'photo_user').img != None:
				c_image_post_data.hasImgID = True
				str_id_img = cell_ct.find('span', 'photo_user').img['src']
				c_image_post_data.imgIdUrl = str_id_img
			else:
				c_image_post_data.hasImgID = False
				str_user = cell_ct.find('span', 'photo_user').text
				c_image_post_data.user = str_user

			# Time
			c_image_post_data.time = cell_ct.find('span', 'photo_time').text

			# Message
			c_image_post_data.message = cell_ct.find('span', 'photo_desc scalable').text

			# c_image_post_data.

			arrData.append(c_image_post_data)


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
			'imgIdUrl' : itemData.imgIdUrl,
			'message' : itemData.message,
			'category' : itemData.category,
			'time' : itemData.time,
			'cell_type' : itemData.cell_type
			})

	return arrRetVal

def getImgPageData(input_url):
	page_num = 1
	return json.dumps( {'items' : getData(input_url) }, ensure_ascii=False)

def getImgNextPageData(input_url, page):
	page_num = page
	return json.dumps( {'items' : getData(input_url) }, ensure_ascii=False)