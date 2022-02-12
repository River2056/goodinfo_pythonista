def find_max_amount_of_buy(budget, *args):
    arr = []
    for pair in args:
        p = budget / pair
        print(f'price:{pair} => max: {p}')
        arr.append(p)
    print(arr)
    combos = {}
    t = list(zip(args, arr))
    print(t)
