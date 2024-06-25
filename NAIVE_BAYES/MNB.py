import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from spellchecker import SpellChecker
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import pickle

# nltk.download('punkt')
# nltk.download('stopwords')

#data = {'text':['when my exam', 'when my timetable', 'today event', 'what my schedule', 'my score'], 'category':['exam','schedule','event', 'schedule','score']}

df = pd.read_csv("data.csv")

#print(df)

def spell(text):
    spelling = SpellChecker()
    stopword = set(stopwords.words('english'))
    words = word_tokenize(text)
    corrected_words = [spelling.correction(word) for word in words if word.lower() not in stopword]
    #corrected_words = [word for word in words if word.lower() not in stopword]
    return " ".join(corrected_words)

df['text'] = df['text'].apply(spell)

# Drop rows with NaN values
df.dropna(inplace=True)

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['category'], test_size= 0.2)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('nb', MultinomialNB())
    ])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print('Accuracy:',accuracy_score(y_test,y_pred))

print("classification report", classification_report(y_test,y_pred))

# sample1 = "wen is eaxm?"
# corrected_text1 = spell(sample1)
# pred1 = pipeline.predict([corrected_text1])
# print(pred1)

with open('model.pkl', 'wb') as file:
    pickle.dump(pipeline, file)
