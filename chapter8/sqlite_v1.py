import sqlite3
# connect the database
con = sqlite3.connect('./test.db')

# create a cursor from con
cur = con.cursor()
try:
    # execute a sql 
    cur.execute('create table person(id integer primary key, name varchar(20), age integer);')

    # execute a sql
    cur.execute('insert into person values(?,?,?)',(0, 'qiye', 20))

    # execute many sql
    cur.executemany('insert into person values (?,?,?)',[(3,'marry',20),(4,'jack',20)])

    # commit a transaction
    con.commit()
    print('commit successfully.')
except Exception as e:
    print('operation failed.')
    con.rollback()
finally:
    print('finally')
    cur.close()
    con.close()



