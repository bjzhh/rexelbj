import sys
import MainWin

from PyQt5.QtWidgets import QApplication,QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = QMainWindow()
    ui = MainWin.Ui_MainWindow()
    ui.setupUi(mw)
    mw.show()


    def pk(self):
        print('okokok')

    # def IFS_Clicked(self):
    #     webbrowser.open('http://www.rexel.com.cn')

    sys.exit(app.exec())
