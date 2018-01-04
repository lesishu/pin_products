#!/usr/bin/python
# -*- coding: UTF-8 -*-
import StringIO
import urllib
import pycurl
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 读tocken文件获取用户Tocken
token_file = open('tocken')
try:
	my_token = token_file.read().strip()
finally:
	token_file.close()
# 组合 API URL
pinurl = 'https://api.pinterest.com/v1/me/boards/?access_token=' + my_token

# 定义请求函数
def Pin(pinurl):
	b=StringIO.StringIO()
	c=pycurl.Curl()
	c.setopt(pycurl.URL, pinurl)
	c.setopt(pycurl.WRITEFUNCTION, b.write)
	c.setopt(pycurl.FOLLOWLOCATION, 1)
	c.setopt(pycurl.MAXREDIRS, 5)
	c.setopt(pycurl.CUSTOMREQUEST,'GET')
	c.perform()
	return b.getvalue()

# 返回值转换JSON
pinjson = json.loads(Pin(pinurl))

# 循环输出Boards
for x in xrange(0,len(pinjson['data'])):
	print pinjson['data'][x]['id']
	print pinjson['data'][x]['name']
	print pinjson['data'][x]['url']
	print '-' * 18

