import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score, classification_report
from spellchecker import SpellChecker
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import pickle

# nltk.download('punkt')
# nltk.download('stopwords')

df = pd.read_csv("data.csv")

def spell(text):
    spelling = SpellChecker()
    stopword = set(stopwords.words('english'))
    words = word_tokenize(text)
    corrected_words = [spelling.correction(word) for word in words if word.lower() not in stopword]
    return " ".join(corrected_words)

df['text'] = df['text'].apply(spell)

df.dropna(inplace=True)

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['category'], test_size= 0.2)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('rf', RandomForestClassifier(random_state=42))
    ])

pipeline.fit(X_train, y_train)

with open('model.pkl', 'wb') as file:
    pickle.dump(pipeline, file)

# y_pred = model.predict(X_test)
# print("Accuracy",accuracy_score(y_test, y_pred))

y_pred = pipeline.predict(X_test)
# pipeline.save('model.keras')
print('Accuracy:',accuracy_score(y_test,y_pred))
print("classification report", classification_report(y_test,y_pred))
# sample1 = "when is exam?"
# corrected_text1 = spell(sample1)
# pred1 = pipeline.predict([corrected_text1])
# print(pred1)
# with open('model.pkl', 'rb') as file:
#     model = pickle.load(file)



