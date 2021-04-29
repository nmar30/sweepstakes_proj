from sweepstake import Sweepstake

class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager

    def create_sweepstakes(self):
        name = input('Enter Sweepstake Name: ')
        sweepstake = Sweepstake(name)
        enter_contestants = True
        while enter_contestants:
            print('Please enter contestant info')
            contestant = sweepstake.create_contestant()
            sweepstake.register_contestant(contestant)
            add_another = input('Would you like to add another? ')
            add_another = add_another.lower()
            if add_another == 'no':
                enter_contestants = False
        # Dependency Injection
        self.manager.insert_sweepstakes(sweepstake) 