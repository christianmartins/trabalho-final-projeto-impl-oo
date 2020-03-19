from src.util import InputUtil
from src.util.StringFileUtil import method_not_implemented, finish_msg_application, invalid_input


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

    def finish_application(self):
        self.show_message_on_finish_application()
        exit()

    @staticmethod
    def show_message_on_finish_application():
        print(finish_msg_application)

    @staticmethod
    def show_message_invalid_input():
        print(invalid_input)
