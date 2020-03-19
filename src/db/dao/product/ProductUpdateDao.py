from src.db.dao.BaseCrudDao import BaseCrudDao
from src.model.Product import Product
from src.util.QueryStringFileUtil import query_update_product


class ProductUpdateDao(BaseCrudDao):
    def __init__(self):
        super()

    def update(self, product: Product):
        data = (product.description, product.ean, product.stock, product.price, product.url, str(product.cod))
        self.get_cursor().execute(query_update_product, data)
        self.commit()

