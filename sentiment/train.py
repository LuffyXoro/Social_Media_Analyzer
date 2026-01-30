# Separating the phases of training and evaluation into different functions for clarity and modularity


import joblib 


from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression # type: ignore
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


file_ids=movie_reviews.fileids()
words=movie_reviews.words()
categories=movie_reviews.categories()

pos_file_ids=movie_reviews.fileids('pos')
neg_file_ids=movie_reviews.fileids('neg')
# print(file_ids[:20])
# print(words[:20])
# print(f"Categories: {categories}")
# print(f"Positive file ids: {len(pos_file_ids)}")
# print(f"Negative file ids: {len(neg_file_ids)}")


def load_labeled_data():
    texts=[]
    labels=[]
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
    model.fit(X_train,y_train )
    y_pred=model.predict(X_test)    

    print("Accuracy:",accuracy_score(y_test,y_pred))
    print("Classification Report:\n",classification_report(y_test,y_pred))  

    joblib.dump(model,'sentiment/sentiment_model.pkl')
    joblib.dump(vectorizer,'sentiment/vectorizer.pkl')
    
with open("reports/model_report.txt","w")as f:
    f.write(classification_report(y_test,y_pred))

    