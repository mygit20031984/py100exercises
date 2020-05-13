import sqlite3
import pandas as pd

conn = sqlite3.connect("database.db")
cur = conn.cursor()
cur.execute("select * from countries where area >= 200000")
rows = cur.fetchall()
conn.close()

df = pd.DataFrame.from_records(rows)
df.columns = ["Rank", "Country", "Area", "Population"]
df.to_csv("Countries_big_area.csv",index=False)