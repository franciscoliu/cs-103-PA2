import sqlite3


def to_cat_dict(cat_tuple):
    ''' cat is a category tuple (rowid, name, desc)'''
    cat = {'rowid': cat_tuple[0], 'item_number': cat_tuple[1], 'amount': cat_tuple[2], 'category': cat_tuple[3],
           'date': cat_tuple[4], 'description': cat_tuple[5]}
    return cat


def to_cat_dict_list(cat_tuples):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_cat_dict(cat) for cat in cat_tuples]


class Transaction():
    def __init__(self, dbfile):
        con = sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions 
                    (item_number int, amount int, category text, date int, description text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)

    def add(self, item):
        ''' add a transaction to the transaction table.
            this returns the rowid of the inserted element
        '''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)",
                    (item['item_number'], item['amount'], item['category'], item['date'], item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def delete(self, rowid):
        ''' delete a transaction to the transaction table.
            this returns the rowid of the deleted element
        '''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE rowid=(?);
        ''', (rowid,))
        con.commit()
        con.close()
