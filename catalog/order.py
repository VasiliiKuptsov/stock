
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

    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("обработка дебетного")
            print(f"проверка кода: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("обработка кредитного")
            print(f"проверка кода: {security_code}")
            self.status = "paid"


order = Order()
order.add_item("клава", 1, 2500)
order.add_item("ssd", 1, 7500)
order.add_item("usb", 2, 250)

print(order.total_price())
order.pay("debit", "0372846")
order.pay("credit", "8765448")