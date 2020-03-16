from src.util.StringFile import *


def init():
    looper()


def looper():
    show_options()
    get_input()


def show_options():
    print(menu_options)


def get_input():
    return input(menu_input)
