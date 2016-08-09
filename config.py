#!/usr/bin/env python
# -*- coding: utf-8 -*-

cmd_array = ['run','get','set','add','del','save','shell','exit']
set_array = []
run_array = []
configfile = ''
target = []  #目标ip
sys_payload = []  #系统payload
out_payload = ''  #连接外部系统payload
thread_num = 10   #线程并发数
run_count = 10    #命令运行次数
sleep_time = 120  #运行间隔时间
write_log_allow = False #是否开启日志