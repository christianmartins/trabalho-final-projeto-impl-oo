from src.db.dao.product import ProductDao


class EntityController:

    @staticmethod
    def create_entities():
        ProductDao.start()
