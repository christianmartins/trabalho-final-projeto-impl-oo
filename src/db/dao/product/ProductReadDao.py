from src.db.dao.BaseCrudDao import BaseCrudDao
from src.util.QueryStringFile import queryselectproduct


class ProductReadDao(BaseCrudDao):

    def get_list(self):
        return self.__get_list(queryselectproduct)

    def __get_list(self, query):
        self.get_cursor().execute(query)
        return self.get_cursor().fetchall()

