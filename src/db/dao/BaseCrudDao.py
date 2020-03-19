from src.db.DBConnection import DBConnection


class BaseCrudDao:
    __db = DBConnection()

    def get_connection(self):
        return self.__db.get_connection()

    def get_cursor(self):
        return self.__db.get_cursor()

    def commit(self):
        self.get_connection().commit()
