import pandas as pd
import joblib
from xgboost import XGBClassifier
from features import get_url_features

# Load dataset
data = pd.read_csv("phishing_dataset.csv")

# Drop rows with NA values
data.dropna(inplace=True)

# Ensure labels are integers
data["Label"] = data["Label"].astype(int)

# Extract features and wrap in DataFrame with correct column names
features_list = [get_url_features(url) for url in data["URL"]]
X = pd.DataFrame(features_list, columns=[f"f{i}" for i in range(7)])
y = data["Label"]

# Train the model
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X, y)

# Save the model
joblib.dump(model, "phishing_model.pkl")
print("✅ Model trained and saved with proper features and label handling.")
