# coding:utf-8
import xlwt
import os
import time

def saveToExcel(header, contents, savePath, filename):
    '''
    header: [header1, header2, … , headern]
    contents: ((col1, col2, … , coln), ……, (col1, col2, … , coln)) 或 二维列表形式
    savePath: 结果存放的路径
    filename：结果文件的名字,如：result，返回的文件应为result_2018_02_07_11_47_43.xls
    '''

    if not os.path.isdir(savePath) and not os.path.isabs(savePath):
        print("*********************************************************")
        print("The savePath is Unavailable, it is must be a absolute path, eg.'D:/workspace'")
        print("*********************************************************")
        return False

    path = os.path.abspath(savePath) + r"/"
    print(path)
    '''
    filenameList = filename.split(".")
    filenameListLen = len(filenameList)
    file = ""
    for i in range(filenameListLen - 2):
        file = file + filenameList[i] + "."
    file = file + filenameList[filenameListLen - 2]  # relation1
    fileType = "." + filename.split(".")[filenameListLen - 1]  # .xls

    if not fileType == ".xls":
        print()
        print("error:The file type is Unavailable, it is must be a .xls file.")
        print("error:eg.'D:/workspace/xxx.xls'")
        print()
        return False
    '''
    formatTime = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    savePath = path + filename + "_" + formatTime + ".xls"
    if os.path.isfile(savePath):
        bak = "_" + str(time.time())
        fileOld = path + filename + "_" + formatTime + bak + ".xls"
        os.rename(savePath, fileOld)

    book = xlwt.Workbook(encoding='utf-8')
    sheet1 = book.add_sheet('sheet1')
    if header != None:
        for col in range(0, len(header)):  # 输出表头（列名称）
            sheet1.write(0, col, header[col])
        for row in range(1, len(contents) + 1):  # 输出具体查询结果
            rowValue = contents[row - 1]
            for col in range(0, len(rowValue)):
                sheet1.write(row, col, rowValue[col])
    else:
        for row in range(0, len(contents)):
            rowValue = contents[row]
            for col in range(0, len(rowValue)):
                sheet1.write(row, col, rowValue[col])

    book.save(savePath)
    print("The result is saved successful, the file is " + savePath)

    return savePath

if __name__ == "__main__":
    saveToExcel([1, 2], [["hahaha", 1], ["hahahahhaha4444444444", 2]], r"D:\workspace", "xixihaha")

