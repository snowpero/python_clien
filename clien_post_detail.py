#-*- coding: utf-8 -*-
import json
import urllib2

from bs4 import BeautifulSoup
from data.clien_detail_data import ClienDetailData
from data.clien_detail_reply_item import ClienDetailReplyItem

def getPostDetailData(post_url):
	page = urllib2.urlopen(post_url)
	soup = BeautifulSoup(page)
	page.close()
	# print soup

	def_url_img = 'http://m.clien.net'

	info = soup.findAll('span', 'view_info')
	info_txt = info
	# print info_txt[0].text
	title = soup.findAll('div', 'post_tit scalable')
	# print title[0].string

	post_content = soup.findAll('div', 'post_ct scalable')
	# print post_content[0].text

	signature = soup.findAll('p', 'signature_txt scalable')
	# print signature[0].text

	reply_list = soup.findAll('div', {'class', 'reply', 'reply_add'})
	# print 'reply_list length : ' + str(len(reply_list))

	c_detail_data = ClienDetailData()
	c_detail_data.viewinfo = info_txt[0].text
	c_detail_data.title = title[0].text
	c_detail_data.text = post_content[0].text
	if( len(signature) > 0 ) :
		c_detail_data.signature = signature[0].text
	else :
		c_detail_data.signature = ''

	count = 0
	if( len(reply_list) > 0 ) :
		for reply_item in reply_list:
			itemData = ClienDetailReplyItem()			
			itemData.text = reply_item.findAll('div', 'reply_txt scalable')[0].text
			itemData.date = reply_item.findAll('span', 'reply_date')[0].text
			isAddReply = False
			if( str(reply_item).find('reply_add') != -1 ) :
				isAddReply = True
			itemData.isAddReply = isAddReply
			count = count+1			

			reply_name = reply_item.findAll('span', 'reply_user')[0]
			if( reply_name.img != None ) :
				itemData.hasImgId = True
				itemData.imgUrl = def_url_img + str(reply_name.img['src'])
			else :
				itemData.hasImgId = False
				itemData.user = reply_name.text

			json_reply = {
				'text' : itemData.text,
				'date' : itemData.date,
				'isAddReply' : itemData.isAddReply,
				'hasImgId' : itemData.hasImgId,
				'imgUrl' : itemData.imgUrl,
				'userId' : itemData.user
			}
			c_detail_data.arrReplyList.append(json_reply)

	# print 'Add Item Count : ' + str(len(c_detail_data.arrReplyList))

	#for item in post_content[0].a.next_siblings:
	#	if isinstance(item, Tag):			
	#		print item

	retVal = {
		'title' : c_detail_data.title,
		'text' : c_detail_data.text,
		'viewinfo' : c_detail_data.viewinfo,
		'signature' : c_detail_data.signature,
		'reply_items' : c_detail_data.arrReplyList
	}
	# print retVal

	return json.dumps( {'data' : retVal}, ensure_ascii=False )


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