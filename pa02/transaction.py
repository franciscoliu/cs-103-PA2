import sqlite3

class Transaction():
    def __init__(self,dbfile):
        con = sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions 
                    (item, integer, amount, integer, category, text, date, text, description, text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile