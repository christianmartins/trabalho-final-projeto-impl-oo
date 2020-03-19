from src.db.DBConnection import DBConnection
from src.db.dao.product.ProductDao import ProductDao


class EntityController:
    _instance = None
    __product_dao = ProductDao()
    __db = DBConnection()

    def __init__(self):
        self.some_attribute = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def create_entities(self):
        self.__product_dao.start()

    def get_product_dao(self):
        return self.__product_dao

    def get_db(self):
        return self.__db
