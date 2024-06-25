import sqlite3

# Verify the table creation
conn = sqlite3.connect('feedback.db')
c = conn.cursor()

c.execute("PRAGMA table_info(feedback);")
schema = c.fetchall()

print("Schema of the feedback table:")
for column in schema:
    print(column)

conn.close()
