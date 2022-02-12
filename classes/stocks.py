class Stocks():
    def __init__(self, *args):
        self.stocks = args

    def __str__(self):
        return '\n'.join(map(lambda x: f'{x.__str__()}, subtotal: {x.cal()}', self.stocks))

    def sum_all(self):
        print(self.__str__())
        return sum(map(lambda x: x.cal(), self.stocks))
