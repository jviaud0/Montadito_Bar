class Bar:
    def __init__(self, name):
        self.name = name
    def welcome(self):
        print(f"Welcome to {self.name}")



shout = Bar(name = 'Shout')
shout.welcome()


