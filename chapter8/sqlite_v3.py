import sqlite3

con = sqlite3.connect('./test.db')

cur = con.cursor()
try:
    cur.execute('update person set name=? where id=?',('rose',3))
    # cur.execute('delete from person where id=?' ,(0,))
    con.commit()
    print('commit successfully')
except Exception as e:
    print('operation failed.')
    con.rollback()
finally:
    print('disconnected.')
    cur.close()
    con.close()
