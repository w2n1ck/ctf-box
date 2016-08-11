#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__('sys').path.append('../../con_payload')
from config import *
from sys_payload import *
#import payload #test
import payload_module
from log import *
import threading
import Queue
import time



class RunPayload(threading.Thread):
    """This mainly designed for ctf-box"""
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        
        
    def run(self):
            log('info',self.getName()+' starts')
            while True:
                    if self.queue.empty():
                            break
                            
                    else:
                            [self.target,self.payload]=self.queue.get().split('||')
                    if not con_payload.has_key(self.target):
                        log('warning','没有对应的con_payload！')
                        continue
                    try:
                        self.result = __import__(con_payload[self.target]).run(self.target,self.payload,'自定义参数')       
                    except Exception,e:
                        log('warning',e)
                        self.result = 'error'
                    log('info','Run '+self.payload+' on '+self.target+' results: '+self.result)
    
    
        

def thread_ctrl(thread_num):
    #init the queue
    queue = Queue.Queue(1000)
    for payload in sys_payload:
        for ip in target:
            queue.put(ip+"||"+payload)
    #start the  threads
    threads = []
    for i in range(thread_num):
        t = RunPayload(queue)
        t.start()
        time.sleep(3)
        threads.append(t)
    for t in threads:
        t.join()
        pass


if __name__ == '__main__':
    log('info','start the exploit')
    for x in xrange(run_count):
        log('info','start round '+str(x))
        thread_ctrl(thread_num)
        time.sleep(sleep_time)
