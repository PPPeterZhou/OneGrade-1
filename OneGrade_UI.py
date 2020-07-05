class OneGrade_UI():
    def __init__(self):
        pass

    def welcome(self):
        print("\n            -------------------------------")
        print("           / Welcome to OneGrade System! /")
        print("           ------------------------------\n")

    def session_message(self):
        print("\n        --------------------------------------")
        print("       / Which Session Would You Like to See?/")
        print("       --------------------------------------\n")
        print("")
        print(" --------------------Session--------------------")

    def show_sessions(self, session_list):
        for session in session_list:
            print("|{0}|".format(str(session[0]).center(47)))
            print(" -----------------------------------------------")

    def take_cmd_message(self):
        print("\n            -----------------------------------------")
        print("           /       What Would You Like to Do?      /")
        print("          /    a: Check the Detail of the Course  /")
        print("         /     b: Add a new Course               /")
        print("        -----------------------------------------")

    def show_courses(self, courses_info):
        print("\n ----------------Courses Information--------------")
        print("|Course      Credits      Session      TargetGrade|")
        for course in courses_info:
            print("|{0:<12s}{1:^12}{2:^12}{3:^12}|".format(course[0], course[1], course[2], course[3]))
            print(" -------------------------------------------------")

    def show_analysis(self, courses_details):
        print("\n {0}Courses Grade{0}".format(18*"-"))
        print("|{0:<12}{1:^12}{2:^12}{3:^12}|".format("Course", "Component", "Weight", "Grade"))
        for detail in courses_details:
            print("|{0:<12}{1:^12}{2:^12}{3:^12}|".format(detail[0], detail[1], detail[2], detail[3]))
        print(" {}".format("-"*49))