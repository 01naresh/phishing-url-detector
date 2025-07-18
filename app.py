from flask import Flask, render_template, request
import joblib
import pandas as pd
from features import get_url_features

app = Flask(__name__)
model = joblib.load("phishing_model.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    url = request.form["url"]
    features = get_url_features(url)
    features_df = pd.DataFrame([features], columns=[f"f{i}" for i in range(7)])
    prediction = model.predict(features_df)[0]
    result = "Phishing site ⚠️" if prediction == 1 else "Original site ✅"
    return render_template("result.html", url=url, result=result)

if __name__ == "__main__":
    app.run(debug=True)
