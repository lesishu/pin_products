#!/usr/bin/python
# -*- coding: UTF-8 -*-
import StringIO
import sqlite3
import urllib
import pycurl
import re
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
pinurl = 'https://api.pinterest.com/v1/pins/?access_token=' + my_token

# 指定发布Pin的 Board ID
board_id = '195765983741497086'

# 定义Pin发布函数
def Pin(pinurl,board_id,note,url,image):
	b=StringIO.StringIO()
	c=pycurl.Curl()
	c.setopt(pycurl.URL, pinurl)
	c.setopt(pycurl.WRITEFUNCTION, b.write)
	c.setopt(pycurl.FOLLOWLOCATION, 1)
	c.setopt(pycurl.MAXREDIRS, 5)
	c.setopt(pycurl.CUSTOMREQUEST,'POST')
	post_data_dic = {"board":board_id,"note":note,"link":url,"image_url":image}
	c.setopt(c.POSTFIELDS, urllib.urlencode(post_data_dic))
	c.perform()
	return c.getinfo(c.HTTP_CODE)
	#print b.getvalue()

# 连接SQLite数据库
conn = sqlite3.connect('products.sqlite')
cursor = conn.cursor()

# 从数据库中取出产品信息（默认1条；可以是多条，修改limit）
cursor.execute('select * from products where status=0 limit 0,1')
values = cursor.fetchall()

# 发送Pin
for value in values:
	pid = value[0]
	note = value[3]
	url = value[1]
	image = value[2]
	status = value[4]
	# 更新status为1，标识为已发布
	cursor.execute('update products set status=? where id=?', ('1',pid))
	conn.commit()
	# 执行发布
	pinreturn = Pin(pinurl,board_id,note,url,image)
	# 写日志，如果成功写入到succes.log
	if pinreturn == 201:
		logfile = open('succes.log','a')
		logfile.write(str(pid) + ',' + url + '\n')
		logfile.close()
	# 如果失败，写入到error.log
	else:
		logfile = open('error.log','a')
		logfile.write(str(pid) + ',' + str(pinreturn) + ',' + url + '\n')
		logfile.close()

# 关闭数据库连接
cursor.close()
conn.close()