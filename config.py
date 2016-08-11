#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys

run_path = os.getcwd()
run_hostname = os.popen('hostname').read()[:-1]
run_user = os.popen('whoami').read()[:-1]
run_symbol = '#' if 'root' in run_user or 'admin' in run_user else '$'
platform = 'linux' if 'root' in run_user else "windows"

cmd_array = ['run','get','set','add','del','save','shell','exit']
set_array = []
run_array = []
configfile = ''
target = ['127.0.0.1','127.0.0.1']  #目标ip
sys_payload = ['test1','test2','test3']  #系统payload
con_payload = {'127.0.0.1':'local'}  #连接外部系统payload
shell_target = ['127.0.0.1']
thread_num = 10   #线程并发数
run_count = 10    #命令运行次数
sleep_time = 120  #运行间隔时间
write_log_allow = False #是否开启日志
