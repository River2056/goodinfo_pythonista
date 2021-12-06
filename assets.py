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
            DP.CURRENT_PRICE * A.STOCK_HOLDINGS AS BOOK_VALUE,
            (A.STOCK_HOLDINGS * DP.CURRENT_PRICE) - A.COST_OF_INVESTMENT AS PROFIT_AND_LOSS,
            (((A.STOCK_HOLDINGS * DP.CURRENT_PRICE) - A.COST_OF_INVESTMENT) / A.COST_OF_INVESTMENT) * 100 AS PROFIT_AND_LOSS_PERCENTAGE
        FROM ASSETS A
        JOIN DAILY_PRICE DP ON A.ID = DP.ID;
    """)
    rows = cur.fetchall()
    print('代號\t持股\t成交均價\t投資成本\t市價\t帳面市值\t損益\t損益率%')
    for row in rows:
        print(
            '{id}\t{holdings}\t{avg_price}\t{cost}\t{curr}\t{book}\t{profit}\t{profit_p}'
            .format(
                id=row[1],
                holdings=row[3],
                avg_price=row[4],
                cost=row[5],
                curr=row[6],
                book=row[7],
                profit=row[8],
                profit_p=row[9]
            )
        )
        profit_and_loss += row[8]
    print('總損益: {}'.format(profit_and_loss))
    conn.close()