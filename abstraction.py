from abc import ABC, abstractmethod

class Payment(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def pay(self, amount):
        pass

    def printOperation(self):
        print("non abstract function invoked", self.name)

class CreditCard(Payment):

    def pay(self, amount):
        print("Payment using CreditCard: ", amount)

class UPI(Payment):
    def pay(self, amount):
        print("Payment using UPI: ", amount)

credit_card = CreditCard("Vignesh")
credit_card.pay(1000)
credit_card.printOperation()

upi = UPI("Vignesh")
upi.pay(20000)