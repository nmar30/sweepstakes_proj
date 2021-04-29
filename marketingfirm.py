from sweepstake import Sweepstake
from contestant import Contestant

class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager

    def create_sweepstakes(self):
        name = input('Enter Sweepstake Name: ')
        self.manager.insert_sweepstakes(Sweepstake(name))