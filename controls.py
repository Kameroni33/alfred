
from enums import Options


class Controls:
    user_prompt = 'What would you like to do? '

    def __init__(self, display):
        self.display = display
        self.user = 'kameron'

    def prompt_user_input(self):
        user_input = input(self.user_prompt).lower()
        self.user_input_handler(user_input)

    def user_input_handler(self, user_input):
        if user_input == Options.EXIT.value:
            self.close_program()
        elif user_input == Options.HELP.value:
            self.display.show_help()
            return Options.HELP
        else:
            self.display.new_message(' *** Sorry, invalid command. To list all commands type \'help\' ***\n')
            return Options.NONE

    @staticmethod
    def close_program():
        print('Alfred is powering down now...')
        exit()
