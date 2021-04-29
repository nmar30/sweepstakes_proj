from sweepstakesstackmanager import SweepstakesStackManager
from sweepstakesqueuemanager import SweepstakesQueueManager
from marketingfirm import MarketingFirm


class MarketingFirmCreator:
    def __init__(self):
        pass

    def choose_manager_type(self):
        manager_type = input("Please enter Stack or Queue: ")
        manager_type = manager_type.lower()
        while True:
            if manager_type == "stack":
                return MarketingFirm(SweepstakesStackManager())
            elif manager_type == 'queue':
                return MarketingFirm(SweepstakesQueueManager())
            else:
                print('Wrong Input!')