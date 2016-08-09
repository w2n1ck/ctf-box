#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
import time
from log import *
import json
from config import *

run_path = os.getcwd()
run_hostname = os.popen('hostname').read()[:-1]
run_user = os.popen('whoami').read()[:-1]
run_symbol = '#' if 'root' in run_user or 'admin' in run_user else '$'


def split_cmdline(cmdline):
        args = cmdline.split(' ')
        return [arg for arg in args if arg]
        

def parse_cmdline(args):
        if args[0] in cmd_array:
                func = getattr(cmd,args[0]+'_func')
                func(args[1:])
        else:
                log('warning','未知变量！')

class cmd():
        def get_func(self,args):
                if not args:
                        print globals()
                        return
                elif not globals().has_key(args[0]):
                        log('warning','没有这个变量！')
                else:
                        log('info',str(args[0])+' is: '+str(globals()[args[0]]))
                
      
                        
        def set_func(self,args):
                if not globals().has_key(args[0]):
                        log('warning','没有这个变量！')
                        return
                if len(args)<2:
                        log('warning','缺少参数，请检查！')
                        return
                elif not 'list' in str(type(globals()[args[0]])):
                        globals()[args[0]] = args[1]
                else:
                        globals()[args[0]] = args[1].split(',')
                log('info','设置成功！')

                if args[0]=='configfile':
                        try:
                                configs = json.loads(open('./tmp/'+args[1]+'.json').read())
                                #print configs
                                for configname in configs:
                                        log('info','import variable: '+configname)
                                        globals()[configname] = configs[configname]
                        except Exception,e:
                                print e
                                log('warning','无效文件！')
                        
                        
                                
                        
                
        def save_func(self,args):
                result = '[configfile]\r\n'
                json_result = {}
                for var in globals():
                        if 'str' in str(type(globals()[var])) or 'int' in str(type(globals()[var])) and var!='configfile':
                                result += var+'="'+str(globals()[var])+'"\r\n'
                                json_result[var] = globals()[var]
                        elif 'list' in str(type(globals()[var])):
                                result += var+'='+str(globals()[var])+'\r\n'
                                json_result[var] = globals()[var]
                if args:
                        f = open('./tmp/'+args[0]+'.txt','w')
                        f2 =open('./tmp/'+args[0]+'.json','w')
                else:
                        f=open('./tmp/'+'tmp.txt','w')
                        f2 =open('./tmp/'+'tmp.json','w')
                f.write(result)
                f2.write(json.dumps(json_result))
                f.close()
                f2.close()
                log('info','保存成功！')
                                  

                
        def add_func(self,args):
                if 'list' not in str(type(globals()[args[0]])):
                        log('warning','添加对象只能是数组！')
                        return
                if len(args)<2:
                        log('warning','缺少参数，请检查！')
                globals()[args[0]].append(args[1])
                log('info','添加成功！')
                          
        def del_func(self,args):
                if 'list' not in str(type(globals()[args[0]])):
                        log('warning','添加对象只能是数组！')
                        return
                if len(args)<2:
                        log('warning','缺少参数，请检查！')
                globals()[args[0]] = [ x for x in globals()[args[0]] if x!=args[1] ]
                log('info','删除成功！')
                
        def run_func(self,args):
                pass

        def shell_func(self,args):
                print os.popen(' '.join(args)).read()

        def exit_func(self,args):
                sys.exit('good bye~')

                        
cmd = cmd()
while True:
    cmdline = raw_input(run_user+'@'+run_hostname+':'+run_path+run_symbol)
    if cmdline:
                args = split_cmdline(cmdline)
                parse_cmdline(args)
                log('info',args)
    
