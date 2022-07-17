import enum
from collections import namedtuple


class Categories(enum.Enum):
    FOOD = 'food'
    GROCERIES = 'groceries'
    BILLS = 'bills'
    MONTHLY_PAYMENTS = 'monthly payments'
    ENTERTAINMENT = 'entertainment'
    GIFTS = 'gifts'
    CHARITY = 'charity'
    MISC = 'misc'
    OTHER = 'other'

    NONE = 'none'


class Actions(namedtuple('Actions', 'type description'), enum.Enum):
    ADD = (
        'add',
        'create a new transaction, account, ...',
    )
    EDIT = (
        'edit',
        'edit details on an existing transaction, account, ...',
    )
    DELETE = (
        'delete',
        'delete a transaction, account, ...'
    )
    VIEW = (
        'view',
        'change the screen to a different page'
    )
    HELP = (
        'help',
        'list all possible commands',
    )
    EXIT = (
        'exit',
        'save and exit the program',
    )
