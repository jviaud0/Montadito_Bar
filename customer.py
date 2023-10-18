import random as rd

class Customer:
    def __init__(self, id, age):
        self.id = id
        self.age = age
        print(f"Customer {self.id} was created. He is {self.age} years old. ")

    def order(self):
        n_beers = rd.randint(1, 5)
        print(f"Customer {self.id} wants {n_beers} beers. ")

for i in range(5):
    customer = Customer(i + 1, rd.randint(18, 50))
    customer.order()