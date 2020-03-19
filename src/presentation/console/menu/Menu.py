from src.presentation.console.menu.BaseMenu import BaseMenu
from src.util.StringFile import *


class Menu(BaseMenu):
    def __init__(self):
        super()

    def get_options_menu(self):
        return menu_options

    def get_msg_input(self):
        return menu_input

    def on_select_option(self):
        return "on action"
