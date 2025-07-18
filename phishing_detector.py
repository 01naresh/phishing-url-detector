# phishing_detector.py
import joblib
from features import get_url_features

model = joblib.load("phishing_model.pkl")

def predict_url(url):
    features = get_url_features(url)
    return model.predict([features])[0]
