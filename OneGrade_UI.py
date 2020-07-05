class OneGrade_UI():
    def __init__(self):
        self.course_format = "|{0:<15s}{1:^8}{2:^15}{3:^15}|"
        self.grade_format = "|{0:<15s}{1:^15}{2:^15}{3:^15}|"

    def welcome(self):
        print("\n            -------------------------------")
        print("           / Welcome to OneGrade System! /")
        print("           ------------------------------\n")

    def session_message(self):
        print("\n        --------------------------------------")
        print("       / Which Session Would You Like to See?/")
        print("       --------------------------------------\n")
        print("")

        print("\n           ------------------------------------------")
        print("          /         What Would You Like to Do?      /")
        print("         /     a: Add a Course in a New Session    /")
        print("        /      b: View a Session (e.g. 2020FALL)  /")
        print("        ------------------------------------------\n")
        print(" --------------------Session--------------------")

    def show_sessions(self, session_list):
        for session in session_list:
            print("|{0}|".format(str(session[0]).center(47)))
            print(" -----------------------------------------------")

    def take_cmd_message(self):
        print("\n            -----------------------------------------")
        print("           /       What Would You Like to Do?      /")
        print("          /    a: Check the Detail of the Course  /")
        print("         /     b: Add a New Course               /")
        print("        /      c: Delete a Course               /")
        print("       -----------------------------------------")

    def show_courses(self, courses_info):
        print("\n {0}Courses Information{0}".format("-"*17))
        print(self.course_format.format("Course", "Credits", "Session", "TargetGrade"))
        i = 0
        for course in courses_info:
            if i > 0:
                print(" {}".format("-"*54))
            print(self.course_format.format(course[0], course[1], course[2], course[3]))
            i += 1
        print(" {}".format("-"*54))

    def show_analysis(self, courses_details, analyze):
        print("\n {0}Courses Grades{0}".format(23*"-"))
        print(self.grade_format.format("Course", "Component", "Weight", "Grade"))
        print(" {}".format("-"*60))
        for detail in courses_details:
            if detail[3] is not None:
                print(self.grade_format.format(detail[0], detail[1], detail[2], detail[3]))
            else:
                print(self.grade_format.format(detail[0], detail[1], detail[2], "Unknown"))
            analyze.comment_component(detail[2], detail[3])
            print(" {}".format("-"*60))
            
        analyze.comment_course()