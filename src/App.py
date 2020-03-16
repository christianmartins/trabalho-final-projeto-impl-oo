from src.db.dao import ProductDAO
from src.view import Menu


def createEntity():
    ProductDAO.start()


def start():
    createEntity()
    Menu.init()


def main():
    start()


if __name__ == '__main__':
    main()
