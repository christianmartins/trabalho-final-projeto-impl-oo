import sqlite3


class DBController:

    @staticmethod
    def get_connection():
        return sqlite3.connect("../finalproject.db")

    def get_cursor(self):
        return self.get_connection().cursor()
