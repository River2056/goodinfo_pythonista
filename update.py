from datetime import datetime
import utils
import yaml
import sqlite3
import fetch
import time


def read_stocks_from_yaml(yaml_path):
    with open(yaml_path) as file:
        contents = file.read()
        stocksContent = yaml.safe_load(contents)
        return stocksContent['stocks']


def update_current_price(stocks):
    current = datetime.now()
    datetime_str = utils.format_date_into_string(current)
    conn = sqlite3.connect('./stocks.db')
    cur = conn.cursor()
    for stock in stocks:
        price, percentage = fetch.fetch_stock_price_and_percentage(stock)
        print('stock: {}, price: {}, percentage: {}, modify_date: {}'.format(stock, price, percentage, datetime_str))
        time.sleep(2)

        cur.execute(
            'UPDATE DAILY_PRICE SET CURRENT_PRICE = ?, PERCENTAGE = ?, MODIFY_DATE = ? WHERE STOCK_ID = ?',
            (price, percentage, datetime_str, stock)
        )
        conn.commit()
    conn.close()
    print('done updating database')