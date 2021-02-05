import sqlite3

conn = sqlite3.connect('count.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')

cur.execute('DELETE FROM Ages')
cur.execute("INSERT INTO Ages (name, age) VALUES ('Kaysie', 14)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Clyde', 40)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Serene', 31)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Capree', 23)")
sqlstr = "SELECT hex(name || age) AS X FROM Ages ORDER BY X"
conn.commit()
#sqlstr = "SELECT name, age FROM Ages LIMIT 5"
for row in cur.execute(sqlstr):
    print(row[0])

cur.close()
