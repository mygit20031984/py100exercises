import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()
cur.execute("select country,area,population from countries where area >= 200000")
rows = cur.fetchall()
conn.close()

for i in rows:
    print(i[0],i[1],i[2])