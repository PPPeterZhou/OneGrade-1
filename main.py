import sys, database
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication, QDesktopWidget, QInputDialog

class OneGrade(QMainWindow):

    def __init__(self):
        super().__init__()
        self.db = database.DBase()
        self.initUI()


    def initUI(self):
        menubar = self.menuBar()
        ActMenu = menubar.addMenu('Action')
        newClassAct = QAction('Add Class', self)
        ActMenu.addAction(newClassAct)
        newClassAct.triggered.connect(self.showDialog)
        
        self.resize(600, 400)
        self.center()
        self.setWindowTitle("OneGrade")
        self.show()
    
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    program = OneGrade()
    sys.exit(app.exec_())
