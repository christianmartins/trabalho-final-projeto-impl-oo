import sqlite3

from src.db.EntityController import EntityController
from src.model.Product import Product
from src.presentation.console.menu.BaseMenu import BaseMenu
from src.util import StringFileUtil


class MenuCreate(BaseMenu):
    def __init__(self):
        super()

    def onInit(self):
        product = self.create_product()
        self.save_product(product)

    def create_product(self):
        cod = self.get_int_input(StringFileUtil.input_msg_product_cod)
        description = self.get_string_input(StringFileUtil.input_msg_product_description)
        ean = self.get_string_input(StringFileUtil.input_msg_product_ean)
        stock = self.get_int_input(StringFileUtil.input_msg_product_stock)
        price = self.get_double_input(StringFileUtil.input_msg_product_price)
        url = self.get_string_input(StringFileUtil.input_msg_product_url)
        return Product(cod, description, ean, stock, price, url)

    def save_product(self, product: Product):
        try:
            cod_has_exists = self.get_read_dao().check_cod_has_exists(product.cod)
            if cod_has_exists:
                print(StringFileUtil.cod_has_exists)
            else:
                self.get_create_dao().insert(product)
                print(StringFileUtil.successful_save)
        except sqlite3.Error:
            print(StringFileUtil.failed_save)

    @staticmethod
    def get_create_dao():
        return EntityController.get_instance().get_product_dao().get_create()

    @staticmethod
    def get_read_dao():
        return EntityController.get_instance().get_product_dao().get_read()