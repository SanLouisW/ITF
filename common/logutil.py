# -*- coding: utf-8 -*-
'''
Created on 2013-12-28

@author: lenovo
'''

import time
import sys
import os
# import term
#from termcolor import colored

def print_log(msg):
     ISOTIMEFORMAT='%Y-%m-%d %X'
     try:
         raise Exception
     except:
         f = sys.exc_info()[2].tb_frame.f_back
     #term.writeLine('[%s module:%s line:%s]' % (str(time.strftime( ISOTIMEFORMAT, time.localtime() )),
                                              #os.path.basename(f.f_code.co_filename), str(f.f_lineno))+msg,
     #           term.red)
     msg = '[%s module:%s line:%s]' % (str(time.strftime( ISOTIMEFORMAT, time.localtime() )),
                                              os.path.basename(f.f_code.co_filename), str(f.f_lineno))+str(msg)
     print str(msg).strip('')
     # term.writeLine(msg.strip(''),term.red)


def print_step(msg):
    msg = '===============' + str(msg) + '==============='
    print msg


if __name__ == '__main__':
    print_step("步骤1")
    print_log('查询不到数据')