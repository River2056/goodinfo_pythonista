from enum import Enum


class Mode(Enum):
    UPDATE_ALL_CURRENT_PRICE = 1
    FETCH_STOCK_PRICES = 2
    QUERY_ASSETS = 3
    SELECT_DATA_FROM_TABLE = 4
    QUIT = 999