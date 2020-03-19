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
        self.createDao.create_table()
        print(self.readDao.get_list())

    def getCreateDao(self):
        return self.createDao

    def getReadDao(self):
        return self.readDao

    def getUpdate(self):
        return self.updateDao

    def getDelete(self):
        return self.deleteDao


