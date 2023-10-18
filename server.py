import random as rd

class Server:
    def __init__(self,hands, name):
        self.name = name
        self.hands = hands
    def introduce(self):
        print(f"Hello, my name is {self.name} and I have {self.hands} hands."
              f"\nI will be your server for today")

Chad = Server(hands = rd.randint(1,3), name = "Chad", )
Chad.introduce()






