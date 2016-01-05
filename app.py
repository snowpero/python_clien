#!flask/bin/python
import clien_park
import clien_post_detail
import naver_webtoon
from flask import Flask, jsonify, make_response, request
from urlparse import parse_qs, urlparse
from urllib import quote, unquote

app = Flask(__name__)

@app.route('/')
def index():
    return clien_park.getData()

@app.route('/clien', methods=['GET'])
def get_clien():
    return clien_park.getData()

@app.route('/clien/next', methods=['GET'])
def get_next_clien():
	return clien_park.getNextPageData()

@app.route('/webtoon', methods=['GET'])
def get_webtoon():
    return naver_webtoon.getData()

@app.route('/detail', methods=['GET'])
def get_detail():
	parse = parse_qs(urlparse(request.url).query.encode('utf-8'), keep_blank_values=True)
	post_url =  parse.get('url')[0]
    #    return post_url
	return clien_post_detail.getPostDetailData(post_url)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)