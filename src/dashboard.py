import streamlit as st
import requests
import json
import pandas as pd

st.title("🔐 Phishing URL Detector")
st.markdown("### A real-time detector for device security")

st.info("Enter a URL below to check if it's a phishing site.")

url_to_check = st.text_input("URL")

if st.button("Analyze URL"):
    if url_to_check:
        try:
            # Call the Flask API
            response = requests.post(
                "http://localhost:5000/predict", # Update URL if Flask server is remote
                json={"url": url_to_check}
            )
            
            if response.status_code == 200:
                result = response.json()
                prediction = result['prediction']
                
                if prediction == 'phishing':
                    st.error(f"🚨 **Warning!** This URL is likely a **{prediction}** site.")
                else:
                    st.success(f"✅ This URL appears to be **{prediction}**.")
            else:
                st.error(f"Error from API: {response.text}")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the API. Make sure `app.py` is running.")
    else:
        st.warning("Please enter a URL to analyze.")

st.markdown("---")
st.header("📊 Recent API Activity")
try:
    # Read and display the log file
    log_df = pd.read_csv('phishing_api.log', header=None, names=['timestamp', 'level', 'message'], sep=' - ')
    st.dataframe(log_df.tail(10)) # Show the 10 most recent entries
except FileNotFoundError:
    st.warning("`phishing_api.log` not found. Run the API and analyze some URLs to see activity.")