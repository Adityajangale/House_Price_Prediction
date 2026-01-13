import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('house_price_model.pkl', 'rb'))

# App title
st.title("🏠 House Price Prediction App")

# User input
st.header("Enter the details:")
MedInc = st.number_input("Median Income (in tens of thousands)", min_value=0.0)
HouseAge = st.number_input("House Age", min_value=0.0)
AveRooms = st.number_input("Average Rooms", min_value=0.0)
AveBedrms = st.number_input("Average Bedrooms", min_value=0.0)
Population = st.number_input("Population", min_value=1.0)
AveOccup = st.number_input("Average Occupancy", min_value=0.0)
Latitude = st.number_input("Latitude", min_value=32.0, max_value=42.0)
Longitude = st.number_input("Longitude", min_value=-125.0, max_value=-114.0)

# Prediction
if st.button("Predict Price"):
    input_data = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])
    prediction = model.predict(input_data)
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")
