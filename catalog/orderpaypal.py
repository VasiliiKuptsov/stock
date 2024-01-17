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

    def __init__(self, security_code):
        self.security_code = security_code
        self.is_verified = False
    def pay(self, order):
        if not self.is_verified:
            raise Exception('необходимо авторизоваться по SMS')
        print("обработка дебетного")
        print(f"проверка кода: {self.security_code}")
        order.status = "paid"

class CreditPayment(Payment):

    def __init__(self, security_code):
        self.security_code = security_code
        self.is_verified = False
    def pay(self, order):
        print("обработка кредитного")
        print(f"проверка кода: {self.security_code}")
        order.status = "paid"

class PaypalPayment(Payment):

    def __init__(self, email_adress):
        self.email_adress = email_adress

    def pay(self, order):
        if not self.is_verified:
            raise Exception('необходимо авторизоваться по SMS')
        print("обработка Paypal")
        print(f"проверка почты: {self.email_adress}")
        order.status = "paid"


order = Order()
order.add_item("клава", 1, 2500)
order.add_item("ssd", 1, 7500)
order.add_item("usb", 2, 250)

print(order.total_price())
debit_payment = DebitPayment("0372846")
debit_payment.pay(order)
credit_payment = CreditPayment("8765448")
credit_payment.pay(order)

credit_payment = PaypalPayment("same@mail.com")
credit_payment.pay(order)
