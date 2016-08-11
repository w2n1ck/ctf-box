#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import *
from sys_payload import  *
import os

# example of payload
def run(target,payload,extend):
	target = target
	payload = sys_payload_array[payload]
	cmd = extend
	return os.popen(cmd).read()