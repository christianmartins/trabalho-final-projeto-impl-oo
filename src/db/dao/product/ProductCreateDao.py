from src.db.dao.BaseCrudDao import BaseCrudDao
from src.model import Product
from src.util.QueryStringFileUtil import query_create_table_product, query_insert_product


class ProductCreateDao(BaseCrudDao):
    def __init__(self):
        super()

    def create_table(self):
        self.get_cursor().execute(query_create_table_product)

    def insert(self, product: Product):
        data = (product.cod, product.description, product.ean, product.stock, product.price, product.url)
        self.get_cursor().execute(query_insert_product, data)
        self.commit()

