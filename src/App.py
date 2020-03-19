from src.db.EntityController import EntityController
from src.presentation.PresentationView import PresentationView


class App:

    @staticmethod
    def start():
        EntityController().create_entities()
        PresentationView().init()

    def main(self):
        self.start()
