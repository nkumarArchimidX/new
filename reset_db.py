import sqlite3

def reset_db():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    # Drop the table if it exists
    c.execute('DROP TABLE IF EXISTS feedback')
    # Create the table with the correct schema
    c.execute('''
        CREATE TABLE feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            input_text TEXT NOT NULL,
            feedback REAL NOT NULL,
            comment TEXT,
            model TEXT NOT NULL,
            class_choice TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("Table created successfully.")

reset_db()
