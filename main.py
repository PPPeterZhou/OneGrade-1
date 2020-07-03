import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication, QDesktopWidget


class OneGrade(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        menubar = self.menuBar()
        ActMenu = menubar.addMenu('Action')
        newAct = QAction('New', self)        

        ActMenu.addAction(newAct)

        
        self.resize(600, 400)
        self.center()
        self.setWindowTitle("OneGrade")
        self.show()
    
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    program = OneGrade()
    sys.exit(app.exec_())
