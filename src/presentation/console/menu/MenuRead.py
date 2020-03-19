from src.db.EntityController import EntityController
from src.model.Product import Product
from src.presentation.console.menu.BaseMenu import BaseMenu
from src.util import StringFileUtil


class MenuRead(BaseMenu):
    def __init__(self):
        super()

    def onInit(self):
        self.show_all()

    def show_all(self):
        print(StringFileUtil.all_title_list)
        products = self.get_read_dao().get_list()
        self.iterator(products)

    @staticmethod
    def get_read_dao():
        return EntityController.get_instance().get_product_dao().get_read()

    def iterator(self, list_data):
        for data in list_data:
            product = self.convert_to_product(data)
            self.beautiful_text(product)

    @staticmethod
    def convert_to_product(data):
        return Product(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4],
            data[5],
        )

    def beautiful_text(self, product):
        print(
            self.safe_text("Codigo: ", product.cod)
            + self.safe_text(", Descrição: ", product.description)
            + self.safe_text(", Codigo de barra: ", product.ean)
            + self.safe_text(", Estoque: ", product.stock)
            + self.safe_text(", Preço: ", product.price)
            + self.safe_text(", Url da imagem: ", product.url)
        )

    @staticmethod
    def safe_text(text, value):
        return text + str(value)
