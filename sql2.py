import sqlite3

conn = sqlite3.connect('count.sqlite')
cur = conn.cursor()

cur.execute("INSERT INTO Ages (name, age) VALUES ('Kaysie', 14)")
sqlstr = "SELECT name, age FROM Ages LIMIT 5"
for row in cur.execute(sqlstr):
    print(row[0], row[1])

cur.close()
