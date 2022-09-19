import random

class CoinFlipper:
    num_of_coins = 0
    def __init__(self, num_of_coins, recordList):
        self.num_of_coins = num_of_coins
        self.recordList = recordList
    def flip(self):
        
        self.recordList = []

        for n in range(self.num_of_coins):
            flip = random.randint(0,1)
            if(flip == 0):
                self.recordList.append("H")
            else:
                self.recordList.append("T")
            
        return self.recordList
