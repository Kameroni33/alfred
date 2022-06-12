import os
import time

from enums import Options


class Display:

    def __init__(self):
        self.version = '0.1.0'
        self.header = f' ALFRED {self.version}  - by Kameron Ronald '
        self.body = f' An all inclusive, interactive, digital butler :) \n'
        self.message = ''

    def print_screen(self):
        os.system('cls')
        print('=====================================================================================================')
        print(self.header)
        print('=====================================================================================================\n')
        print(self.body)
        print('-----------------------------------------------------------------------------------------------------\n')
        print(self.message)
        print('-----------------------------------------------------------------------------------------------------\n')

    def show_help(self):
        new_message = ' Here is a list of all possible commands:\n\n'
        for opt in Options:
            new_message += '  - ' + opt.value + '\n'
        self.new_message(new_message)

    def new_body(self, body_info):
        self.body = body_info

    def new_header(self, header_info):
        self.header = header_info

    def new_message(self, message_info):
        self.message = message_info

    def add_to_body(self, body_info):
        self.body += body_info

    def add_to_header(self, header_info):
        self.header += header_info

    def add_to_message(self, message_info):
        self.message += message_info

    def clear_header(self):
        self.header = ''

    def clear_body(self):
        self.body = ''

    def clear_message(self):
        self.message = ''
