from src.db.dao.BaseCrudDao import BaseCrudDao
from src.util.QueryStringFileUtil import query_select_product


class ProductReadDao(BaseCrudDao):
    def __init__(self):
        super()

    def get_list(self):
        return self.__get_list(query_select_product)

    def __get_list(self, query):
        self.get_cursor().execute(query)
        return self.get_cursor().fetchall()

