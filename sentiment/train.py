# Separating the phases of training and evaluation into different functions for clarity and modularity


import joblib 


from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression # type: ignore
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
