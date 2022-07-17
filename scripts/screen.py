from scripts import Page, OverviewPage, TransactionsPage


class Screen:
    """
    Base class to hold all the various pages.
    """
    def __init__(self, transactions):
        self.overview = OverviewPage(transactions)
        self.transactions = TransactionsPage(transactions)

        self.active_page = self.overview

    def build_active_page(self):
        return self.active_page.build_screen()

    def change_active_page(self, page: Page):
        self.active_page = page

