from modules import assets
from modules import query
from modules import update
from database import dbutils


def module_selection():
    module_map = {
        '1': 'update all current price',
        '2': 'fetch stock prices',
        '3': 'query assets',
        '4': 'select data from table',
        'q': 'press q to exit...'
    }
    for k, v in module_map.items():
        print('{key}. {value}'.format(key=k, value=v))
    choice = input('choose a module: ')
    return module_map[choice]


if __name__ == '__main__':
    while True :
        choice = module_selection()
        if choice == 'update all current price':
            stock_list = update.read_stocks_from_yaml('./stocks.yaml')
            print('stocks listed for update are: ')
            [print(stock, end=', ') for stock in stock_list]
            ans = input('\nconfirm update? [y/n] ')
            if ans == 'y':
                print('running update...')
                update.update_current_price(stocks=stock_list)
                input('press any key to continue...\n')
            else:
                print('terminating...\n')
        elif choice == 'query assets':
            print('querying results...')
            assets.query_assets()
            input('press any key to continue...\n')
        elif choice == 'select data from table':
            conn = dbutils.get_connection()
            cur = conn.cursor()
            print('tables available: ')
            all_tables = query.show_all_tables(cur)
            for idx, table in enumerate(all_tables):
                print('{}. {}'.format(idx+1, table[idx+1]))
            table_choice = int(input('choose a table: '))
            query.query_table(cur, all_tables[table_choice-1][table_choice])
            dbutils.close_connection(conn)
            input('press any key to continue...\n')
        elif choice == 'press q to exit...':
            print('exiting program...\n')
            quit() 
