import time
import datetime

from scripts import controls, display, screen, transactions

# Global Variables
current_date = None


def run():
    # Print the screen
    display.step()
    # Prompt user for command and determine next action
    controls.step()
    time.sleep(0.1)


if __name__ == '__main__':
    current_date = datetime.date.today()
    transactions = transactions.Transactions()
    screen = screen.Screen(transactions)
    display = display.Display(screen)
    controls = controls.Controls(display, screen, transactions)
    while True:
        run()
