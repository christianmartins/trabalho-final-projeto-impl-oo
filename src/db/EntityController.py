from src.db.dao.product.ProductDao import ProductDao


class EntityController:

    @staticmethod
    def create_entities():
        ProductDao().start()
