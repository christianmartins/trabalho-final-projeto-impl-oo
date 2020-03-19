import sqlite3

from src.db.EntityController import EntityController
from src.model.Product import Product
from src.presentation.console.menu.BaseMenu import BaseMenu
from src.util import StringFileUtil


class MenuUpdate(BaseMenu):
    def __init__(self):
        super()

    def onInit(self):
        self.update()

    def update(self):
        cod = self.get_int_input(StringFileUtil.input_msg_product_cod)
        cod_has_exists = self.check_cod(cod)
        if cod_has_exists:
            product = self.create_product(cod)
            self.execute_update_product(product)
        else:
            print(StringFileUtil.cod_not_exists)

    def check_cod(self, cod):
        try:
            return self.get_read_dao().check_cod_has_exists(cod)
        except sqlite3.Error:
            return False

    def create_product(self, cod):
        description = self.get_string_input(StringFileUtil.input_msg_product_description)
        ean = self.get_string_input(StringFileUtil.input_msg_product_ean)
        stock = self.get_int_input(StringFileUtil.input_msg_product_stock)
        price = self.get_double_input(StringFileUtil.input_msg_product_price)
        url = self.get_string_input(StringFileUtil.input_msg_product_url)
        return Product(cod, description, ean, stock, price, url)

    def execute_update_product(self, product: Product):
        try:
            self.get_update_dao().update(product)
            print(StringFileUtil.successful_execute)
        except sqlite3.Error:
            print(StringFileUtil.failed_execute)

    @staticmethod
    def get_update_dao():
        return EntityController.get_instance().get_product_dao().get_update()

    @staticmethod
    def get_read_dao():
        return EntityController.get_instance().get_product_dao().get_read()
