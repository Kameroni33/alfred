import datetime


class Page:
    """
    Base class for pages. All pages inherit from this class.
    """

    def build_screen(self):
        raise Exception(f'build_screen function must be implemented for child class {self}')


class OverviewPage(Page):
    def __init__(self, transactions):
        self._transactions = transactions

    def build_screen(self):
        screen = f'Today\'s date is: {datetime.datetime.now()}\n'
        screen += 'Thank you for supporting the work of Alfred :)\n'
        return screen


class TransactionsPage(Page):
    num_of_displayed_transactions = 10

    def __init__(self, transactions):
        self._transactions = transactions

    def build_screen(self):
        screen = f'Last ({self.num_of_displayed_transactions}) transactions:\n'
        curr_transaction = 1
        for transaction in self._transactions.get_list():
            screen += f'{transaction}\n'
            curr_transaction += 1
            if curr_transaction > self.num_of_displayed_transactions:
                break
        return screen
