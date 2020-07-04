import sys, datetime, database
from PyQt5.QtWidgets import (QMainWindow, QAction, QMenu, QApplication, QDesktopWidget, QInputDialog, QLabel)
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
        self.refresh()
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
            'Course Number(100-999): ')

        if course_number_ok:
            course_target, course_target_ok  = QInputDialog.getText(self, 'Course Infomation', 
            'Course Target(0-100): ')
        
        if course_target_ok:
            course_credit, course_credit_ok  = QInputDialog.getText(self, 'Course Infomation', 
            'Course Credit(s)(0-10): ')

        if course_credit_ok:
            year = datetime.datetime.now().year
            sessions = [str(year) + 'Winter', str(year) + 'Spring', str(year) + 'Summer', str(year) + 'Fall', str(year+1) + 'Winter', str(year+1) + 'Spring', str(year+1) + 'Summer', str(year+1) + 'Fall'] 
            course_session, course_session_ok = QtWidgets.QInputDialog.getItem(self, 'Course Infomation', 'Course Session:', sessions) 

        course_info = [course_code, course_number, course_target, course_credit, course_session]
        # print('Course Code: %s\nCourse Number: %s\nCredit(s): %s \nSession: %s \n' % (course_code, course_number, course_credit, course_session))
        # print(course_info)
        self.storeCourseInfo(course_info)

    def storeCourseInfo(self, course_info):
        self.db.insert_course(course_info[0], course_info[1], course_info[2], course_info[3], course_info[4])
        self.refresh()

    def refresh(self):
        y = 0
        course_infos = self.db.retrieveData()
        for course_info in course_infos:
            label = QLabel('Course Code: %s\nCourse Number: %s\nCourse Target: %s\nCredit(s): %s \nSession: %s \n' % (course_info[0], course_info[1], course_info[2], course_info[3], course_info[4]), self)
            label.resize(500, 100)
            label.move(10, 100 * y)
            y += 1
            print(y)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    program = OneGrade()
    sys.exit(app.exec_())
