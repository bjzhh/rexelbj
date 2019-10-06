import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainMenu(QMainWindow):
    def __init__(self,parent=None):
        super(MainMenu,self).__init__(parent)
        self.resize(800, 600)

        layout = QHBoxLayout()
        bar = self.menuBar()
        m1 = bar.addMenu('File')
        m1.addAction('New...')
        m1.addAction('Open...')
        m1.addAction('Save')
        m1.addAction('Save...')
        m1.addAction('print')
        m1.addAction('Quit')

        m1.triggered[QAction].connect(self.pk)

        m2 = bar.addMenu('ShortCut')
        m2.addAction('IFS')
        m2.addAction('CRM')
        m2.addAction('PAS')
        m2.addAction('ESS')
        m2.addAction('OMS')
        m2.addAction('IMC')


        m3 = bar.addMenu('ShortCut')
        m3.addAction('Excel Split')


        m4 = bar.addMenu('ShortCut')
        m4.addAction('Update...')
        m4.addAction('About')

    def pk(self,q):
        print(q.text(),' is ok')
        if q.text() == 'Quit':
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mm = MainMenu()
    mm.show()
    sys.exit(app.exec_())
