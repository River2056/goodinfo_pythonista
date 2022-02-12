class Stock():
    def __init__(self, id_no, price, amount):
        self.id_no = id_no
        self.price = price
        self.amount = amount
    
    def __str__(self):
        return f'Stock[{self.id_no}]: price: {self.price} ; amount: {self.amount}'

    def cal(self):
        return self.price * self.amount
