#!/usr/bin/env python
# -*- coding: utf-8 -*-

cmd_array = ['run','get','set','add','del','save','shell','exit']
set_array = []
run_array = []
configfile = ''
target = ['127.0.0.1','192.168.1.1','127.0.0.2','127.0.0.3','127.0.0.4','127.0.0.5']  #目标ip
sys_payload = ['get_flag','duplicate_shell','get_flag2','get_flag3','get_flag4','get_flag5']  #系统payload
con_payload = {'127.0.0.1':'local'}  #连接外部系统payload
shell_target = ['127.0.0.1']
thread_num = 10   #线程并发数
run_count = 10    #命令运行次数
sleep_time = 120  #运行间隔时间
write_log_allow = False #是否开启日志
