#coding:utf-8
from selenium.webdriver import ActionChains


def get_orderlist(driver):
    url = "https://pan.baidu.com/disk/home"
    driver.get(url)
    toobar = driver.find_element_by_css_selector("#layoutMain").find_element_by_class_name("DxdbeCb")
    order = toobar.find_element_by_class_name("EzLavy")
    #showtype = toobar.find_element_by_class_name("ryvhP50g")
    orderlistshow = order.find_element_by_class_name("efdtEWV0")
    ActionChains(driver).move_to_element(orderlistshow).perform()
    orderlist = order.find_element_by_class_name("sDwvAgb").find_elements_by_css_selector("span")

    listpro = []
    for orderem in orderlist:
        emtext = orderem.get_attribute("innerText")
        listpro.append(emtext)

    return [orderlist, listpro]

def order(driver):
    # ====================文件列表================================
    filelists = driver.find_element_by_css_selector("#layoutMain").find_element_by_class_name(
        "vdAfKMb").find_elements_by_css_selector("dd")
    print(len(filelists))
    for file in filelists:
        filehref = file.find_element_by_css_selector("div.file-name>div>a")
        filetitle = filehref.get_attribute("title")
        print(filetitle)
