import sqlite3

def query_table(cur, table_name):
    sql = 'SELECT * FROM {table}'.format(table=table_name)
    cur.execute(sql)
    cols = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    for col in cols:
        print('{:<3}'.format(col), end='\t')
    print()
    for i in range(len(rows)):
        for v in rows[i]:
            print('{:<7}'.format(v), end='\t')
        print()

def show_all_tables(cur):
    cur.execute('''
        SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%'
    ''')
    all_tables = cur.fetchall()
    result = []
    for idx, table in enumerate(all_tables):
        result_obj = {}
        result_obj[idx+1] = table[0]
        result.append(result_obj)
    return result
