import sqlite3

con = sqlite3.connect('./test.db')

cur = con.cursor()

cur.execute('select * from person ')
res = cur.fetchall()
print(res)
cur.close()
con.close()
