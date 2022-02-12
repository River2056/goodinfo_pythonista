def find_max_amount_of_buy(budget, *args):
    # find average amount of stock count according to budget
    average_amount = budget / len(args)
    print(f'average amount: {average_amount}')
    total = 0
    for stock_price in args:
        max_amount = average_amount / stock_price
        sub_total = stock_price * int(max_amount)
        total += sub_total
        print(f'price: {stock_price}, max amount: {max_amount}, sub total: {sub_total}')
    print(f'total: {total}')
