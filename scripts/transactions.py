import datetime
import uuid
import pickle

from resources import NonExistentError, Categories


class Transactions:
    """
    CLass that contains all saved transactions. Offers methods to create, edit, or delete transactions. All are saved
    locally in .csv file
    """
    num_of_transactions = 0
    data_path = './data/transaction_data.p'

    def __init__(self):
        self._transactions_list = []

        try:
            self.load()
            self.num_of_transactions = len(self._transactions_list)
        except IOError:
            raise IOError('could not load transaction data...')

    def new(self, date: datetime, amount: float, description: str, category: Categories):
        new_transaction = Transaction(date, amount, description, category)
        self._transactions_list.append(new_transaction)
        self.num_of_transactions += 1

    def edit(self, id, date: datetime, amount: float, description: str, category: Categories):
        transaction = self.find(id)
        if transaction:
            transaction.update(date, amount, description, category)
        else:
            raise NonExistentError(f'Could not find transaction with ID {id}')

    def delete(self, id):
        transaction = self.find(id)
        if transaction:
            print(transaction)
            self._transactions_list.remove(transaction)
        else:
            raise NonExistentError(f'Could not find transaction with ID {id}')

    def find(self, id):
        for transaction in self.get_list():
            if transaction.id == id:
                return transaction

    def save(self):
        with open(self.data_path, 'wb+') as file:
            pickle.dump(self._transactions_list, file)

    def load(self):
        with open(self.data_path, 'rb+') as file:
            self._transactions_list = pickle.load(file)

    def sort(self):
        self._transactions_list.sort()

    def get_list(self):
        return self._transactions_list


class Transaction:
    """
    Represents a transaction of money.
    """
    DEFAULT_AMOUNT = 0.0
    DEFAULT_DESCRIPTION = ''
    DEFAULT_CATEGORY = Categories.NONE

    def __init__(self, date, amount, description, category):
        self.id = uuid.uuid4()
        if date is not None:
            self.date = date
        else:
            self.date = datetime.date.today()
        if amount is not None:
            self.amount = amount
        else:
            self.amount = self.DEFAULT_AMOUNT
        if description is not None:
            self.description = description
        else:
            self.description = self.DEFAULT_DESCRIPTION
        if category is not None:
            self.category = category
        else:
            self.category = self.DEFAULT_CATEGORY

    def __str__(self):
        if self.amount >= 0:
            return f'| {self.id} | {self.date} | +${self.amount} | {self.description} | {self.category}'
        else:
            return f'| {self.id} | {self.date} | -${self.amount[1:-1]} | {self.description} | {self.category}'

    def __len__(self):
        return len(str(self))

    def __eq__(self, other):
        return self.id == other.id

    def update(self, date, amount, description, category):
        if date is not None:
            self.date = date
        if amount is not None:
            self.amount = amount
        if description is not None:
            self.description = description
        if category is not None:
            self.category = category



