#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import *
from sys_payload import all *

# example of payload
import request

def run(target,payload,extend):
	target = target
	payload = sys_payload[payload]
	url = 'http://'+target+'/index.php?cmd='+payload
	t = request(url)
	return t.text
