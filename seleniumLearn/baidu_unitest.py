# coding:utf-8
import unittest
from selenium import webdriver
from .baiduwangpan import init
from .baiduwangpan import toolbarCase

class BaiduTestCase(unittest.TestCase):
    # 使用修饰器，定义一个测试类的方法，这样可以不用每次执行一个测试用例就重新启动一个浏览器
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        init.init(self.driver)


    def test_01_title_and_username(self):
        u"""测试百度云登录首页的title以及与账号对应的用户名"""
        url = "https://pan.baidu.com/disk/home"
        title = init.get_title_and_username(self.driver, url)[0]
        username = init.get_title_and_username(self.driver, url)[1]
        print(title + "----" + username)
        self.assertEqual(title, init.home_title, "Title错误")
        self.assertEqual(username, init.username, "用户名错误")


    def test_02_ordericon(self):
        u"""测试首页导航栏中的排序图标的下拉列表"""
        orderlist = toolbarCase.get_orderlist(self.driver)[0]
        orderlisttext = toolbarCase.get_orderlist(self.driver)[1]
        print(len(orderlist))
        self.assertEqual(len(orderlist), init.toobar_order_list_len, "排序列表中的选项不为3")
        self.assertListEqual(orderlisttext, init.toobar_order_list, "排序下拉列表不正确")

    # 原理同setUpClass()
    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

