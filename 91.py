import sqlite3
import pandas as pd

data = pd.read_csv('ten_countries.txt')

conn = sqlite3.connect("database.db")
cur = conn.cursor()
for index,row in data.iterrows():
    print(row["Country"], row["Area"])
    cur.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)",(row["Country"], row["Area"]))

conn.commit()
conn.close()