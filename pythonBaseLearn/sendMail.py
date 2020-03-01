# coding:utf-8
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib
import time
import os

def sendmail(file_new):
    mail_from = "testing4862@163.com"
    mail_to = "531351925@qq.com"

    #定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')

    #定义标题
    msg['Subject'] = u'测试报告'
    msg['data'] = time.strftime('%a, %d %b %Y %H:%M:%S %z ')
    smtp = smtplib.SMTP()
    print(msg)

    # 连接服务器
    smtp.connect('smtp.163.com')
    authentication_code = 'testing4862'  # 邮箱客户端登录的授权码，在网页版的设置中查找
    smtp.login('testing4862@163.com',authentication_code )
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()

def findlastreport(result_dir):

    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not os.path.isdir(result_dir+"\\"+fn) else 0)
    print (u'最新测试报告：'+ lists[-1])
    file_new = os.path.join(result_dir, lists[-1])
    return file_new

def sendreport(result_dir):

    report = findlastreport(result_dir)
    sendmail(report)

if __name__ == "__main__":
    result_dir = r'D:\\code'
    sendreport(result_dir)

