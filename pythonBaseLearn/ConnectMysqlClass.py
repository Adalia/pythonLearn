#-*- coding: utf-8 -*-
'''
Created on 20160902
@author: LiHaihui
'''
import pymysql
from pythonbase.save_to_xlsx import *


class ConnctMysql(object):
    '''
    Connect class
    'encoding': utf-8
     __init__(host,user,password,db,port):
     __init__(host,user,password,db,port,encoding):
    '''
    host = None
    user = None
    password = None
    db = None
    port = '3306'
    encoding = 'utf-8'
    connect = None
    cursor = None
    '''Init connection '''
    def __init__(self, host, user, password, db, port, encoding='utf8'):  # 创建数据库的连接
        
        try: 
            self.connect = pymysql.connect(host=host, user=user, passwd=password, db=db, port=port, charset=encoding)
              
        except pymysql.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def select(self, selectColList, tableList, requirementsList):

        '''
        This function need 4 arguments: selectColList,tableList,requirementsList,savePath.
           Sql = Select secectColList from tableList where requirementsList.
           返回查询列表[[],……,  []]
        ''' 
        # print(tableList)
        sql = "select "
        for colN in range(0,len(selectColList)-1):
            print(selectColList[colN])
            sql = sql+selectColList[colN]+","
        sql = sql + selectColList[len(selectColList)-1] 
        
        sql = sql + " from "
        for tableN in range(0,len(tableList)-1):
            sql = sql+tableList[tableN]+","
        sql = sql + tableList[len(tableList)-1]   
        
        sql = sql + " where "
        for requireN in range(0,len(requirementsList)-1):
            sql = sql + requirementsList[requireN]+" "
        sql = sql + requirementsList[len( requirementsList)-1]
        
        print()
        print(sql)
        print()
        
        self.cursor=self.connect.cursor()  # 创建数据库游标
        print(self.cursor.execute(sql))
        if self.cursor.execute(sql):
            print("Select successful!")
            print(self.cursor.execute(sql))
        rows = self.cursor.fetchall()#得到查询的所有数据
        self.cursorClose()
        
        self.commit()
        if len(rows) == 0:  #如果查询结果为空，将不存出结果
            print("There is no results conform to the conditions of the query.")
            return 0
        else:
            return rows
    
    def insert(self, table, insertColList, insertColValuesTuplesList):  # “INSERT IGNORE INTO 和：  忽略重复的，或者替换重复的
        '''
        insertCloList[col1,col2,……,coln]
        values= [(value1,value2,……,valuen),(value1,value2,……,valuen),(value1,value2,……,valuen)……]
        '''
        colListLen = len(insertColList)
        # 拼接sql语句"insert int tablename (col1,col2,……,coln) values (%s,%s,……,%s)
        sql = "insert ignore into " + table + " ("
        for colNum in range(0,colListLen-1):
            sql = sql + insertColList[colNum]+ ","
        sql = sql + insertColList[colListLen-1]
        
        sql = sql + ") values ("
        for colNum in range(0,colListLen-1):
            sql = sql + "%s, "    
        sql = sql + "%s)"

        print()
        print(sql)
        print()
        
        self.cursor=self.connect.cursor()   
        for value in insertColValuesTuplesList:
            print(value)
            if len(value)==colListLen:
                if self.cursor.execute(sql,value):
                    print("Insert"+str(value)+"successful!")
                    print
                else:
                    print("Have duplicate entry for col which must be only")
                    print()
            else:
                print("The number of "+str(value)+"is not equal to the number of columns:")
                print()
                
        self.cursorClose()
        self.commit() 
    
    def update(self,table, updateColList, requirementsList):
        '''
        updateCloList[col1,col2,……,coln]
        col1 = [colname,colvalue]
        '''
        colListLen = len(updateColList)
       
        colvalues = [updateColList[0][1]]
        for colNum in range(1,colListLen):
            colvalues.append(updateColList[colNum][1])
        colvalues = tuple(colvalues)
        print(tuple(colvalues))
        
        sql = "update " + table + " set "
        for colNum in range(0,colListLen-1):
            sql = sql + updateColList[colNum][0]+ " = '"+updateColList[colNum][1] +"',"
        sql = sql + updateColList[colListLen-1][0]+ " = '"+updateColList[colListLen-1][1]+"'"
        sql = sql + " where "
        for requireN in range(0,len(requirementsList)-1):
            sql = sql + requirementsList[requireN]+" "
        sql = sql + requirementsList[len(requirementsList)-1]
        print()
        print(sql)
        print()
        self.cursor= self.connect.cursor()
        if self.cursor.execute(sql):
            print("The row is updated successful!")
            print
        else:
            print("The row is not need  updated!")
            print()
        
        self.cursorClose()
        self.commit()
        return False
    
    def delete(self, table, requirementsList):
        self.cursor = self.connect.cursor()
        sql = "delete from "+table
        sql = sql + " where "
        for requireN in range(0,len(requirementsList)-1):
            sql = sql + requirementsList[requireN]+" "
        sql = sql + requirementsList[len( requirementsList)-1]
        print(sql)
        if self.cursor.execute(sql):
            print("Delete successful!")
            print()
        
        self.cursorClose()
        self.commit()
        #return False

                   
    def commit(self):
        self.connect.commit()
    def cursorClose(self):
        self.cursor.close()
    def connectClose(self):
        self.connect.close()

if __name__ == '__main__':
    conn = ConnctMysql('127.0.0.1', 'root', 'root', 'test_mysqldb', 3306)

    # 多表查询
    selectCol = ["mail.MAIL_SEND_TIME", "mail.MAIL_SUBJECT", "file.FILE_TYPE", "file.FILE_NAME",
                 "file.ATTACHPATH", "file.CONTENT"]
    tableList = ["ZC_MAIL_DATA_INFO as mail", "ZC_FILE AS file", "ZC_ATTACH_INFO as attach"]
    requirementsList = ["mail.MID=attach.MID", "and", "attach.MD5=file.ID"]
    results = conn.select(selectCol, tableList, requirementsList)
    savePath = "D:/code/MyLearnProject/pythonbase/output"
    saveToExcel(selectCol,results,savePath,"mailattch")

    print(results)
    print(type(results))
    '''
    # 单行or多行插入
    cols1 = ['SXM_RULE_ID', 'SXM_RULE_KWORD_1']
    colsvalues = [(11, "ahh"), (12, "xixi"), (13, "88")]
    conn.insert("SXM_RULE", cols1, colsvalues)

    # 删除
    requirementsList = ["SXM_RULE_ID=99", "or", "SXM_RULE_ID=56"]
    conn.delete("SXM_RULE", requirementsList)

    # 更新
    cols = [['SXM_RULE_KWORD_1', "update"], ['SXM_RULE_STATUS', "0"],
            ['SXM_RULE_CREATETIME', "2016-09-05 13:49:36"], ['SXM_RULE_STARTTIME', '2016-09-05 13:55:36']]
    requirementsList = ["SXM_RULE_ID=9"]
    conn.update("SXM_RULE", cols, requirementsList)

    conn.connectClose()
    # 使用cur.rowcount获取影响了多少行
    # print("Number of rows updated: %d" % cur.rowcount)
    # connect.outputSelectResult( 1, 1)
    # connect.selectRelation("ralationResult")

    '''



