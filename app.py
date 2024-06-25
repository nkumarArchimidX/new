import os
import subprocess

# Ensure NLTK resources are downloaded
subprocess.run(['python', 'nltk_setup.py'], check=True)

import streamlit as st
import sqlite3
import pandas as pd
import rule_based

def get_db_connection():
    conn = sqlite3.connect('feedback.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
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

def insert_feedback(name, input_text, feedback, comment, model, class_choice):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        INSERT INTO feedback (name, input_text, feedback, comment, model, class_choice, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    ''', (name, input_text, feedback, comment, model, class_choice))
    conn.commit()
    conn.close()

create_table()

st.title("Text Classification")

add_selectbox = st.sidebar.selectbox(
    "Which model do you want to use?",
    ("Random Forest", "Naive Bayes", "Logistic Regression", "SVM", "AZURE MODEL")
)

name = st.sidebar.selectbox(
    "Name",
    ("Aadhitya", "Ahmed", "Aijesh Nisha", "Alsamath", "Anouska", "Ashraf Ahmed", "Chandru", "Deva", "Gowtham", "Harini", "Jovita", "Madhumitaa", "Nithik", "Sangavi", "Sathish", "Shalini", "Swetha", "Sylesh", "Vaishnavi", "Varun")
)

st.sidebar.subheader("Feedback Summary")
conn = get_db_connection()
c = conn.cursor()
c.execute("SELECT name, model, COUNT(*) AS row_count FROM feedback WHERE name = ? GROUP BY name, model", (name,))
data = c.fetchall()
columns = ["Name", "Model", "Count"]
st.sidebar.table(pd.DataFrame(data, columns=columns))
conn.close()

with st.form(key="classify_form", clear_on_submit=True):
    input_text = st.text_input("Enter the message to classify", key="user_input")
    button = st.form_submit_button("Classify")
    
if button:
    ans = rule_based.pred(input_text, add_selectbox)
    if len(ans) == 1:
        st.write("The given input was:")
        st.write("Prediction: ", ans[0])
    else:
        st.write("The given input was: ", input_text)
        st.write("Predicted Class: ", ans[0][0])
        st.write("Confidence Score: ", ans[1])

st.subheader("Feedback")
feedback = None  # Initialize feedback

with st.form(key="feedback_form", clear_on_submit=True):
    feedback_type = st.radio(
        "Rate the Performance",
        ('👍', '👎', '❤️')
    )
    if feedback_type == '👍':
        feedback = 0.5
    elif feedback_type == '👎':
        feedback = 0
    else:
        feedback = 1

    if feedback == 0:
        class_choice = st.selectbox(
            "Choose the correct class",
            ("Event", "Exam", "Notes", "Subject", "Schedule", "Question paper", "Calendar", "Score", "Important Question", "Assignments")
        )
    else:
        class_choice = '-'

    comments = st.text_input("Comments", key="comments")
    submit_feedback = st.form_submit_button("Submit Feedback")

if submit_feedback:
    st.write(f"Name: {name}")
    st.write(f"Input Text: {input_text}")
    st.write(f"Feedback: {feedback}")
    st.write(f"Comments: {comments}")
    st.write(f"Model: {add_selectbox}")
    st.write(f"Class Choice: {class_choice}")

    if name and input_text and feedback is not None and comments and add_selectbox:
        insert_feedback(name, input_text, feedback, comments, add_selectbox, class_choice)
        st.write("Feedback submitted successfully.")
    else:
        st.write("Please fill in all required fields.")
