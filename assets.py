import sqlite3

def query_assets():
    profit_and_loss = 0
    conn = sqlite3.connect('./stocks.db')
    cur = conn.cursor()
    cur.execute("""
        SELECT
            A.ID,
            A.STOCK_ID,
            A.STOCK_NAME,
            A.STOCK_HOLDINGS,
            A.AVERAGE_PRICE,
            A.COST_OF_INVESTMENT,
            DP.CURRENT_PRICE,
            (DP.CURRENT_PRICE * A.STOCK_HOLDINGS) - ((DP.CURRENT_PRICE * A.STOCK_HOLDINGS) * 0.001425) - ((DP.CURRENT_PRICE * A.STOCK_HOLDINGS) * 0.003) AS BOOK_VALUE,
            (A.STOCK_HOLDINGS * DP.CURRENT_PRICE) - A.COST_OF_INVESTMENT - ((DP.CURRENT_PRICE * A.STOCK_HOLDINGS) * 0.001425) - ((DP.CURRENT_PRICE * A.STOCK_HOLDINGS) * 0.003) AS PROFIT_AND_LOSS,
            (((A.STOCK_HOLDINGS * DP.CURRENT_PRICE) - A.COST_OF_INVESTMENT - ((DP.CURRENT_PRICE * A.STOCK_HOLDINGS) * 0.001425) - ((DP.CURRENT_PRICE * A.STOCK_HOLDINGS) * 0.003)) / A.COST_OF_INVESTMENT) * 100 AS PROFIT_AND_LOSS_PERCENTAGE
        FROM ASSETS A
        JOIN DAILY_PRICE DP ON A.ID = DP.ID;
    """)
    rows = cur.fetchall()
    print('{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}'.format("代號","持股","成交均價","投資成本","市價","帳面市值","損益","損益率%"))
    for row in rows:
        print(
            '{id:<10}\t{holdings:<10}\t{avg_price:<10}\t{cost:<10}\t{curr:<10}\t{book:<10.2f}\t{profit:<10.2f}\t{profit_p:<10.2f}'
            .format(
                id=row[1],
                holdings=row[3],
                avg_price=row[4],
                cost=row[5],
                curr=row[6],
                book=float(row[7]),
                profit=float(row[8]),
                profit_p=float(row[9])
            )
        )
        profit_and_loss += row[8]
    print('總損益: {}'.format(profit_and_loss))
    conn.close()