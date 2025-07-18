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
🖼️ Screenshots
---

<img width="1750" height="984" alt="Screenshot 2025-07-19 004751" src="https://github.com/user-attachments/assets/5b6a463c-cda2-4181-977d-07dda8a70278" />
---
<img width="922" height="563" alt="Screenshot 2025-07-19 004815" src="https://github.com/user-attachments/assets/218cfedf-5d39-4eac-84dc-23c862b0e410" />
---
<img width="941" height="574" alt="Screenshot 2025-07-19 004832" src="https://github.com/user-attachments/assets/dc1b0889-1651-442c-a1d1-458f6baaeacb" />
---
<img width="768" height="449" alt="Screenshot 2025-07-19 004850" src="https://github.com/user-attachments/assets/4aaef829-0890-4575-bd2d-61ebfe44b2c9" />
---




