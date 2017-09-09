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
    p.daemon = True
    p.start()
    p.join()    #加入join方法
    print "Parent process run. subProcess is ", p.pid
    print "Parent process end,{0}".format(time.ctime())
	
	
# 执行结果：

# subProcess 32076 run, Mon Mar 27 11:46:07 2017 
# subProcess 32076 run, Mon Mar 27 11:46:09 2017 
# subProcess 32076 run, Mon Mar 27 11:46:11 2017 
# Parent process run. subProcess is 32076 
# Parent process end,Mon Mar 27 11:46:13 2017