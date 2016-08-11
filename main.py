#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
import time
from log import *
import json
from config import *
import hashlib


sys.path.append('./con_payload')


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
                if len(args)<2:
                        log('warning','缺少参数，请检查！')
                        return
                if not globals().has_key(args[0]):
                        log('warning','没有这个变量！')
                        return
                elif 'list' in str(type(globals()[args[0]])):
                        globals()[args[0]] = args[1].split(',')
                elif 'dict' in str(type(globals()[args[0]])):
                        if ',' not in args[1]:
                                log('warning','目标参数是数组，请使用,分隔之')
                                return
                        key = args[1].split(',')[0]
                        value = args[1].split(',')[1]
                        globals()[args[0]][key] = value
                        
                else:
                        globals()[args[0]] = args[1]
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
                if len(args)<2:
                        log('warning','缺少参数，请检查！')
                        return
                if 'list'  in str(type(globals()[args[0]])):
                        globals()[args[0]].append(args[1])
                elif 'dict' in str(type(globals()[args[0]])):
                        if ',' not in args[1]:
                                log('warning','目标参数是数组，请使用,分隔之')
                                return
                        key,value = args[1].split(',')
                        globals()[args[0]][key] = value
                else:
                        log('warning','添加对象只能是数组！')
                        return
                
                log('info','添加成功！')
                          
        def del_func(self,args):
                if len(args)<2:
                        log('warning','缺少参数，请检查！')
                        return
                if 'list'  in str(type(globals()[args[0]])):
                        globals()[args[0]] = [ x for x in globals()[args[0]] if x!=args[1] ]      
                elif 'dict'  in str(type(globals()[args[0]])):
                        del globals()[args[0]][args[1]]
                else:
                        log('warning','删除对象只能是数组或字典！')
                        return
                
                log('info','删除成功！')
                
        def run_func(self,args):
                if len(args)==1:
                        self.set_func(['sys_payload',args[0]])
                        
                def check_arg_generate_config():
                        config_result = '#!/usr/bin/env python\r\n'+'# -*- coding: utf-8 -*-\r\n'
                        check_array = ['target','thread_num','sys_payload','con_payload','run_count','sleep_time',
                                       'write_log_allow']
                        for var in check_array:
                                error = 0
                                if not globals().has_key(var):
                                        log('warning','缺少设置：'+var)
                                        error = 1
                                else:
                                        config_result += var+' = '+str(globals()[var])+'\r\n'
                        if error:
                                return
                        open('./tmp/config.py','w').write(config_result)

                def generate_payload_module():
                        result = '#!/usr/bin/env python\r\n'+'# -*- coding: utf-8 -*-\r\n'
                        for var in con_payload:
                                result += 'import '+con_payload[var]+'\r\n'
                        open('./tmp/payload_module.py','w').write(result)
                                
                def generate_dir():
                        dir_name = hashlib.md5(str(time.time())).hexdigest()
                        
                        linux_cmd = ['cd ./package',
                                     'mkdir '+dir_name,
                                     'cp ../sys_payload.py .',
                                     'cp ../run.py .',
                                     'cp ../tmp/config.py .',
                                     'cp ../tmp/payload_module.py .',
                                     'cp ../log.py .',
                                     ]
                        windows_cmd = [r'mkdir package\\'+dir_name,
                                     r'copy sys_payload.py package\\'+dir_name,
                                     r'copy run.py package\\'+dir_name,
                                     r'copy tmp\config.py package\\'+dir_name,
                                     r'copy tmp\payload_module.py package\\'+dir_name,
                                     r'copy log.py package\\'+dir_name
                                     ]
                        if platform=='linux':
                                cmd = linux_cmd
                        else:
                                cmd = windows_cmd

                        print cmd 
                        try:
                                print os.popen('|'.join(cmd)).read()
                                log('info','生成的运行文件在目录 '+os.getcwd()+'\package\\'+dir_name)
                        except Exception,e:
                                log('warning',e)

                check_arg_generate_config()
                generate_payload_module()
                generate_dir()
                                 
                               
        def shell_func(self,args):
                for ip in target:
                        if globals()['con_payload'].has_key(ip):
                                module = globals()['con_payload'][ip]
                                #print __import__(module).run(ip,'',' '.join(args))
                                try:
                                        print ip+' 的返回:\r\n'+__import__(module).run(ip,'',' '.join(args))
                                except Exception,e:
                                        log('warning',e)
                        else:
                                log('warning','请设置 '+ip+' 的con_payload配置！')
                                
                

        def exit_func(self,args):
                sys.exit('good bye~')

                        
cmd = cmd()
while True:
    cmdline = raw_input(run_user+'@'+run_hostname+':'+run_path+run_symbol)
    if cmdline:
                args = split_cmdline(cmdline)
                parse_cmdline(args)
                log('info',args)
    
