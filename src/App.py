from src.db import EntityController
from src.presentation.PresentationView import PresentationView


class App:

    def main(self):
        self.__start()

    @staticmethod
    def __start():
        EntityController.create_entities()
        PresentationView().init()
