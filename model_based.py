import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from spellchecker import SpellChecker
import numpy as np
import azure_model

ans = {}
def prediction(corrected_question,model_name):
    
    def pred_confidence(model, X):
        if hasattr(model, "predict_proba"):
            y_pred_prob = model.predict_proba(X)
            return y_pred_prob
        elif hasattr(model, "decision_function"):
            y_pred_prob = model.decision_function(X)
            return (y_pred_prob - y_pred_prob.min()) / (y_pred_prob.max() - y_pred_prob.min())
        
    def log_reg(corrected_question):
    #print("LOGISCTIC REGRESSION")
        with open(r'LOGISTIC REGRESSION\model_logreg.pkl', 'rb') as file:
            model1 = pickle.load(file)
        prediction = model1.predict([corrected_question])
        con_score = pred_confidence(model1, [corrected_question])
        ans[tuple(prediction)] = max(con_score[0])
        print(log_reg)

    #print("\nNAIVE BAYES")
    def naive_bayes(corrected_question):
        with open(r'NAIVE_BAYES\model_naive.pkl', 'rb') as file:
            model2 = pickle.load(file)
        prediction = model2.predict([corrected_question])
        con_score = pred_confidence(model2, [corrected_question])
        ans[tuple(prediction)] = max(con_score[0])
        print(naive_bayes)

    #print("\nRANDOM FOREST")
    def random_forest(corrected_question):
        with open(r'RANDOM_FOREST_CLASSIFIER\model_rfc.pkl', 'rb') as file:
            model3 = pickle.load(file)   
        prediction = model3.predict([corrected_question])
        con_score = pred_confidence(model3, [corrected_question])
        ans[tuple(prediction)] = max(con_score[0])
        print(random_forest)

    # #print("\nSVM")
    def svm(corrected_question):
        with open(r'SVM\model_svm.pkl', 'rb') as file:
            model4 = pickle.load(file)
        prediction = model4.predict([corrected_question])
        con_score = pred_confidence(model4, [corrected_question])
        ans[tuple(prediction)] = max(con_score[0])
        print("svm")
    
    if model_name == "Random Forest":
        random_forest(corrected_question)
    elif model_name == "Naive Bayes":
        naive_bayes(corrected_question)
    elif model_name == "Logistic Regression":
        log_reg(corrected_question)
    elif model_name == "SVM":
        svm(corrected_question)
    elif model_name == "AZURE MODEL":
        return azure_model.sample_classify_document_single_label(corrected_question)


    
    return ans
