import sqlite3
import os

class DBase():
    def __init__(self):
        self.conn = sqlite3.connect('./grades.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("PRAGMA foreign_keys=on;")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS CourseInfo(\
                            cname     char(8),\
                            cnumber     int,\
                            credits     int,\
                            session     char(16),\
                            TargetGrade     int,\
                            PRIMARY KEY (cname, cnumber)\
                            );")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS CourseGrade(\
                            cname     char(8),\
                            cnumber     int,\
                            Component   char(16),\
                            Weight      float,\
                            Grade       float,\
                            PRIMARY KEY (cname, cnumber, Component),\
                            FOREIGN KEY (cname, cnumber) references CourseInfo\
                            ON DELETE CASCADE\
                            );")
        self.conn.commit()

    def insert_course(self, cname, cnumber, credit, session, TargetGrade):
        if not self.isCourseAdded(cname, cnumber):
            self.cursor.execute("INSERT INTO CourseInfo VALUES\
                 (?, ?, ?, ?, ?);", (cname, cnumber, credit, session, TargetGrade))
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
    
    def isComponentAdded(self, cname, cnumber, Component):
        self.cursor.execute("SELECT * FROM CourseGrade \
        WHERE cname=:cname AND cnumber=:cnumber \
        AND Component=:Component;", {"cname":cname, "cnumber":cnumber, "Component":Component})
        rows = self.cursor.fetchall()
        if rows:
            return True
        else:
            return False

    def insert_component(self, cname, cnumber, Component, Weight, Grade=None):
        if not self.isComponentAdded(cname, cnumber, Component) and self.isCourseAdded(cname, cnumber):
            self.cursor.execute("INSERT INTO CourseGrade VALUES\
                 (?, ?, ?, ?, ?);", (cname, cnumber, Component, Weight, Grade))
            self.conn.commit()
    
    def delete_component(self, cname, cnumber, Component):
        if self.isComponentAdded(cname, cnumber, Component):
            self.cursor.execute("DELETE FROM CourseGrade \
            WHERE cname=:cname AND cnumber=:cnumber AND \
                Component=:Component;", {"cname":cname, "cnumber":cnumber, "Component":Component})
            self.conn.commit()
    
    def clear_database(self):
        self.cursor.execute("DELETE FROM CourseInfo;")
        self.conn.commit()


if __name__ == '__main__':
    db = DBase()
    db.insert_course("MATH", 217, 3, "2020FALL", 90)
    db.insert_course("MATH", 317, 3, "2020FALL", 89)
    db.insert_course("MATH", 417, 3, "2020FALL", 88)
    db.insert_component("MATH", 217, "Midterm", 50, 100)
    db.insert_component("MATH", 217, "Midterm2", 50, 99)
    db.insert_component("MATH", 317, "Midterm2", 50, 99)
    db.insert_component("MATH", 317, "Midterm2", 50, 99)
    db.delete_component("MATH", 217, "Midterm2")
