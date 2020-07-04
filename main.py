import analyzer
import sqlite3
import time
from database import DBase

class OneGrade():
    def __init__(self, path):
        self.db = DBase()


    def connect(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return

    def show_dashboard(self):
        self.welcome()
        self.chooseSession()

    def welcome(self):
        print("\n            -------------------------------")
        print("           / Welcome to OneGrade System! /")
        print("           ------------------------------\n")

    def chooseSession(self):
        courses_info = self.db.retrieveCourseInfoData()
        print("\n        --------------------------------------")
        print("       / Which Session Would You Like to See?/")
        print("       --------------------------------------\n")
        print("")
        print(" --------------------Session--------------------")

        session_list = []
        for course in courses_info:
            session_list.append(course[3])
        session_list = list(dict.fromkeys(session_list))

        session = ""
        for element in session_list:
            session += (element + "   ")
        print("|  " + session + "  |")

        print(" -----------------------------------------------")
        session_chosen = input("I choose: ")

        self.show_courses(session_chosen)

    def show_courses(self, session):
        courses_info = self.db.retrieveCourseInfoData()

        print("\n -----------------Courses Information---------------")
        print("|Course       Credits      Session      Target Grade|")
        for course in courses_info:
            if course[3].upper() == session.upper():
                print("|%s%s         %s         %s          %s     |" % (course[0], course[1], course[2], course[3], course[4]))
        print(" ---------------------------------------------------")
        self.command(session.upper())

    def command(self, session):
        courses_info = self.db.retrieveCourseInfoData()
        course_list = []
        for course in courses_info:
            if course[3].upper() == session.upper():
                course_list.append((course[0] + str(course[1])).upper())
        course_list = list(dict.fromkeys(course_list))

        print("\n            -----------------------------------------")
        print("           /       What Would You Like to Do?      /")
        print("          /    a: Check the Detail of the Course  /")
        print("         /     b: Add a new Course               /")
        print("        -----------------------------------------")
        user_command = input("I want to: ")
        while True:
            if user_command == "a":
                while True:
                    course_to_check = input("Which Course: (e.g. MATH217) ")
                    if course_to_check.upper() not in course_list:
                        print("Invalid Input!")
                    else:
                        self.courseDetail(course_to_check.upper())
                        break
                break
            elif user_command == "b":
                self.addCourse(session)
                break
            else:
                print("Invalid Input!")

    def courseDetail(self, course):
        courses_details = self.db.retrieveCourseGradeData()
        print("\n -----------------Courses Grade--------------------")
        print("|Course        Component        Weight        Grade|")
        for detail in courses_details:
            if course == (detail[0] + str(detail[1])):
                print("|%s        %s          %s         %s|" % (course, detail[2], detail[3], detail[4]))
        print(" --------------------------------------------------")


    def addCourse(self, session):
        cname = input("Course Name: ")
        cnumber = input("Course Number: ")
        credit = input("Course Credit(s): ")
        target_grade = input("Course Target Grade: ")
        self.db.insert_course(cname, cnumber, credit, session, target_grade)


def main():
    path = "./grades.db"
    program = OneGrade(path)
    program.show_dashboard()

if __name__ == '__main__':
    main()