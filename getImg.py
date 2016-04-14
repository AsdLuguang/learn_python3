#!/usr/bin/python3

import urllib.request
import socket
import re
import sys
import os

baseDir = "/home/asd/python/aax"

def destFile(path):
	if not os.path.isdir(baseDir):
		os.mkdir(baseDir);
	pos = path.rindex('/');
	t = os.path.join(baseDir, path[pos+1:]);
	return t;

def GetHtml(url):
	webPage = urllib.request.urlopen(url);
	html = webPage.read();
	return html;

PATH_DIR = '/home/asd/python'
FILE_IMG = 'test.jpg'
IMG_URL = r'http://www.yjz9.com/uploadfile/2014/1018/20141018062027405.jpg'
#IMG_URL = 'http://www.yiibai.com/uploads/allimg/141005/0A3562145-0.jpg'
def Create_PATH():
	if not os.path.isdir(PATH_DIR):
		os.mkdir(PATH_DIR);
	t = os.path.join(PATH_DIR, FILE_IMG);
	return t;

img_dest_path = Create_PATH();
img_data = GetHtml(IMG_URL)

pf = open(img_dest_path, 'wb')
pf.write(img_data)
pf.close()
'''
url = "http://www.baidu.com"
temp = GetHtml(url)
html = temp.decode('UTF-8');
#print(type(temp), type(html))
#print(html);
'''
"""
f = open('baidu.html', 'r')
html = f.read()

for link, t in set(re.findall(r'(http[s]?://[^,]*?(jpg|png|gif))', str(html))):
	print(link);
"""	
'''
html = 'abchttp://df.jpg>caabacaccca';
print(html);
s1 = set(re.findall(r'(http:[^s]*?(jpg|png|gif))', str(html)));
for link in s1:
	print(link);
'''

