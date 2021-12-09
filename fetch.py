import requests
from bs4 import BeautifulSoup
import constants as c

def fetch_stock_price_and_percentage(stock_id):
    res = requests.get('{base_url}{stock}'.format(base_url=c.BASE_URL, stock=stock_id), headers=c.HEADER)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.find('table', attrs={'class': 'b1 p4_2 r10'})
    rows = table.find_all('tr')
    cells = rows[3].find_all('td')
    return (cells[0].text, cells[3].text)