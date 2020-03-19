from src.db.EntityController import EntityController


class BaseCrudDao:
    __entity_controller = EntityController.get_instance()

    def get_connection(self):
        return self.__entity_controller.get_db().get_connection()

    def get_cursor(self):
        return self.get_connection().get_cursor()

    def commit(self):
        self.get_connection().commit()
