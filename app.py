#!flask/bin/python
import clien_park
import clien_post_detail
import clien_board_title
import clien_image_board
# import naver_webtoon
from flask import Flask, jsonify, make_response, request
from urlparse import parse_qs, urlparse
from urllib import quote, unquote

app = Flask(__name__)

@app.route('/')
def index():
    return 'TEST'

@app.route('/clien', methods=['GET'])
def get_clien():
    parse = parse_qs(urlparse(request.url).query.encode('utf-8'), keep_blank_values=True)
    detail_url = ''
    if len(parse) > 0:
        detail_url = parse.get('url')[0]
        detail_url = unquote(detail_url).decode('utf-8')
    return clien_park.getData(detail_url)

@app.route('/clien/next/<page>', methods=['GET'])
def get_next_clien(page):
    parse = parse_qs(urlparse(request.url).query.encode('utf-8'), keep_blank_values=True)
    detail_url = ''
    if len(parse) > 0:
        detail_url = parse.get('url')[0]
        detail_url = unquote(detail_url).decode('utf-8')
    return clien_park.getNextPageData(detail_url, page)

@app.route('/clien_img/', methods=['GET'])
def get_clien_img():
    parse = parse_qs(urlparse(request.url).query.encode('utf-8'), keep_blank_values=True)
    detail_url = ''
    if len(parse) > 0:
        detail_url = parse.get('url')[0]
        detail_url = unquote(detail_url).decode('utf-8')
    return clien_image_board.getImgPageData(detail_url)

@app.route('/clien_img_next/<page>', methods=['GET'])
def get_clien_img_next(page):
    parse = parse_qs(urlparse(request.url).query.encode('utf-8'), keep_blank_values=True)
    detail_url = ''
    if len(parse) > 0:
        detail_url = parse.get('url')[0]
        detail_url = unquote(detail_url).decode('utf-8')
    return clien_image_board.getImgNextPageData(detail_url, page)

@app.route('/detail', methods=['GET'])
def get_detail():
	parse = parse_qs(urlparse(request.url).query.encode('utf-8'), keep_blank_values=True)
	detail_url = parse.get('url')[0]
	return clien_post_detail.getPostDetailData(detail_url)

@app.route('/tabs', methods=['GET'])
def get_title():
	return clien_board_title.getBoardTitles()

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Test Code
# clien_board_title.getBoardTitles()

if __name__ == '__main__':
    app.run(debug=True)