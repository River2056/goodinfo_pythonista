from modules import assets
from modules import query
from modules import update
from database import dbutils
from classes.mode import Mode
from classes.menus import Menus
from classes.menu_mode import MenuMode


if __name__ == '__main__':
    options = [
        MenuMode(1, 'update all current price'),
        MenuMode(2, 'fetch stock prices'),
        MenuMode(3, 'query assets'),
        MenuMode(4, 'select data from table'),
        MenuMode(999, 'quit')
    ]
    menus = Menus(*options)

    while True :
        menus.print_msg_to_console()
        choice = Mode(int(input('please choose module: ')))
        if choice == Mode.UPDATE_ALL_CURRENT_PRICE:
            print(f'print choice in function: {choice}')
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
        elif choice == Mode.QUERY_ASSETS:
            print('querying results...')
            assets.query_assets()
            input('press any key to continue...\n')
        elif choice == Mode.SELECT_DATA_FROM_TABLE:
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
        elif choice == Mode.QUIT:
            print('exiting program...\n')
            quit() 
