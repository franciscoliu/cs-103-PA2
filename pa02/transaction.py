import sqlite3


def to_cat_dict(cat_tuple):
    ''' cat is a category tuple (rowid, name, desc)'''
    cat = {'rowid': cat_tuple[0], 'item_number': cat_tuple[1], 'amount': cat_tuple[2], 'category': cat_tuple[3],
           'date': cat_tuple[4], 'description': cat_tuple[5]}
    print("Test second")
    return cat


def to_cat_dict_list(cat_tuples):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_cat_dict(cat) for cat in cat_tuples]


def summarize_by_date_helper(cat_tuple):
    cat = {'date': cat_tuple[0], 'total_amount_transaction': cat_tuple[1]}
    return cat


def summarize_by_category_helper(cat_tuple):
    cat = {'category': cat_tuple[0], 'total_amount_transaction': cat_tuple[1]}
    return cat


class Transaction:
    def __init__(self, dbfile):
        con = sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions 
                    (item_number text, amount int, category text, date int, description text)''')
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

    def select_one(self, rowid):
        ''' return all of the transactions as a list of dicts.'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions where rowid = (?)", (rowid,))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict(tuples[0])

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

    def summarize_by_date(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT date, SUM(amount) FROM transactions GROUP BY date''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [summarize_by_date_helper(tuple) for tuple in tuples]

    def summarize_by_month(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT date/100%100, SUM(amount) FROM transactions GROUP BY date/100%100''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [summarize_by_date_helper(tuple) for tuple in tuples]

    def summarize_by_year(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT date/10000, SUM(amount) FROM transactions GROUP BY date/10000''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [summarize_by_date_helper(tuple) for tuple in tuples]

    def summarize_by_category(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT category, SUM(amount) FROM transactions GROUP BY category''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [summarize_by_category_helper(tuple) for tuple in tuples]

    def summarize_by_month(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT date, SUM(amount) FROM transactions GROUP BY date//100%100 ''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [summarize_by_category_helper(tuple) for tuple in tuples]

    def clear_database(self):
        '''
        clear the entire Transaction database
        '''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('DELETE FROM transactions;', )
        con.commit()
        con.close()
