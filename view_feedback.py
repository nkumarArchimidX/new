import sqlite3
import streamlit as st

# Function to get database connection
def get_db_connection():
    conn = sqlite3.connect('feedback.db')
    conn.row_factory = sqlite3.Row
    return conn

# Function to fetch all feedback
def fetch_all_feedback():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM feedback")
    rows = c.fetchall()
    conn.close()
    return rows

# Streamlit app code
st.title('Feedback Viewer')

feedback = fetch_all_feedback()
if feedback:
    for row in feedback:
        st.write(f"ID: {row['id']}, Name: {row['name']}, Input Text: {row['input_text']}, Feedback: {row['feedback']}, Comment: {row['comment']}, Model: {row['model']}, Class Choice: {row['class_choice']}, Timestamp: {row['timestamp']}")
else:
    st.write("No feedback found.")
