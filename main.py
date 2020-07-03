import sys
import datetime
from PyQt5.QtWidgets import (QMainWindow, QAction, QMenu, QApplication, QDesktopWidget, QInputDialog)
from PyQt5 import QtWidgets
from database import DBase

class OneGrade(QMainWindow):

    def __init__(self):
        super().__init__()
        self.db = DBase()
        self.initUI()


    def initUI(self):
        menubar = self.menuBar()
        ActMenu = menubar.addMenu('Action')
        newAct = QAction('New', self)        
        ActMenu.addAction(newAct)

        newAct.triggered.connect(self.showCourseInfoDialog)
        
        self.resize(600, 400)
        self.center()
        self.setWindowTitle("OneGrade")
        self.show()
    
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showCourseInfoDialog(self):
        
        course_code, course_code_ok  = QInputDialog.getText(self, 'Course Infomation', 
            'Course Code: ')

        if course_code_ok:
            course_number, course_number_ok  = QInputDialog.getText(self, 'Course Infomation', 
            'Course Number: ')

        if course_number_ok:
            course_target, course_target_ok  = QInputDialog.getText(self, 'Course Infomation', 
            'Course Target: ')
        
        if course_target_ok:
            course_credit, course_credit_ok  = QInputDialog.getText(self, 'Course Infomation', 
            'Course Credit(s): ')

        if course_credit_ok:
            year = datetime.datetime.now().year
            langs =[str(year) + 'Winter', str(year) + 'Spring', str(year) + 'Summer', str(year) + 'Fall', str(year+1) + 'Winter', str(year+1) + 'Spring', str(year+1) + 'Summer', str(year+1) + 'Fall'] 
            course_session, course_session_ok = QtWidgets.QInputDialog.getItem(self, 'Course Infomation', 'Course Session:', langs) 

        course_info = [course_code, course_number, course_target, course_credit, course_session]
        # print('Course Code: %s\nCourse Number: %s\nCredit(s): %s \nSession: %s \n' % (course_code, course_number, course_credit, course_session))
        # print(course_info)
        self.storeCourseInfo(course_info)

    def storeCourseInfo(self, course_info):
        self.db.insert_course(course_info[0], course_info[1], course_info[2], course_info[3], course_info[4])
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    program = OneGrade()
    sys.exit(app.exec_())
