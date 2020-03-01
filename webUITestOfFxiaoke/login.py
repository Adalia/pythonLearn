import requests
from common.readconfig import ReadConfig
import configparser

class Login:
    def __init__(self):
        self.conf = ReadConfig() #"config.ini"
        print(self.conf.cf.sections())

    def login(self, dev, ei):
        if(dev == 'test'):
            domain = "https://www.ceshi112.com"
        else:
            domain = "https://www.fxiaoke.com"

        login_url = domain + "/FHH/EM0HUL/Authorize/EnterpriseAccountLogin"

        login_key = self.conf.get_login_key(ei)
        print("login_key:"+login_key)

        response = requests.post(login_url, json=login_key)
        print(response.text)


if __name__=="__main__":
    login1 = Login()
    login1.login("test","71698")