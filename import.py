#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sqlite3
import os
import re
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 创建SQLite数据库连接
conn = sqlite3.connect('products.sqlite')
cursor = conn.cursor()

# 遍历CSV目录，获取CSV文件，创建文件列表
csvfiles = []
for csvfile in os.listdir('products_csv/'):
	if csvfile[0] == '.':
		pass
	else:
		csvfiles.append(csvfile)

# 逐一导入CSV文件内容到SQLite数据库
if csvfiles:
	for csvfile in csvfiles:
		print 'Importing', csvfile
		with open('products_csv/' + csvfile,'r') as csvtext:
			lines = csv.reader(csvtext)
			i = 0
			for line in lines:
				i += 1
				url = line[0]
				image = line[1]
				note = line[2]
				sql = 'INSERT INTO products(url,image,note) VALUES("%s","%s","%s");' % (url,image,note)
				try:
					cursor.execute(sql)
					conn.commit()
				except:
					conn.rollback()
		# 导入完成删除CSV文件
		os.remove('products_csv/' + csvfile)
		print ' |- Importe', i, 'products'

# 关闭SQLite数据库连接
cursor.close()
conn.close()