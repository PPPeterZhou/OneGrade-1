import sqlite3
import os

class DBase():
    def __init__(self):
        self.conn = sqlite3.connect('./grades.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS CourseInfo(\
                            cname     char(8),\
                            cnumber     int,\
                            credits     int,\
                            session     char(16),\
                            TargetGrade     int,\
                            PRIMARY KEY (cname, cnumber)\
                            );\
                            ")
        self.conn.commit()

    def insert_course(self, cname, cnumber, credit, session, TargetGrade):
        if not self.isCourseAdded(cname, cnumber):
            self.cursor.execute("INSERT INTO CourseInfo VALUES (?, ?, ?, ?, ?);", (cname, cnumber, credit, session, TargetGrade))
            self.conn.commit()

    def delete_course(self, cname, cnumber):
        if self.isCourseAdded(cname, cnumber):
            self.cursor.execute("DELETE FROM CourseInfo \
            WHERE cname=:cname AND cnumber=:cnumber;", {"cname":cname, "cnumber":cnumber})
            self.conn.commit()
    
    def isCourseAdded(self, cname, cnumber):
        self.cursor.execute("SELECT * FROM CourseInfo \
        WHERE cname=:cname AND cnumber=:cnumber;", {"cname":cname, "cnumber":cnumber})
        rows = self.cursor.fetchall()
        if rows:
            return True
        else:
            return False
    
    def clear_database(self):
        self.cursor.execute("DELETE FROM CourseInfo;")
        self.conn.commit()


if __name__ == '__main__':
    db = DBase()
    db.insert_course("MATH", 217, 3, "2020FALL", 90)
    db.insert_course("MATH", 317, 3, "2020FALL", 89)
    db.insert_course("MATH", 417, 3, "2020FALL", 88)
