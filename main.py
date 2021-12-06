from datetime import datetime
import time
import yaml
import requests
from bs4 import BeautifulSoup
import sqlite3
import constants as c
import assets


def fetch_stock_price_and_percentage(stock_id):
    res = requests.get('{base_url}{stock}'.format(base_url=c.BASE_URL, stock=stock_id), headers=c.HEADER)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.find('table', attrs={'class': 'b1 p4_2 r10'})
    rows = table.find_all('tr')
    cells = rows[3].find_all('td')
    return (cells[0].text, cells[3].text)


def format_date_into_string(date):
    return '{}-{}-{} {}:{}:{}'.format(
        date.year, 
        date.month if date.month >= 10 else '0{}'.format(date.month), 
        date.day if date.day >= 10 else '0{}'.format(date.day),
        date.hour if date.hour >= 10 else '0{}'.format(date.hour), 
        date.minute if date.minute >= 10 else '0{}'.format(date.minute), 
        date.second if date.second >= 10 else '0{}'.format(date.second),
    )


def update_current_price():
    stocks = []
    current = datetime.now()
    datetime_str = format_date_into_string(current)
    with open('./stocks.yaml') as file:
        contents = file.read()
        stocksContent = yaml.safe_load(contents)
        stocks = stocksContent['stocks']
    conn = sqlite3.connect('./stocks.db')
    cur = conn.cursor()
    for stock in stocks:
        price, percentage = fetch_stock_price_and_percentage(stock)
        print('stock: {}, price: {}, percentage: {}, modify_date: {}'.format(stock, price, percentage, datetime_str))
        time.sleep(2)

        cur.execute(
            'UPDATE DAILY_PRICE SET CURRENT_PRICE = ?, PERCENTAGE = ?, MODIFY_DATE = ? WHERE STOCK_ID = ?',
            (price, percentage, datetime_str, stock)
        )
        conn.commit()
    conn.close()
    print('done updating database')

if __name__ == '__main__':
    print('choose mode to execute: ')
    print('1. update_current_price')
    print('2. query_assets')
    choice = int(input())
    if choice == 1:
        print('running update...')
        update_current_price()
    elif choice == 2:
        print('querying results...')
        assets.query_assets()