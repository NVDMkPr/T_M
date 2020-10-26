print("Importing Database")
import sqlite3

__all__ = ["SearchUserID","InsertData"]

Connect = sqlite3.connect("all.db",check_same_thread=False)
Cursor = Connect.cursor()

def SearchUserID(id,table_name):
    Cursor.execute(
        f'''
        SELECT *
        FROM {table_name}
        WHERE user_id = {id}
        ''')
    Connect.commit()
    result = Cursor.fetchall()
    if len(result) == 0:
        return None
    return result
def InsertData(table_name,coll_name,value):
    Cursor.execute(
        f'''
        INSERT INTO {table_name} {coll_name}
        VALUES ({value})
        ''')
    Connect.commit()

"""
Cursor.executescript(
    '''
    CREATE TABLE AddrGenByUser(
        user_id int,
        addr_gen_by_user text,
        trx_balance real,
        private_key_of_addr text,
        verified bool
    );
    CREATE TABLE AddrByUser(
        user_id int,
        withdraw_addr text
    )''')
Connect.commit()
Cursor.execute(
    '''
    INSERT INTO test
    VALUES (000000,"TPvC9qQLX4xQ8MUstqfxM3UjJR2GiJXH7E","bf87aabe40d4f53dbfbb4be4ae70c626b0dee2d68c8aa590e9a05cbc9f0572fb")
    ''')
"""
print("Imported Database")