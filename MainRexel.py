import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import webbrowser


class MainMenu(QMainWindow):
    # def __init__(self,parent=None):
    #     super(MainMenu,self).__init__(parent)
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        self.setWindowIcon(QIcon("./res/box.ico"))  # 设置窗口图标
        self.setWindowTitle("REXEL App Box")  # 设置窗口名

        layout = QHBoxLayout()
        bar = self.menuBar()
        m1 = bar.addMenu('File')
        m1.addAction('New...')
        m1.addAction('Open...')
        m1.addAction('Save')
        m1.addAction('Save...')
        m1.addAction('print')
        myquit= m1.addAction('Quit')

        bar.triggered[QAction].connect(self.pk)

        m2 = bar.addMenu('ShortCut')
        m2.addAction('IFS')
        m2.addAction('CRM')
        m2.addAction('PAS')
        m2.addAction('ESS')
        m2.addAction('Rexel Academy')
        m2.addAction('Success Factor')
        m2.addAction('Web Email')
        m2.addAction('rexel.com.cn')

        m3 = bar.addMenu('Office')
        m3.addAction('Excel Split')

        m4 = bar.addMenu('Help')
        m4.addAction('Update...')
        m4.addAction('About')

        myquit = QAction(QIcon('./res/exit.ico'), 'Quit', self)
        myquit.setShortcut('Ctrl+Q')
        myquit.setStatusTip('Quit application')
        myquit.triggered.connect(self.close)

        self.statusBar()
        # menubar = self.menuBar()
        # fileMenu = bar.addMenu('&File')
        # fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(myquit)

    def pk(self,q):
        print(q.text(),' is ok')
        if q.text() == 'Quit':
            self.close()
        elif q.text() == 'Web Email':
            webbrowser.open_new('http://outlook.office365.com')
        elif q.text() == 'rexel.com.cn':
            webbrowser.open_new('http://www.rexel.com.cn')
        elif q.text() == 'IFS':
            webbrowser.open_new('http://jbosssvr01.rexel-cn.local:58080/')
        elif q.text() == 'CRM':
            webbrowser.open_new('http://10.219.120.35/Login/Index')
        elif q.text() == 'PAS':
            webbrowser.open_new('http://10.219.100.70:8080/pas/')
        elif q.text() == 'ESS':
            webbrowser.open_new('http://10.219.100.77/PlatinumHRM-ESS/logon.aspx')
        elif q.text() == 'Success Factor':
            webbrowser.open_new('https://performancemanager4.successfactors.com/login?company=Rexel&loginMethod=PWD#/login')
        elif q.text() == 'Rexel Academy':
            webbrowser.open_new('https://rexelacademy.lms.crossknowledge.com/interfaces/login.php')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mm = MainMenu()
    mm.show()
    sys.exit(app.exec_())
