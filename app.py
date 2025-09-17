import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model and scaler
model=joblib.load("model.pkl")
scaler=joblib.load("scaler.pkl")

st.title("Breast Cancer Prediction App")
st.write("Predict whether a tumor is **Malignant (M)** or **Benign (B)**")

# Load dataset to get feature names
df=pd.read_csv("data_extended.csv")
df=df.drop(columns=["id","Unnamed: 32"],errors="ignore")
features=[col for col in df.columns if col!="diagnosis"]

# Collect user input
user_input=[]
for f in features:
    val=st.number_input(f"Enter {f}",value=float(df[f].mean()))
    user_input.append(val)

# Convert to array and scale
input_data=np.array(user_input).reshape(1,-1)
input_data_scaled=scaler.transform(input_data)

# Predict
if st.button("Predict"):
    pred=model.predict(input_data_scaled)[0]
    result="Malignant (M)" if pred==1 else "Benign (B)"
    st.success(f"Prediction: **{result}**")
