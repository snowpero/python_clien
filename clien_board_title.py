#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import json
from data.clien_board_item import ClienBoardItem

def getBoardTitles():
    parse_url = 'http://m.clien.net/cs3/'

    page = urllib2.urlopen(parse_url)
    soup = BeautifulSoup(page.read(), 'html.parser')
    page.close()

    board_title = soup.find_all('ul', 'nav_snb_board')
    arr_title = board_title[0]

    arrRetVal = []
    for li in arr_title.findAll('li'):
        arrRetVal.append({
            'title' : li.a.text[1:len(li.a.text)],
            'link' : li.a['href']
        })

    return json.dumps( {'items' : arrRetVal }, ensure_ascii=False)