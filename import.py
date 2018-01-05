#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sqlite3
import os
import re
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

conn = sqlite3.connect('products.sqlite')
cursor = conn.cursor()

exit(0)

# 遍历CSV目录，获取CSV文件，创建文件列表
csvfiles = []
for csvfile in os.listdir('products_csv/'):
	if csvfile[0] == '.':
		pass
	else:
		csvfiles.append(csvfile)

for csvfile in csvfiles:
	print csvfile
	with open('products_csv/' + csvfile,'r') as csvtext:
		lines = csv.reader(csvtext)
		for line in lines:
			url = line[0]
			image = line[1]
			text = line[2]
			print url
			print image
			print text