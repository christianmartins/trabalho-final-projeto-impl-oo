import sqlite3


class DBConnection:
    __con = sqlite3.connect("../finalproject.db")
    __cursor = __con.cursor()

    def get_connection(self):
        return self.__con

    def get_cursor(self):
        return self.__cursor

    def close(self):
        return self.close()
