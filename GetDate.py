#!/usr/bin/python
#coding:utf-8

import urllib

old_url = "http://fanyi.youdao.com/openapi.do?keyfrom=TestByMySelf&key=2087059167&type=data&doctype=%(doctype)s&version=1.1&q=%(data)s"

def getResult(data,doctype,mode=None):
	url = old_url
	params = {
		'doctype':doctype,
		'data':data,
		'mode':mode 
	}
	if mode != None:
		url = url + "&only=%(mode)s"

	url = url % params #Construct the URL with params
	try:
		html = urllib.urlopen(url)
		res = html.read()
	except IOError:
		res = None
	return res
