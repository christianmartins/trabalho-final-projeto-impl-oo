from src.presentation.console.menu.BaseMenu import BaseMenu
from src.util import InputUtil
from src.util.StringFileUtil import method_not_implemented


class BaseMenuMultipleOption(BaseMenu):
    is_continue = True

    def __init__(self):
        super()

    def onInit(self):
        self.__looping()

    def __looping(self):
        while self.is_continue:
            self.show_options(self.get_options_menu())
            option_select = self.get_int_input(self.get_msg_input())
            if option_select == 0:
                self.finish_application()
            self.on_select_option(option_select)

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
    def on_select_option(option):
        raise NotImplementedError(method_not_implemented)
