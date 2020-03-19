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
        cod = self.get_string_input(StringFileUtil.input_msg_product_cod)
        description = self.get_string_input(StringFileUtil.input_msg_product_description)
        ean = self.get_string_input(StringFileUtil.input_msg_product_ean)
        stock = self.get_int_input(StringFileUtil.input_msg_product_stock)
        price = self.get_double_input(StringFileUtil.input_msg_product_price)
        url = self.get_string_input(StringFileUtil.input_msg_product_price)
        return Product(cod, description, ean, stock, price, url)

    def save_product(self, product):
        print("TODO", product)
