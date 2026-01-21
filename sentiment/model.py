import nltk
nltk.download('movie_reviews')
nltk.download('punkt')

import nltk
import joblib
from nltk.corpus import movie_reviews

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics

