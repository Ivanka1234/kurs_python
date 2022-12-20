import sqlite3

db=sqlite3.connect('test_sqlite')
cursor=db.cursor()

cursor.execute("SELECT * FROM user")
res= cursor.fetchone()


for lok in res:
    print(lok)


db.close()