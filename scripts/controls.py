import time
import datetime
import uuid

from resources import Actions, Categories, NonExistentError


class Controls:
    DEFAULT_PROMPT = 'What would you like to do? '

    def __init__(self, display, screen, transactions):
        self._display = display
        self._screen = screen
        self._transactions = transactions
        self._user = 'kameron'

    @staticmethod
    def _prompt_user_input(prompt=DEFAULT_PROMPT):
        return input(prompt).lower().strip()

    def _process_user_input(self, user_input):
        input_array = user_input.split()
        # No command was given, so actions are required
        if len(input_array) == 0:
            return
        try:
            self._parse_action(input_array)
        except Exception as e:
            self._display.new_message(f'*** Sorry, could not process command ***')
            self._display.add_to_message(f'Error: {e}')

    def _parse_action(self, input_array):
        if input_array[0] == Actions.HELP.type:
            self._display.show_help()
        elif input_array[0] == Actions.EXIT.type:
            self.close_program()
        elif input_array[0] == Actions.VIEW.type:
            if len(input_array) > 1:
                self.handle_view(input_array[1])
            else:
                self._display.new_message(f'please provide a page you wish to view')
        elif input_array[0] == Actions.ADD.type:
            if len(input_array) > 1:
                self.handle_add(input_array[1])
            else:
                self._display.new_message(f'please provide an element you would like to add')
        elif input_array[0] == Actions.EDIT.type:
            if len(input_array) > 1:
                self.handle_edit(input_array[1])
            else:
                self._display.new_message(f'please provide an element you would like to edit')
        elif input_array[0] == Actions.DELETE.type:
            if len(input_array) > 1:
                self.handle_delete(input_array[1])
            else:
                self._display.new_message(f'please provide an element you would like to delete')
        else:
            self._display.new_message(f'\'{input_array[0]}\' is not a valid command')

    def close_program(self):
        print('Alfred is powering down now...')
        self._transactions.save()
        exit()

    def handle_view(self, page):
        if page == 'help':
            self._display.new_message(f'View: {Actions.VIEW.description}')
        elif page == 'overview':
            self._screen.change_active_page(self._screen.overview)
        elif page == 'transactions':
            self._screen.change_active_page(self._screen.transactions)
        else:
            self._display.new_message(f'{page} is not a valid page')

    def handle_add(self, element):
        if element == 'help':
            self._display.new_message(f'Add: {Actions.ADD.description}')
        elif element == 'transaction':
            self.add_transactions()
        else:
            self._display.new_message(f'{element} is not a valid element')

    def handle_edit(self, element):
        if element == 'help':
            self._display.new_message(f'Edit: {Actions.EDIT.description}')
        elif element == 'transaction':
            self.edit_transaction()
        else:
            self._display.new_message(f'{element} is not a valid element')

    def handle_delete(self, element):
        if element == 'help':
            self._display.new_message(f'Delete: {Actions.DELETE.description}')
        elif element == 'transaction':
            self.delete_transaction()
        else:
            self._display.new_message(f'{element} is not a valid element')

    def add_transactions(self):
        other_options = '(\'cancel\': cancel new transaction, \'\': set to default value)'
        date = None
        amount = None
        description = None
        category = None
        self._display.new_message(f'Enter a date in the format YYYY-MM-DD {other_options}')
        while not date:
            self._display.print_screen()
            user_input = self._prompt_user_input(prompt='Date: ')
            if user_input == 'cancel':
                self._display.clear_message()
                return
            elif user_input == '':
                break
            else:
                try:
                    parsed_input = user_input.split('-')
                    date = datetime.date(int(parsed_input[0]), int(parsed_input[1]), int(parsed_input[2]))
                except:
                    pass
        self._display.new_message(f'Enter an amount {other_options}')
        while not amount:
            self._display.print_screen()
            user_input = self._prompt_user_input(prompt='Amount: ')
            if user_input == 'cancel':
                self._display.clear_message()
                return
            elif user_input == '':
                break
            else:
                try:
                    amount = float(user_input)
                except:
                    pass
        self._display.new_message(f'Enter a description {other_options}')
        while not description:
            self._display.print_screen()
            user_input = self._prompt_user_input(prompt='Description: ')
            if user_input == 'cancel':
                self._display.clear_message()
                return
            elif user_input == '':
                break
            else:
                description = user_input
        self._display.new_message(f'Enter a category {other_options}')
        while not category:
            self._display.print_screen()
            user_input = self._prompt_user_input(prompt='Category: ')
            if user_input == 'cancel':
                self._display.clear_message()
                return
            elif user_input == '':
                break
            else:
                try:
                    category = Categories(user_input)
                except:
                    pass
        try:
            self._transactions.new(date, amount, description, category)
            self._display.new_message('Added new transaction!')
        except:
            self._display.new_message('Could not create new transaction.')

    def edit_transaction(self):
        pass

    def delete_transaction(self):
        other_options = '(\'cancel\': cancel delete)'
        deleted = False
        self._display.new_message(f'Please provide the ID of the transaction you wish to delete {other_options}')
        while not deleted:
            self._display.print_screen()
            user_input = self._prompt_user_input(prompt='ID: ')
            if user_input == 'cancel':
                return
            else:
                try:
                    self._transactions.delete(uuid.UUID(user_input))
                    self._display.clear_message()
                    deleted = True
                except NonExistentError:
                    self._display.new_message(f'{user_input} does not exist {other_options}')
                except ValueError:
                    self._display.new_message(f'{user_input} is not a valid ID {other_options}')

    def step(self):
        user_input = self._prompt_user_input()
        self._process_user_input(user_input)
