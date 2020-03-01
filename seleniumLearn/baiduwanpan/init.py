# coding:utf-8
import time


home_title = u'百度网盘-全部文件'
username = u'幸福_小乖'
toobar_order_list = [u"文件名", u"大小", u"修改日期"]
toobar_order_list_len = len(toobar_order_list)
cookieslist=[{'domain': '.baidu.com', 'expiry': 1549505204.797628, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': 'D3828E482815792C7B3EC39D9E4973BF:FG=1'}, \
              {'domain': '.pan.baidu.com', 'expiry': 1549505212, 'httpOnly': False, 'name': 'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0', 'path': '/', 'secure': False, 'value': '1517969212'}, \
              {'domain': '.pan.baidu.com', 'expiry': 1520561210.765999, 'httpOnly': True, 'name': 'STOKEN', 'path': '/', 'secure': False, 'value': '23e25c3b62668c16f170ed53485243ee6e9a7ac075336d38fa1b97d565aa08ec'}, \
              {'domain': '.baidu.com', 'expiry': 2556057600, 'httpOnly': False, 'name': 'FP_UID', 'path': '/', 'secure': False, 'value': 'd9f7f09f7116a4e7ab3d465f1604e9a0'},\
              {'domain': '.baidu.com', 'expiry': 1777169209.553225, 'httpOnly': True, 'name': 'BDUSS', 'path': '/', 'secure': False, 'value': 'Ux4eFZKOGhSQTZEMzVEOHdtS2FjOFdlTmZLRkJXYVl6Y3NpRTNveC1PTTU3S0ZhQVFBQUFBJCQAAAAAAAAAAAEAAAAuIRoQ0NK4o1~QobnUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADlfelo5X3paY'}, \
              {'domain': '.pan.baidu.com', 'expiry': 1520561210.765857, 'httpOnly': True, 'name': 'SCRC', 'path': '/', 'secure': False, 'value': '7bf1cf84f298263bbd51c44b376569db'}, {'domain': 'pan.baidu.com', 'expiry': 4109969210.613192, 'httpOnly': False, 'name': 'pan_login_way', 'path': '/', 'secure': False, 'value': '1'}, \
              {'domain': '.pan.baidu.com', 'expiry': 1549505210.654186, 'httpOnly': False, 'name': 'PANWEB', 'path': '/', 'secure': False, 'value': '1'},\
              {'domain': '.pan.baidu.com', 'httpOnly': False, 'name': 'Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0', 'path': '/', 'secure': False, 'value': '1517969212'}, \
              {'domain': '.pan.baidu.com', 'expiry': 1518055613.822401, 'httpOnly': True, 'name': 'PANPSC', 'path': '/', 'secure': False, 'value': '12853920149049253088%3AXppE28xPbvLd7JASh8gDKrHQG6qeixv0ysYP0LIp8HGEvXm79GhqCKXToYasOMBASrvFsiwiy%2BHl0rTUmtFxx8Js6VzM5d7HyYKFurdZKlTXG9GmBZpeFQ5fEBmQG6Wags6%2BSP%2BysvjmHv0bs3W3dKdgHgOgmuYeA8yxsQhfco3IUyrvncE2%2F56%2FckKAnhyPPINT3EXK3IjGdPa0DtmINb3bwxtQHr5H'}, \
              {'domain': '.baidu.com', 'expiry': 1518833216, 'httpOnly': False, 'name': 'cflag', 'path': '/', 'secure': False, 'value': '15%3A3'}]

def init(driver):
    driver.get("https://pan.baidu.com/")
    driver.set_window_size(1280, 960)
    driver.implicitly_wait(30)
    for cookie in cookieslist:
        driver.add_cookie(cookie)

def get_title_and_username(driver, url):
    driver.get(url)
    time.sleep(5)
    title = driver.title
    user = driver.find_element_by_class_name("user-name").get_attribute("innerHTML")
    return [title, user]

