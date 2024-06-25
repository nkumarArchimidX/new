import sqlite3

conn = sqlite3.connect('feedback.db')
c = conn.cursor()
c.execute("select * from feedback")
data = c.fetchall()
print(data)
conn.commit()
conn.close()
