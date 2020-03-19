from src.db.dao.product.ProductCreateDao import ProductCreateDao
from src.db.dao.product.ProductDeleteDao import ProductDeleteDao
from src.db.dao.product.ProductReadDao import ProductReadDao
from src.db.dao.product.ProductUpdateDao import ProductUpdateDao


class ProductDao:
    __createDao = ProductCreateDao()
    __readDao = ProductReadDao()
    __updateDao = ProductUpdateDao()
    __deleteDao = ProductDeleteDao()

    def start(self):
        self.get_create().create_table()

    def get_create(self):
        return self.__createDao

    def get_read(self):
        return self.__readDao

    def get_update(self):
        return self.__updateDao

    def get_delete(self):
        return self.__deleteDao


