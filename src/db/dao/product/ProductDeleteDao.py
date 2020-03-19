from src.db.dao.BaseCrudDao import BaseCrudDao
from src.util.QueryStringFileUtil import query_delete_by_cod, query_delete_all_products


class ProductDeleteDao(BaseCrudDao):
    def __init__(self):
        super()

    def delete(self, cod):
        self.get_cursor().execute(query_delete_by_cod, str(cod))
        self.commit()

    def delete_all(self):
        self.get_cursor().execute(query_delete_all_products)
        self.commit()
