from src.db.EntityController import EntityController
from src.presentation.PresentationView import PresentationView


class App:

    @staticmethod
    def start():
        EntityController.get_instance().create_entities()
        PresentationView().init()

    def main(self):
        self.start()
