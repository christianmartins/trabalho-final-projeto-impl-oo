from src.presentation.console.menu.BaseMenuMultipleOption import BaseMenuMultipleOption
from src.presentation.console.menu.MenuCreate import MenuCreate
from src.util.StringFileUtil import *


class Menu(BaseMenuMultipleOption):
    def __init__(self):
        super()
        super().__init__()

    def get_options_menu(self):
        return menu_options

    def get_msg_input(self):
        return menu_input

    def on_select_option(self, option):
        if option == 1:
            MenuCreate().init()
        if option == 1:
            MenuRead().init()
        else:
            self.show_message_invalid_input()
