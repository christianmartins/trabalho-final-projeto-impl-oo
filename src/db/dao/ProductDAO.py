from src.db.DBController import *
from src.db.util.QueryStringFile import *


def create_table_product():
    get_cursor().execute(querycreatetableproduct)


def get_products():
    return get_list(queryselectproduct)


def start():
    create_table_product()
    print(get_products())
