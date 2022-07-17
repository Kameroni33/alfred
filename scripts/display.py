import os
import datetime

from resources import constants, Actions


class Display:

    def __init__(self, screen):
        self._date = datetime.date.today()
        self._screen = screen
        self._header = f' ALFRED {constants.VERSION}  - by Kameron Ronald '
        self._message = ''

    def print_screen(self):
        os.system('cls')
        print(self.make_line('=', constants.SCREEN_WIDTH, new_line=False))
        print(self._header + f'\t\t\t\t\t {self._date.strftime("%B %d, %Y")}')
        print(self.make_line('=', constants.SCREEN_WIDTH))
        print(self._screen.build_active_page())
        print(self.make_line('=', constants.SCREEN_WIDTH))
        print(self._message + '\n')
        print(self.make_line('=', constants.SCREEN_WIDTH))

    def make_line(self, char: str, length: int, new_line=True):
        line = ''
        for _ in range(length):
            line += char
        if new_line:
            return line + '\n'
        else:
            return line

    def show_help(self):
        new_message = ' Here is a list of possible commands:\n\n'
        for action in Actions:
            new_message += '  - ' + action.type + '\n'
        self.new_message(new_message)

    def new_header(self, header_info):
        self._header = header_info

    def new_message(self, message_info):
        self._message = message_info

    def add_to_header(self, header_info):
        self._header += header_info

    def add_to_message(self, message_info):
        self._message += message_info

    def clear_header(self):
        self._header = ''

    def clear_message(self):
        self._message = ''

    def step(self):
        self.print_screen()
