from src.db.dao.BaseCrudDao import BaseCrudDao
from src.util.QueryStringFileUtil import query_select_product, query_check_product_id_has_exists


class ProductReadDao(BaseCrudDao):
    def __init__(self):
        super()

    def check_cod_has_exists(self, cod):
        self.get_cursor().execute(query_check_product_id_has_exists, str(cod))
        return self.get_cursor().fetchone()[0] > 0

    def get_list(self):
        return self.__get_list(query_select_product)

    def __get_list(self, query):
        self.get_cursor().execute(query)
        return self.get_cursor().fetchall()

