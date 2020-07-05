class analyzer():
    def __init__(self, cname, target_grade):
        self.cname = cname
        self.total_lost_marks = 0.0
        self.traget_grade = target_grade

    def calculate_grade_needed(self):
        pass

    def comment_component(self, grade, weight, target): #grade in percent%, weight in percent%
        if grade is None:
            print("")
        elif grade<target:
            lostmark = (100-grade)*weight/100
            print("You have lost {0}% of the total mark in this component.".format(lostmark))
            self.total_lost_marks+=lostmark

    def comment_course(self):
        if self.total_lost_marks >= (100-self.traget_grade):
            print("Your goal is unrealistic, you are {0}% behind of your goal.".format(self.traget_grade-(100-self.total_lost_marks)))
        else:
            print("Your goal is achievable, you have lost {0}%.".format(self.total_lost_marks))
