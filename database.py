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
                            session     char(16)\
                            );\
                            ")

if __name__ == '__main__':
    db = DBase()