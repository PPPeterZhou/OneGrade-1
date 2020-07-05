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
                            cname     char(16),\
                            credits     int,\
                            session     char(16),\
                            TargetGrade     int,\
                            PRIMARY KEY (cname) \
                            );")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS CourseGrade(\
                            cname     char(16),\
                            Component   char(16),\
                            Weight      float,\
                            Grade       float,\
                            PRIMARY KEY (cname, Component),\
                            FOREIGN KEY (cname) references CourseInfo\
                            ON DELETE CASCADE\
                            );")
        self.conn.commit()

    def insert_course(self, cname, credit, session, TargetGrade):
        cname = cname.upper()
        session = session.upper()
        if not self.isCourseAdded(cname):
            self.cursor.execute("INSERT INTO CourseInfo VALUES\
                 (?, ?, ?, ?);", (cname, credit, session, TargetGrade))
            self.conn.commit()

    def delete_course(self, cname):
        cname = cname.upper()
        session = session.upper()
        if self.isCourseAdded(cname):
            self.cursor.execute("DELETE FROM CourseInfo \
            WHERE cname=:cname;", {"cname":cname})
            self.conn.commit()
    
    def isCourseAdded(self, cname):
        cname = cname.upper()
        self.cursor.execute("SELECT * FROM CourseInfo \
        WHERE cname=:cname;", {"cname":cname})
        rows = self.cursor.fetchall()
        if rows:
            return True
        else:
            return False
    
    def retrieveSessions(self):
        self.cursor.execute("SELECT distinct session FROM CourseInfo order by session;",)
        rows = self.cursor.fetchall()
        return rows

    def retrieveCourseInfoData(self, session):
        self.cursor.execute("SELECT * FROM CourseInfo WHERE session=:session;", {"session":session})
        rows = self.cursor.fetchall() # each course info
        return rows

    def retrieveCourseGradeData(self, cname):
        self.cursor.execute("SELECT * FROM CourseGrade WHERE cname=:cname\
            ;", {"cname":cname})
        rows = self.cursor.fetchall()
        return rows
    
    def isComponentAdded(self, cname, Component):
        self.cursor.execute("SELECT * FROM CourseGrade \
        WHERE cname=:cname \
        AND Component=:Component;", {"cname":cname, "Component":Component})
        rows = self.cursor.fetchall()
        if rows:
            return True
        else:
            return False

    def insert_component(self, cname, Component, Weight, Grade=None):
        if not self.isComponentAdded(cname, Component) and self.isCourseAdded(cname):
            self.cursor.execute("INSERT INTO CourseGrade VALUES\
                 (?, ?, ?, ?);", (cname, Component, Weight, Grade))
            self.conn.commit()
    
    def delete_component(self, cname, Component):
        if self.isComponentAdded(cname, Component):
            self.cursor.execute("DELETE FROM CourseGrade \
            WHERE cname=:cname AND \
                Component=:Component;", {"cname":cname, "Component":Component})
            self.conn.commit()
    
    def clear_database(self):
        self.cursor.execute("DELETE FROM CourseInfo;")
        self.conn.commit()

    def isSessionEmpty(self, session):
        session = session.upper()
        self.cursor.execute("SELECT * FROM CourseInfo WHERE session=:session;", {"session":session})
        rows = self.cursor.fetchall()
        if rows:
            return False
        else:
            return True

    def get_target_grade(self, cname):
        self.cursor.execute("SELECT TargetGrade FROM CourseInfo WHERE cname=:cname;", {"cname":cname})
        row = self.cursor.fetchone()
        return row[0]

if __name__ == '__main__':
    db = DBase()
    db.insert_course("MATH217", 3, "2020FALL", 90)
    db.insert_course("MATH317", 3, "2020FALL", 89)
    db.insert_course("MATH417", 3, "2020FALL", 88)
    db.insert_course("MATH418", 3, "2020Winter", 88)
    db.insert_component("MATH217", "Midterm", 20, 100)
    db.insert_component("MATH217", "Midterm2", 20, 99)
    db.insert_component("MATH317", "Midterm2", 50, 99)
    db.insert_component("MATH317", "Midterm2", 20, 99)
    db.insert_component("MATH217", "Final", 60)
