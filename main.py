import analyzer
import sqlite3
import time, sys
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
        while True:
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

        for session in session_list:
            print("|{0}|".format(str(session).center(47)))
            print(" -----------------------------------------------")

        while True:
            session_chosen = input(": ").upper()
            if session_chosen=="Q":
                sys.exit()
            elif self.db.isSessionEmpty(session_chosen):
                print("Invalid session.")
                continue
            else:
                break

        self.command(session_chosen)

    def show_courses(self, session):
        courses_info = self.db.retrieveCourseInfoData()

        print("\n ----------------Courses Information--------------")
        print("|Course      Credits      Session      TargetGrade|")
        for course in courses_info:
            if course[3] == session:
                print("|{0:<12s}{1}{2}{3}|".format(course[0]+str(course[1]), str(course[2]).center(8), str(course[3]).center(20), str(course[4]).center(9)))
                print(" -------------------------------------------------")

    def command(self, session):
        courses_info = self.db.retrieveCourseInfoData()
        course_list = []
        for course in courses_info:
            if course[3] == session:
                course_list.append(course[0] + str(course[1]))
        course_list = list(dict.fromkeys(course_list))

        while True:
            self.show_courses(session)
            print("\n            -----------------------------------------")
            print("           /       What Would You Like to Do?      /")
            print("          /    a: Check the Detail of the Course  /")
            print("         /     b: Add a new Course               /")
            print("        -----------------------------------------")
            user_command = input(": ").lower()
            if user_command == "a":
                while True:
                    course_to_check = input("Which Course: ").upper()
                    if course_to_check not in course_list:
                        print("Invalid Input!")
                    else:
                        self.courseDetail(course_to_check)
                    break
            elif user_command == "b":
                self.addCourse(session)
                continue
            elif user_command == "q":
                break
            else:
                print("Invalid Input!")

    def courseDetail(self, course):
        while True:
            courses_details = self.db.retrieveCourseGradeData()
            print("\n -----------------Courses Grade--------------------")
            print("|Course        Component        Weight        Grade|")
            for detail in courses_details:
                if course == (detail[0] + str(detail[1])):
                    print("|%s        %s          %s         %s|" % (course, detail[2], detail[3], detail[4]))
            print(" --------------------------------------------------")
            print("You may add a course component by command 'a'.")
            user_input = input(": ").lower()
            if user_input == "q":
                break
            else:
                continue



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