# coding:utf-8
import HTMLTestRunner
import os
import time
import unittest
from seleniumlearn import baidu_unitest
from util import sendMail

def casesuitetest():

    # 用测试套件加载测试类，按加载的顺序执行各个测试类，但是测试类中的测试方法还是根据名称来排序的。
    testunit = unittest.TestSuite()
    testunit.addTest(unittest.makeSuite(a.A))
    testunit.addTest(unittest.makeSuite(b.B))
    testunit.addTest(unittest.makeSuite(baidu_unitest.BaiduTestCase))

    timestring = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
    # 这块是获取项目路径，后面在生成report时会放到改目录下
    current_path = os.getcwd()

    # 要先建立下面的文件夹selenium_result，否则会报错[Errno 22] invalid mode ('wb') or filename
    result_path = current_path + r'\output'

    filename = result_path +r'\selenium-result_'+ timestring + '.html'
    print(filename)

    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'selenium自动化测试学习',
        description=u'用例执行结果:'
    )
    runner.run(testunit)
    fp.close()
    #sendMail.sendreport(result_path)

if __name__ == '__main__':
    print('开始执行测试用例')
    casesuitetest()
    print('测试用例执行完毕')


