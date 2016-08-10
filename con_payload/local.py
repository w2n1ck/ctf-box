#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import *
from sys_payload import  *
import os

# example of payload
def run(target,payload,extend):
	cmd = extend
	return os.popen(cmd).read()