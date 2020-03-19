from src.db.dao.product.ProductCreateDao import ProductCreateDao
from src.db.dao.product.ProductDeleteDao import ProductDeleteDao
from src.db.dao.product.ProductReadDao import ProductReadDao
from src.db.dao.product.ProductUpdateDao import ProductUpdateDao


class ProductDao:
    createDao = ProductCreateDao()
    readDao = ProductReadDao()
    updateDao = ProductUpdateDao()
    deleteDao = ProductDeleteDao()

    def start(self):
        self.get_create().create_table()

    def get_create(self):
        return self.createDao

    def get_read(self):
        return self.readDao

    def get_update(self):
        return self.updateDao

    def get_delete(self):
        return self.deleteDao


