from src.db.DBController import DBController


class BaseCrudDao:
    db = DBController()

    def get_cursor(self):
        self.get_cursor()
