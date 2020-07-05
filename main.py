import sqlite3
import time, sys
from database import DBase
from analyzer import analyzer
from OneGrade_UI import OneGrade_UI

class OneGrade():
    def __init__(self):
        self.db = DBase()
        self.ui = OneGrade_UI()

    def chooseSession(self):
        while True:
            session_list = self.db.retrieveSessions()
            self.ui.session_message()
            self.ui.show_sessions(session_list)
            session_chosen = input(": ").upper()

            if session_chosen=="Q":
                sys.exit()
            elif self.db.isSessionEmpty(session_chosen):
                print("Invalid session.")
                continue
            else:
                break

        return session_chosen

    def isCourseInSession(self, course_selected, courses_info):
        course_list = []
        for course in courses_info:
            course_list.append(course[0])
        course_list = list(dict.fromkeys(course_list))
        return (course_selected in course_list)

    def addCourse(self, session):
        cname = input("Course Name: ")
        credit = input("Course Credit(s): ")
        target_grade = input("Course Target Grade: ")
        self.db.insert_course(cname, credit, session, target_grade)

    def start_program(self):
        self.ui.welcome()
        while True:
            session_chosen = self.chooseSession()
            while True:
                course_selected = self.command(session_chosen)
                if course_selected:
                    self.courseDetail(session_chosen, course_selected)
                elif course_selected is None:
                    break

    def command(self, session):
        while True:
            courses_info = self.db.retrieveCourseInfoData(session)
            self.ui.show_courses(courses_info)
            self.ui.take_cmd_message()
            user_command = input(": ").lower()

            if user_command == "a":
                course_to_check = input("Which Course: ").upper()
                if not self.isCourseInSession(course_to_check, courses_info):
                    print("Course not found in this session!")
                else:
                    return course_to_check
            elif user_command == "b":
                self.addCourse(session)
                continue
            elif user_command == "q":
                return None
            else:
                print("Invalid Input!")
                continue

    def courseDetail(self, session, cname):
        while True:
            self.component_analysis(cname)
            user_cmd = input("You may add a course component by command 'a'.\n: ").lower()
            if user_cmd == "a":
                pass
            elif user_cmd == "b":
                pass
            elif user_cmd == "q":
                break

    def component_analysis(self, cname):
        target_grade = self.db.get_target_grade(cname)
        grade_details = self.db.retrieveCourseGradeData(cname)

        analyze = analyzer(cname, target_grade, grade_details)
        self.ui.show_analysis(grade_details, analyze)

    def add_component(self, cname, component):
        pass


def main():
    program = OneGrade()
    program.start_program()

if __name__ == '__main__':
    main()