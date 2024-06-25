import pandas as pd
import yake
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk

# Ensure NLTK resources are downloaded
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
nltk.download('punkt')

stopword = set(stopwords.words('english'))
yake_kw = yake.KeywordExtractor() 
df = pd.read_csv("data.csv")
important_words = {}
wnl = WordNetLemmatizer()

#EVENTS
events = df[df['category'] == 'event']['text']
words_event = ""
for i in range(events.size):
    for j in events[i].split():
        if j.lower() not in stopword:
            words_event += " " + wnl.lemmatize(j)

KeyWords = yake_kw.extract_keywords(words_event) 
keywords_event = [kw for kw, _ in KeyWords] 
keywords_event = set(" ".join(keywords_event).split()) 
important_words["events"] = keywords_event

#EXAM
exams = df[df['category'] == 'exam']['text']
words_exam = ""
for i in exams:
    for j in i.split():
        if j.lower() not in stopword:
            words_exam += " " + wnl.lemmatize(j)
KeyWords = yake_kw.extract_keywords(words_exam) 
keywords_exam = [kw for kw, _ in KeyWords] + ["exam"]
keywords_exam = set(" ".join(keywords_exam).split())
important_words["exam"] = keywords_exam

#NOTES
notes = df[df['category'] == 'notes']['text']
words_note = ""
for i in notes:
    for j in i.split():
        if j.lower() not in stopword:
            words_note += " " + wnl.lemmatize(j)
KeyWords = yake_kw.extract_keywords(words_note) 
keywords_note = [kw for kw, _ in KeyWords] 
keywords_note = set(" ".join(keywords_note).split())
important_words["notes"] = keywords_note

#SUBJECT
subjects = df[df['category'] == 'subject']['text']
words_subject = ""
for i in subjects:
    for j in i.split():
        if j.lower() not in stopword:
            words_subject += " " + wnl.lemmatize(j)
KeyWords = yake_kw.extract_keywords(words_subject) 
keywords_subject = [kw for kw, _ in KeyWords] 
keywords_subject = set(" ".join(keywords_subject).split())
important_words["subject"] = keywords_subject

#SCHEDULE
schedules = df[df['category'] == 'schedule']['text']
words_schedule = ""
for i in schedules:
    for j in i.split():
        if j.lower() not in stopword:
            words_schedule += " " + wnl.lemmatize(j)
KeyWords = yake_kw.extract_keywords(words_schedule) 
keywords_schedule = [kw for kw, _ in KeyWords] 
keywords_schedule = set(" ".join(keywords_schedule).split())
important_words["schedule"] = keywords_schedule

#QUESTION PAPER
question_papers = df[df['category'] == 'question paper']['text']
words_question_paper = ""
for i in question_papers:
    for j in i.split():
        if j.lower() not in stopword:
            words_question_paper += " " + wnl.lemmatize(j)
KeyWords = yake_kw.extract_keywords(words_question_paper) 
keywords_question_paper = [kw for kw, _ in KeyWords] 
keywords_question_paper = set(" ".join(keywords_question_paper).split())
important_words["question paper"] = keywords_question_paper

#CALENDAR
calendars = df[df['category'] == 'calendar']['text']
words_calendar = ""
for i in calendars:
    for j in i.split():
        if j.lower() not in stopword:
            words_calendar += " " + wnl.lemmatize(j)
KeyWords = yake_kw.extract_keywords(words_calendar) 
keywords_calendar = [kw for kw, _ in KeyWords] 
keywords_calendar = set(" ".join(keywords_calendar).split())
important_words["calendar"] = keywords_calendar

#SCORE
scores = df[df['category'] == 'score']['text']
words_score = ""
for i in scores:
    for j in i.split():
        if j.lower() not in stopword:
            words_score += " " + wnl.lemmatize(j)
KeyWords = yake_kw.extract_keywords(words_score) 
keywords_score = [kw for kw, _ in KeyWords] 
keywords_score = set(" ".join(keywords_score).split())
important_words["score"] = keywords_score

#IMPORTANT QUESTION
important_questions = df[df['category'] == 'important question']['text']
words_important_question = ""
for i in important_questions:
    for j in i.split():
        if j.lower() not in stopword:
            words_important_question += " " + wnl.lemmatize(j)
KeyWords = yake_kw.extract_keywords(words_important_question) 
keywords_important_question = [kw for kw, _ in KeyWords] 
keywords_important_question = set(" ".join(keywords_important_question).split())
important_words["important question"] = keywords_important_question

#ASSIGNMENTS
assignments = df[df['category'] == 'assignments']['text']
words_assignment = ""
for i in assignments:
    for j in i.split():
        if j.lower() not in stopword:
            words_assignment += " " + wnl.lemmatize(j)
KeyWords = yake_kw.extract_keywords(words_assignment) 
keywords_assignment = [kw for kw, _ in KeyWords] 
keywords_assignment = set(" ".join(keywords_assignment).split())
important_words["assignments"] = keywords_assignment

# print("events\n", keywords_event) 
# print("exam\n", keywords_exam)
# print("notes\n", keywords_note)
# print("subjects\n", keywords_subject)
# print("schedule\n", keywords_schedule)
# print("question paper\n", keywords_question_paper)
# print("calendar\n", keywords_calendar)
# print("score\n", keywords_score)
# print("important question\n", keywords_important_question)
# print("assignments\n", keywords_assignment)

# print(important_words)
