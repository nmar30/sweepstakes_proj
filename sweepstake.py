import random
from contestant import Contestant


class Sweepstake:
    def __init__(self, name):
        self.contestants = {}
        self.name = name

    def register_contestant(self, contestant):
        self.contestants[len(self.contestants)] = contestant

    def pick_winner(self):
        winner = random.randint(0, len(self.contestants))
        return self.contestants.get(winner)

    def print_contestant_info(self, contestant):
        print('Winner is:')
        print(f'{contestant.first_name} {contestant.last_name} | {contestant.email_address} | {contestant.registration_number}')