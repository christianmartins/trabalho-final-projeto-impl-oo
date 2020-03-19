from src.presentation.console.menu.BaseMenu import BaseMenu
from src.util import InputUtil
from src.util.StringFileUtil import method_not_implemented, finish_application


class BaseMenuMultipleOption(BaseMenu):
    def __init__(self):
        super()

    def onInit(self):
        self.__looping()

    def __looping(self):
        while True:
            self.show_options(self.get_options_menu())
            option_select = self.get_int_input(self.get_msg_input())
            if option_select == 0:
                self.show_message_on_finish_application()
                break
            self.on_select_option()

    @staticmethod
    def show_options(options_text):
        print(options_text)

    def get_options_menu(self):
        raise NotImplementedError(method_not_implemented)

    @staticmethod
    def get_int_input(msg):
        return InputUtil.get_int_input(msg)

    def get_msg_input(self):
        raise NotImplementedError(method_not_implemented)

    @staticmethod
    def on_select_option():
        raise NotImplementedError(method_not_implemented)

    @staticmethod
    def show_message_on_finish_application():
        print(finish_application)

