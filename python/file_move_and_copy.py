#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 14:14:02 2019

@author: uisee
"""

import os,shutil

def mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.move(srcfile,dstfile)          #移动文件
        print("move %s -> %s"%( srcfile,dstfile))

def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print("copy %s -> %s"%( srcfile,dstfile))

#srcfile='/Users/xxx/git/project1/test.sh'
#dstfile='/Users/xxx/tmp/tmp/1/test.sh'
#mymovefile(srcfile,dstfile)
        
srcfile = '/home/uisee/tmp/Prediction/replay/Trajcase1/prepare.sh'
dstpath = '/home/uisee/tmp/Prediction/replay/Trajcase'

for i in range(1,26):
    dstfile = dstpath + str(i+1) + '/prepare.sh'
#    print(dstfile)
    mycopyfile(srcfile, dstfile)





