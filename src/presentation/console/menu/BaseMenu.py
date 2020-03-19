from abc import ABC

from src.util.StringFile import method_not_implemented


class BaseMenu:

    def init(self):
        self.__looping()

    def __looping(self):
        while True:
            self.show_options(self.get_options_menu())
            option_select = self.get_int_input(self.get_msg_input())
            print(option_select)
            if option_select == 0:
                break
            self.on_select_option()

    def get_options_menu(self):
        raise NotImplementedError(method_not_implemented)

    def get_msg_input(self):
        raise NotImplementedError(method_not_implemented)

    @staticmethod
    def show_options(options_text):
        print(options_text)

    @staticmethod
    def get_int_input(msg):
        try:
            return int(input(msg))
        except ValueError:
            return 0

    @staticmethod
    def on_select_option():
        raise NotImplementedError(method_not_implemented)

