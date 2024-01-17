from abc import ABC, abstractmethod

class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices=[]
        self.status = 'open'

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        return sum(quantities * prices for quantities, prices in zip(self.quantities, self.prices))



class Payment(ABC):


    @abstractmethod
    def pay(self, order, security_code):
        pass

class DebitPayment(Payment):


    def pay(self, order, security_code):
        print("обработка дебетного")
        print(f"проверка кода: {security_code}")
        order.status = "paid"

class CreditPayment(Payment):

    def pay(self, order, security_code):
        print("обработка кредитного")
        print(f"проверка кода: {security_code}")
        order.status = "paid"


order = Order()
order.add_item("клава", 1, 2500)
order.add_item("ssd", 1, 7500)
order.add_item("usb", 2, 250)

print(order.total_price())
debit_payment = DebitPayment()
debit_payment.pay(order, "0372846")
credit_payment = CreditPayment()
credit_payment.pay(order, "8765448")