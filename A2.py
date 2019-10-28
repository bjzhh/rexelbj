from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pandas as pd
import numpy as np
from openpyxl import *


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowIcon(QIcon("./res/excel.ico"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 510, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 751, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 513, 251, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 513, 251, 20))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 510, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.openfile)
        self.pushButton.clicked.connect(self.creat_table_show)

        self.pushButton_2.clicked.connect(self.ExcelSplit)
        self.pushButton_2.clicked.connect(self.HorSectionClicked)


        #想要获得点击所在列 zhh
        self.tableWidget.clicked.connect(self.viewclicked)

        self.tableWidget.verticalHeader().sectionClicked.connect(self.VerSectionClicked)  # 表头单击信号
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.HorSectionClicked)  # 表头单击信号

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Excel按列拆分"))
        self.pushButton.setText(_translate("MainWindow", "打开"))
        self.pushButton_2.setText(_translate("MainWindow", "按列切割"))


    def VerSectionClicked(self, index):
        print(index)
        # ExcelSplit()


    def HorSectionClicked(self, index):
        print(index)
        global aa

        aa = self.tableWidget.model().headerData(index, Qt.Horizontal)
        print(type(aa))
        print(aa)


    def viewclicked(self,index):
        col = self.tableWidget.currentColumn()
        row = self.tableWidget.currentRow()
        # print('您点击了第' + str(row+1) +'行' + '第' + str(col+1) + '列。' + '列名：')
        # print(self.tableWidget.columnCount())


    def openfile(self):

        ###获取路径===================================================================

        openfile_name = QFileDialog.getOpenFileName(self,'选择文件','','Excel files(*.xlsx , *.xls)')

        #print(openfile_name)
        global path_openfile_name




        ###获取路径====================================================================

        path_openfile_name = openfile_name[0]
        self.label.setText(path_openfile_name)

    def creat_table_show(self):
        ###===========读取表格，转换表格，===========================================
        if len(path_openfile_name) > 0:
            input_table = pd.read_excel(path_openfile_name)
        #print(input_table)
            input_table_rows = input_table.shape[0]
            input_table_colunms = input_table.shape[1]
            #print(input_table_rows)
            #print(input_table_colunms)
            input_table_header = input_table.columns.values.tolist()
            #print(input_table_header)

        ###===========读取表格，转换表格，============================================
        ###======================给tablewidget设置行列表头============================

            self.tableWidget.setColumnCount(input_table_colunms)
            self.tableWidget.setRowCount(input_table_rows)
            self.tableWidget.setHorizontalHeaderLabels(input_table_header)

        ###======================给tablewidget设置行列表头============================

        ###================遍历表格每个元素，同时添加到tablewidget中========================
            for i in range(input_table_rows):
                input_table_rows_values = input_table.iloc[[i]]
                #print(input_table_rows_values)
                input_table_rows_values_array = np.array(input_table_rows_values)
                input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
            #print(input_table_rows_values_list)
                for j in range(input_table_colunms):
                    input_table_items_list = input_table_rows_values_list[j]
                #print(input_table_items_list)
                # print(type(input_table_items_list))

        ###==============将遍历的元素添加到tablewidget中并显示=======================

                    input_table_items = str(input_table_items_list)
                    newItem = QTableWidgetItem(input_table_items)
                    newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    self.tableWidget.setItem(i, j, newItem)

        ###================遍历表格每个元素，同时添加到tablewidget中========================

            #提示用户不要忘了点列名
            QMessageBox.warning(self, '', '请点击表中列名进行按列拆分。', QMessageBox.Yes)

        else:
            self.centralWidget.show()


    def ExcelSplit(self):
        # import pandas as pd
        # from openpyxl import *

        data = pd.read_excel(path_openfile_name)
        # data['日期']=pd.to_datetime(data['时间']).dt.date
        data_excel=[]
        sheetname=[]
        # b1 = self.HorSectionClicked()
        # print(b1)

        for x in data.groupby(str(aa)):
            data_excel.append(x[1])
            sheetname.append(x[0])

        dir2 = QFileDialog.getExistingDirectory(self,'选择目标文件夹','')
        for i in range(len(sheetname)): #区别在于循环创建多个路径，路径中加入变量工作表名称
            # print(dir2)
            filename = str(dir2) + "\\" + str(sheetname[i]) + ".xlsx"
            # filename = "d:\\excelsplit\\" + str(sheetname[i]) + ".xlsx"

            # print(filename)
            # data_excel[i].iloc[:,0:4].to_excel(r"e:\\" + str(sheetname[i]) + ".xlsx")
            data_excel[i].iloc[:,0:self.tableWidget.columnCount()].to_excel(filename)
            wb = load_workbook(filename)
            ws = wb.active
            ws.delete_cols(1) #删除第 13 列数据
            ws.freeze_panes = 'A2'  #冻结第一行
            wb.save(filename)
        QMessageBox.warning(self, '', '切割完毕！', QMessageBox.Yes)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())