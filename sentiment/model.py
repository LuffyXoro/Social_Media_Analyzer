import nltk
nltk.download('movie_reviews')
nltk.download('punkt')

import os
import nltk
import joblib
from nltk.corpus import movie_reviews

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression # type: ignore
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score, classification_report

def load_labeled_data():
    texts = []
    labels = []
    for category in movie_reviews.categories():
        for fileid in movie_reviews.fileids(category):
            text=movie_reviews.raw(fileid)
            texts.append(text)
            labels.append(category)
    return texts,labels

def train_sentiment_model():
    texts,labels=load_labeled_data()

    vectorizer=TfidfVectorizer(stop_words='english', max_features=5000)
    X=vectorizer.fit_transform(texts)
    X_train,X_test,y_train,y_test=train_test_split(X,labels,test_size=0.2,random_state=42)
    

    model=LogisticRegression(max_iter=100)
    model.fit(X_train,y_train)

    y_pred=model.predict(X_test)
    print("Accuracy:",accuracy_score(y_test,y_pred))
    print("Classification Report:\n",classification_report(y_test,y_pred))

    joblib.dump(model,'sentiment/sentiment_model.pkl')
    joblib.dump(vectorizer,'sentiment/vectorizer.pkl')
              
MODEL_PATH = os.path.join("sentiment", "sentiment_model.pkl")
VECTORIZER_PATH = os.path.join("sentiment", "vectorizer.pkl")

if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
    sentiment_model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
else:
    sentiment_model = None
    vectorizer = None

def predict_sentiment(text):      # input:cleaned text ; output:semtiment label (pos/neg)
    if not isinstance(text,str) or not text.strip():
        return "neutral"
    if sentiment_model is None or vectorizer is None:
        raise ValueError("Not trained model. Please train the model first.Refer to train_sentiment_model() funstion.")
    
    x=vectorizer.transform([text])
    prediction=sentiment_model.predict(x)[0]

    return prediction



# if __name__=="__main__":
#     train_sentiment_model()








