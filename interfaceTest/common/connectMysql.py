# coding:utf-8
import pymysql
from interfaceTest.common import configLog, getConfig
from requests.exceptions import ConnectionError

getDB = getConfig.ReadConfig()

class MyDB():
    global host, username, passwd, port, database, config, charset
    host = getDB.getConfig('DATABASE','host')
    username = getDB.getConfig('DATABASE','username')
    passwd = getDB.getConfig('DATABASE','password')
    port = getDB.getConfig('DATABASE','port')
    database = getDB.getConfig('DATABASE','database')
    charset = getDB.getConfig('DATABASE','charset')
    config = {
        'host': str(host),
        'user':username,
        'passwd':passwd,
        'port':int(port),
        'db':database,
        'charset': str(charset)
    }
    def __init__(self):
        self.log = configLog.MyLog.get_log()
        self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None

    def connectDB(self):
        try:
            self.db = pymysql.connect(**config)
            self.cursor = self.db.cursor()
            print("Connect DB successfully!")
        except ConnectionError as ex:
            self.logger.error(str(ex))

    def executeSQL(self,sql,params):
        self.connectDB()
        self.cursor.execute(sql,params) # #param应该为tuple或者list
        self.db.commit()
        return self.cursor

    def get_all(self,cursor):
        return cursor.fetchall()

    def get_one(self,cursor):
        return cursor.fetchone()

    def closeDB(self):
        self.db.close()
        print("Close DB successfully!")

if __name__ == '__main__':
    MyDB().connectDB()





