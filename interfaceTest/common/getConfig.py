# coding:utf-8
import os
import codecs   #解决文件编码问题
import ConfigParser
import datetime

proD = os.path.split(os.path.realpath(__file__))[0]
proDir = os.path.split(proD)[0]
configPath = os.path.join(proDir,'conf.cfg')
caseDir = os.path.join(proDir,'testCases')

class ReadConfig:
    def __init__(self):
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(os.path.join(proDir,"conf.cfg"))
    def getConfig(self,section,key):
        return self.cf.get(section,key)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

    def get_resultPath(self):
        resultPath = os.path.join(proDir, "result")
        if not os.path.exists(resultPath):
             os.mkdir(resultPath)
        resultname="result_"+str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))+".html"
        resultFile=os.path.join(resultPath,resultname)
        return resultFile

    def get_logPath(self):
        resultPath = os.path.join(proDir, "result")
        logPath = os.path.join(resultPath,str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(logPath):
          os.mkdir(logPath)
        return logPath

if __name__ == '__main__':
    print(proDir)
    print(ReadConfig().getConfig('EMAIL','mail_host'))