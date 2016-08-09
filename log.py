#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from config import *

def log(type,msg):
    #output to the logfile:
    if write_log_allow:
        #should here be any lock?
        if type<>'error':
            with open(info_log,'a') as f:
                f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+":"+msg+'\n')
        else:
            with open(error_log,'a') as f:
                f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+":"+msg+'\n')
    #output to the terminal
    if type=='info':
        print("[*]\033[32m%s\033[0m: \033[32m%s\033[0m" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg))
    elif type=='warning':
        print("[*]\033[32m%s\033[0m: \033[33m%s\033[0m" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg))
    elif type=='error':
        print("[!]\033[32m%s\033[0m: \033[31m%s\033[0m" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg))
        exit('[!]engaged with fatal error,exit')
