# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

# import webbrowser
from PyQt5.QtWidgets import QAction


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuShoutKeys = QtWidgets.QMenu(self.menubar)
        self.menuShoutKeys.setObjectName("menuShoutKeys")
        self.menuOfficeTools = QtWidgets.QMenu(self.menubar)
        self.menuOfficeTools.setObjectName("menuOfficeTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionsettings = QtWidgets.QAction(MainWindow)
        self.actionsettings.setObjectName("actionsettings")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionIFS = QtWidgets.QAction(MainWindow)
        self.actionIFS.setObjectName("actionIFS")
        self.actionCRM = QtWidgets.QAction(MainWindow)
        self.actionCRM.setObjectName("actionCRM")
        self.actionPAS = QtWidgets.QAction(MainWindow)
        self.actionPAS.setObjectName("actionPAS")
        self.actionOMS = QtWidgets.QAction(MainWindow)
        self.actionOMS.setObjectName("actionOMS")
        self.actionESS = QtWidgets.QAction(MainWindow)
        self.actionESS.setObjectName("actionESS")
        self.actionIMC = QtWidgets.QAction(MainWindow)
        self.actionIMC.setObjectName("actionIMC")
        self.actionExcel_Split = QtWidgets.QAction(MainWindow)
        self.actionExcel_Split.setObjectName("actionExcel_Split")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionsettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuShoutKeys.addAction(self.actionIFS)
        self.menuShoutKeys.addAction(self.actionCRM)
        self.menuShoutKeys.addAction(self.actionPAS)
        self.menuShoutKeys.addAction(self.actionOMS)
        self.menuShoutKeys.addAction(self.actionESS)
        self.menuShoutKeys.addAction(self.actionIMC)
        self.menuOfficeTools.addAction(self.actionExcel_Split)
        self.menuHelp.addAction(self.actionUpdate)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuShoutKeys.menuAction())
        self.menubar.addAction(self.menuOfficeTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # self.actionIFS.triggered(QAction).connect(self.pk)

# def pk(self,q):
#     print(q.text() + 'okokok')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "REXEL App Box"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuShoutKeys.setTitle(_translate("MainWindow", "ShoutKeys"))
        self.menuOfficeTools.setTitle(_translate("MainWindow", "OfficeTools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
        self.actionsettings.setText(_translate("MainWindow", "settings..."))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionIFS.setText(_translate("MainWindow", "IFS"))
        self.actionCRM.setText(_translate("MainWindow", "CRM"))
        self.actionPAS.setText(_translate("MainWindow", "PAS"))
        self.actionOMS.setText(_translate("MainWindow", "OMS"))
        self.actionESS.setText(_translate("MainWindow", "ESS"))
        self.actionIMC.setText(_translate("MainWindow", "IMC"))
        self.actionExcel_Split.setText(_translate("MainWindow", "Excel Split"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionUpdate.setText(_translate("MainWindow", "Update..."))

