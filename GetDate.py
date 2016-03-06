#!/usr/bin/python
#coding:utf-8

import urllib
import json

old_url = "http://fanyi.youdao.com/openapi.do?keyfrom=TestByMySelf&key=2087059167&type=data&doctype=%(doctype)s&version=1.1&q=%(data)s"

def getresult(data,doctype,mode=None):
	url = old_url
	params = {
		'doctype':doctype,
		'data':data,
		'mode':mode 
	}
	if mode != None:
		url = url + "&only=%(mode)s"

#	params = urllib.urlencode(params)
	url = url % params
	html = urllib.urlopen(url)
	res = html.read()
	return res
