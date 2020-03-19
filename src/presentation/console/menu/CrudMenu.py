from src.util.StringFile import *


class CrudMenu:

    def init(self):
        self.__looping()

    def __looping(self):
        while True:
            self.__show_options()
            option_select = self.__get_input()
            if option_select == 0:
                break
            self.__on_select_option()

    @staticmethod
    def __on_select_option():
        print("test")

    @staticmethod
    def __show_options():
        print(menu_options)

    @staticmethod
    def __get_input():
        try:
            return int(input(menu_input))
        except NameError:
            return 0
