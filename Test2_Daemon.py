# -*- coding:utf-8 -*-
from multiprocessing import Process, Pool
import os
import time


def run_proc(wTime):
    n = 0
    while n < 3:
        print "subProcess %s run," % os.getpid(), "{0}".format(time.ctime())
        time.sleep(wTime)
        n += 1

if __name__ == "__main__":
    p = Process(target=run_proc, args=(2,))
    p.daemon = True    #加入daemon
    p.start()
    print "Parent process run. subProcess is ", p.pid
    print "Parent process end,{0}".format(time.ctime())
	
# 执行结果：

# Parent process run. subProcess is 31856 
# Parent process end,Mon Mar 27 11:40:10 2017