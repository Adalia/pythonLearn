# coding:utf-8
import logging
from datetime import datetime
import threading
import getConfig
import os

class Log:
    global logPath
    logPath = getConfig.ReadConfig().get_logPath()

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
       return self.logger

class MyLog(threading.Thread):  # 线程使用疑问
    #线程讲解https://my.oschina.net/u/3041656/blog/794357
    log = None
    mutex = threading.Lock()
    count =0
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()
        #pass

    #@staticmethod
    def get_log(self):
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.count = MyLog.count + 1
            print("getlog")
            print(MyLog.count)
            MyLog.mutex.release()
        return MyLog.log

if __name__ == '__main__':
    for i in range(1,5,1):
        print(MyLog().get_log())
        print(" ")

