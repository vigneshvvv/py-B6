class CreditCardPayment:
    def pay(self, amount):
        print(f"paid ${amount} using credit card")

class UPIPayment:
    def pay(self, amount):
        print(f"paid ${amount} using UPI")

class PayPalPayment:
    def pay(self, amount):
            print(f"paid ${amount} using PayPal")

def processPayment(payment_method, amount):
     payment_method.pay(amount)

credit = CreditCardPayment()
upi = UPIPayment()
pay = PayPalPayment()

processPayment(credit, 10000)
processPayment(upi, 20000)
processPayment(pay, 5000)