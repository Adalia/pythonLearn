# coding:utf-8
import unittest
import HTMLTestRunner
import os
import interfaceTest.common.getConfig as getConfig
from interfaceTest.common.configLog import MyLog
from interfaceTest.common.configEmail import Email

class casesSuite:
    def __init__(self):
        self.casesListFile = os.path.join(getConfig.proDir,"testCases/casesList")
        self.casesList=[] #['/baidu/haha', '/baidu/xixi']
        self.email = Email()

    def set_case_list(self):
        fb = open(self.casesListFile)
        for value in fb.readlines():
            data = str(value)
            if data!='' and not data.startswith("#"):
                self.casesList.append(data.replace("\n",""))
        fb.close()
        print(self.casesList)

    def set_case_suite(self):
        self.set_case_list() # 得到casesList中的值的列表casesList
        testSuite = unittest.TestSuite()
        suiteList = []
        caseDir = getConfig.caseDir  # 存放用例的最顶层目录,存放用例的文件夹必须是包
        for case in self.casesList:
            print("=========case: ")
            print(case)
            case_name = case.split("/")[-1]
            print("*******casename: "+case_name+".py")
            discover = unittest.defaultTestLoader.discover(caseDir,pattern=case_name+".py",top_level_dir=None)
            suiteList.append(discover)
            for test in discover:
                print(test)
                testSuite.addTest(test)
        print("============================================")
        print(testSuite)

        return testSuite

    def run(self):
        resultFile = getConfig.ReadConfig().get_resultPath()
        log = MyLog()
        print("casesSuit启动log：")
        print(log)
        logger = log.get_log().get_logger()
        try:
            suit = self.set_case_suite()
            if suit is not None:
                logger.info("********TEST START********")
                fp = open(resultFile, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                runner.run(suit)
            else:
                logger.info("Have no case to test.")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("*********TEST END*********")
            # send test report by email
            on_off =getConfig.ReadConfig().get_email("on_off")
            if int(on_off) == 0:
                self.email.send_email()
            elif int(on_off) == 1:
                logger.info("Doesn't send report email to developer.")
            else:
                logger.info("Unknow state.")

if __name__ == "__main__":
    casesSuite().run()
