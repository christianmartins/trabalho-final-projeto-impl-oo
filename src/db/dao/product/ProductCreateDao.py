from src.db.dao.BaseCrudDao import BaseCrudDao
from src.util.QueryStringFile import query_create_table_product


class ProductCreateDao(BaseCrudDao):
    def __init__(self):
        super()

    def create_table(self):
        self.db.get_cursor().execute(query_create_table_product)
