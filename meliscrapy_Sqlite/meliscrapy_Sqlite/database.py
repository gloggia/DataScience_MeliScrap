import sqlite3

conn = sqlite3.connect('mymeli.db')
curr = conn.cursor()

curr.execute('''create table meli_tb(
                 título text,
                 precio text,
                 rooms  text,
                 baths  text
                 )''')
conn.commit()
conn.close()
