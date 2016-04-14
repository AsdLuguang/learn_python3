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
'''
url = "http://www.baidu.com"
temp = GetHtml(url)
html = temp.decode('UTF-8');
#print(type(temp), type(html))
#print(html);
'''
f = open('baidu.html', 'r')
html = f.read()

for link, t in set(re.findall(r'(http[s]?://[^,]*?(jpg|png|gif))', str(html))):
	print(link);
	
'''
html = 'abchttp://df.jpg>caabacaccca';
print(html);
s1 = set(re.findall(r'(http:[^s]*?(jpg|png|gif))', str(html)));
for link in s1:
	print(link);
'''

