from src.db.dao import ProductDAO


def createEntity():
    ProductDAO.start()


def start():
    createEntity()


def main():
    start()


if __name__ == '__main__':
    main()
