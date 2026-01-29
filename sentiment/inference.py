import joblib
import os

MODEL_PATH = "sentiment/sentiment_model.pkl"
VECTORIZER_PATH = "sentiment/vectorizer.pkl"

if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
    raise RuntimeError("Model not trained. Run train.py first.")

sentiment_model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def predict_sentiment(text):
    if not isinstance(text, str) or not text.strip():
        return "unknown"

    X = vectorizer.transform([text])
    return sentiment_model.predict(X)[0]

def predict_sentiment_confidence(text):
    if not isinstance(text,str) or not text.strip():
        return None,0.0
    X = vectorizer.transform([text])
    probs=sentiment_model.predict_proba(X)[0]

    label=sentiment_model.classes_[probs.argmax()]
    confidence=probs.max()

    return label, confidence


