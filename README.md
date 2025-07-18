# 🛡️ Phishing URL Detector

This project is a machine learning–based phishing URL detection system built with **Python**, **Flask**, and **XGBoost**. It classifies URLs as either **Legitimate ✅** or **Phishing ⚠️** based on extracted features.

---

## 📌 Project Features

- 🔎 Detects phishing websites based on URL patterns
- ⚙️ Trained with XGBoost classifier using 7 URL-based features
- 🌐 Flask web interface for real-time URL classification
- 💾 CSV dataset support for training
- 🧠 Easy-to-understand feature extraction logic

---

## 🧠 Tech Stack

| Layer       | Technology         |
|-------------|--------------------|
| Backend     | Python 3.7.2       |
| Framework   | Flask              |
| ML Model    | XGBoost            |
| Frontend    | HTML + Inline CSS  |
| Data        | Custom CSV dataset |
| Hosting     | Localhost (Flask)  |

---

## 🏗️ Features Extracted from URL

The following 7 features are extracted from each URL:

1. **Has 'http'**
2. **Length of URL**
3. **Number of dots `.`**
4. **Contains '@'**
5. **Contains '//'**
6. **Contains '-'**
7. **Starts with 'https'**

---

## 🚀 How to Run This Project
✅ Step 1: Clone the repository
bash
git clone https://github.com/01naresh/phishing-url-detector.git
cd phishing-url-detector
---
✅ Step 2: Install required packages
bash
pip install flask pandas xgboost numpy
---
✅ Step 3: Train the model (if not already trained)
bash
python train_model.py
---
✅ Step 4: Run the Flask app
bash
python app.py
---
✅ Step 5: Open your browser
cpp
http://127.0.0.1:5000
---

📜 License
This project is open-source and free to use under the MIT License.
---

🙋‍♂️ Author
Naresh Akula
GitHub: @01naresh
---
