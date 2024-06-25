import keyword_extraction
import model_based
from spellchecker import SpellChecker
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import yake
import numpy as np

def pred(question, model_name):
    key = keyword_extraction.important_words
    classes = ["events", "exam", "notes", "subject", "schedule", "question paper", "calendar", "score", "important question", "assignments"]

    def spell(text):
            spelling = SpellChecker()
            stopword = set(stopwords.words('english'))
            words = word_tokenize(text)
            corrected_words = [spelling.correction(word) for word in words if word.lower() not in stopword and word not in string.punctuation]
            return " ".join(corrected_words)

    def extraction(words):
        yake_kw = yake.KeywordExtractor() 
        KeyWords = yake_kw.extract_keywords(words) 
        keywords_event = [[kw,_] for kw, _ in KeyWords if len(kw.split()) == 1]
        val = sorted(keywords_event, key = lambda x:x[1], reverse= True)
        result = [t[0] for t in val]
        return " ".join(result)

    '''while True:
        question = input("enter 'Q' to exit: ")
        if question == 'q' or question == 'Q':
            break'''
    words = spell(question)
    words = extraction(question).split()
    evaluation = {}
    for i in words:
        for c in classes:
            if i in key[c]:
                evaluation = model_based.prediction(i, model_name)
    if evaluation == {}:
        #print("Unknown Category")                
        return ["Unknown Category"]
    else:
        #print(evaluation)
        max_key = max(evaluation, key=evaluation.get)
        # Print the key and corresponding value
        #print("Key:", max_key)
        #print("Value:", evaluation[max_key])
        return [max_key, evaluation[max_key]]