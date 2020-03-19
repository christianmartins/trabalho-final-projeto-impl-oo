import sqlite3

from src.db.EntityController import EntityController
from src.presentation.console.menu.BaseMenuMultipleOption import BaseMenuMultipleOption
from src.util import StringFileUtil
from src.util.StringFileUtil import delete_all_msg, menu_input, delete_title_options


class MenuDelete(BaseMenuMultipleOption):

    def __init__(self):
        super()
        super().__init__()

    def get_options_menu(self):
        return delete_title_options

    def get_msg_input(self):
        return menu_input

    def on_select_option(self, option):
        if option == 1:
            self.delete_product_by_cod()
        elif option == 2:
            self.delete_all_products()
        else:
            self.show_message_invalid_input()

    def delete_product_by_cod(self):
        cod = self.get_int_input(StringFileUtil.input_msg_product_cod)
        return self.on_delete_product_by_cod(cod)

    def on_delete_product_by_cod(self, cod):
        try:
            cod_has_exists = self.get_read_dao().check_cod_not_exists(cod)
            if cod_has_exists:
                print(StringFileUtil.cod_not_exists)
            else:
                self.get_delete_dao().delete(cod)
                self.is_continue = False
                print(StringFileUtil.successful_execute)
        except sqlite3.Error:
            print(StringFileUtil.failed_execute)

    def delete_all_products(self):
        print(delete_all_msg)
        try:
            self.get_delete_dao().delete_all()
            self.is_continue = False
        except sqlite3.Error:
            print(StringFileUtil.failed_execute)

    @staticmethod
    def get_delete_dao():
        return EntityController.get_instance().get_product_dao().get_delete()

    @staticmethod
    def get_read_dao():
        return EntityController.get_instance().get_product_dao().get_read()
