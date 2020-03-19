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
        self.getCreate().create_table()
        print(self.getRead().get_list())

    def getCreate(self):
        return self.createDao

    def getRead(self):
        return self.readDao

    def getUpdate(self):
        return self.updateDao

    def getDelete(self):
        return self.deleteDao


