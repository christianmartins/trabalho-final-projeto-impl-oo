from src.util import InputUtil
from src.util.StringFileUtil import method_not_implemented, finish_application


class BaseMenu:

    def init(self):
        self.onInit()

    def onInit(self):
        raise NotImplementedError(method_not_implemented)

    @staticmethod
    def get_int_input(msg):
        return InputUtil.get_int_input(msg)

    @staticmethod
    def get_string_input(msg):
        return InputUtil.get_input(msg)

    @staticmethod
    def get_double_input(msg):
        return InputUtil.get_double_input(msg)
