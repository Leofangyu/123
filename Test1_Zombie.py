# -*- coding:utf-8 -*-
from multiprocessing import Process, Pool
import os
import time


def run_proc(wTime):
    n = 0
    while n < 3:
        print "subProcess %s run," % os.getpid(), "{0}".format(time.ctime())    #获取当前进程号和正在运行是的时间
        time.sleep(wTime)    #等待（休眠）
        n += 1

if __name__ == "__main__":
    p = Process(target=run_proc, args=(2,))  #申请子进程
    p.start()     #运行进程
    print "Parent process run. subProcess is ", p.pid
    print "Parent process end,{0}".format(time.ctime())
	
# 运行结果：

# Parent process run. subProcess is 30196 
# Parent process end,Mon Mar 27 11:20:21 2017 
# subProcess 30196 run, Mon Mar 27 11:20:21 2017 
# subProcess 30196 run, Mon Mar 27 11:20:23 2017 
# subProcess 30196 run, Mon Mar 27 11:20:25 2017