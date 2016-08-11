#!/usr/bin/env python
# -*- coding: utf-8 -*-

sys_payload_array = {
'test1' : 'whoami',
'test2' : 'ipconfig',
'test3' : 'dir',
"get_flag" : 'cat /home/ctf/flag;', #获取flag
"duplicate_shell" : 'cp ;' ,        #复制shell到所有目录下
"kill_process" : ';' ,              #杀掉进程
"reverse_shell" : ';'  ,            #反弹shell
"rm_file" : ';'   ,                 #文件批量删除
"daemon_process" : ';'   ,          #进程守护

 }
