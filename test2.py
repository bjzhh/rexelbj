from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import xdrlib ,sys
import xlrd
import re
import xlrd
worksheet = xlrd.open_workbook(r'E:\Bernie.xlsx') #打开excel文件
sheet_names= worksheet.sheet_names() #获取excel中所有工作表名
sheet2 = worksheet.sheet_by_name('Sheet1')   #根据Sheet名获取数据
sheet2 = worksheet.sheet_by_index(0)  #根据索引获取数据，索引为0开始，1表示获取第二张工作表数据
#获取行数和列数
nrows = sheet2.nrows - 1
ncols = sheet2.ncols
print('行数',nrows)
print('列数',ncols)

rows = sheet2.row_values(1)  #表示获取Sheet2中第2行数据
print('获取Sheet2中第2行数据',rows)

cols10 = sheet2.col_values(2)  #表示获取Sheet2中第3列数据（数据保存为list）
print('获取Sheet2中第3列数据',cols10)
cell=sheet2.cell(0,1)  #表示获取Sheet2中(0,1)单元格的数据（数据保存为list）
print('获取Sheet2中(0,1)单元格的数据',cell)
#2007测试表 4 4
print (sheet2.name,sheet2.nrows,sheet2.ncols)
#print (sheet2.cell(1,0).value.encode('utf-8'))  

print ('ctype=',sheet2.cell(1,0).ctype)

print('获取单元格A1值',sheet2.cell(1,1).value)  #获取单元格A1值，column与row依然可用

for i in range(1,5,1):
    print(sheet2.cell(i,1).value) #更加方便实用
    c=sheet2.cell(i,1).value
    print(c)
    if c.find('22.3'):
        print("没有找到所需要的数")
    else:
        print("找到所需要的数")
        A=sheet2.cell(i,0).value
        print(sheet2.cell(i,0).value)
        B=sheet2.cell(i,1).value
        print(sheet2.cell(i,1).value)
        C=sheet2.cell(i,2).value
        print(sheet2.cell(i,2).value)
        D=sheet2.cell(i,3).value
        print(sheet2.cell(i,3).value)
        print("HAHAHAHAHAHAHAHAHA")

class MyTable(QTableWidget):
    def __init__(self,parent=None):
        super(MyTable, self).__init__(parent)
        self.setWindowTitle("北京微电子技术研究所技术支持库")
        self.resize(1380, 480)
        self.setColumnCount(7)
        self.setRowCount(4)
        #设置表格有两行五列。
        self.setColumnWidth(0, 200)
        self.setColumnWidth(4, 200)
        self.setRowHeight(0, 100)
        #设置第一行高度为100px，第一列宽度为200px。
        self.table()

    def table(self):
        self.setItem(0,0,QTableWidgetItem("名称"))
        self.setItem(0,1,QTableWidgetItem("价格"))
        self.setItem(0,2,QTableWidgetItem("出版社"))
        self.setItem(0,3, QTableWidgetItem("语言"))
        self.setItem(0,4,QTableWidgetItem("日期"))
        self.setItem(0,5, QTableWidgetItem("职业"))
        #self.setItem(0,4, QTableWidgetItem("收入"))
        #添加表格的文字内容.
        self.setHorizontalHeaderLabels(["第一行", "第二行", "第三行", "第四行","第五行", "第六行","第七行"])
        self.setVerticalHeaderLabels(["第一列", "第二列","第三列", "第四列"])
        #设置表头
        lbp = QLabel()
        lbp.setPixmap(QPixmap("Maley.png"))
        #在表中添加一张图片
        #self.setCellWidget(1,1,lbp)

        twi = QTableWidgetItem(A)
        twi.setFont(QFont("Times", 10, ))
        self.setItem(1,0,twi)

        twj = QTableWidgetItem(B)
        twj.setFont(QFont("Times", 10, ))
        self.setItem(1,1,twj)

        twk = QTableWidgetItem(C)
        twk.setFont(QFont("Times", 10, ))
        self.setItem(1,2,twk)

        twl = QTableWidgetItem(D)
        twl.setFont(QFont("Times", 10, ))
        self.setItem(1,3,twl)


        #添加一个自己设置了大小和类型的文字。
        dte = QDateTimeEdit()
        dte.setDateTime(QDateTime.currentDateTime())
        dte.setDisplayFormat("yyyy/MM/dd")
        dte.setCalendarPopup(True)
        self.setCellWidget(1,4,dte)
        #添加一个弹出的日期选择，设置默认值为当前日期,显示格式为年月日。
        cbw = QComboBox()
        cbw.addItem("医生")
        cbw.addItem("老师")
        cbw.addItem("律师")
        self.setCellWidget(1,5,cbw)
        #添加了一个下拉选择框
        sb = QSpinBox()
        sb.setRange(1000,10000)
        sb.setValue(5000)#设置最开始显示的数字
        sb.setDisplayIntegerBase(10)#这个是显示数字的进制，默认是十进制。
        sb.setSuffix("元")#设置后辍
        sb.setPrefix("RMB: ")#设置前辍
        sb.setSingleStep(100)
        self.setCellWidget(1,6,sb)
    def open_excel(file= '2018.xlsx'):
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception as e:
            print (str(e))
    def excel_table_byname(file= '2018.xlsx',colnameindex=0,by_name=u'2007测试表'):
        data = open_excel(file)
        table = data.sheet_by_name(by_name)
        nrows = table.nrows #行数 
        colnames = table.row_values(colnameindex) #某一行数据 
        list =[]
        for rownum in range(1,nrows):
            row = table.row_values(rownum)
            if row:
                app = {}
                for i in range(len(colnames)):
                    app[colnames[i]] = row[i]
                list.append(app)
        return list


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myTable = MyTable()
    myTable.show()
    app.exit(app.exec_())
