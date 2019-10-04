import sys
import MainWin

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = QMainWindow()
    ui = MainWin.Ui_MainWindow()
    ui.setupUi(mw)
    mw.show()
    sys.exit(app.exec())
