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

    def __on_select_option(self):
        print("test")

    def __show_options(self):
        print(menu_options)

    def __get_input(self):
        try:
            return int(input(menu_input))
        except NameError:
            return 0
