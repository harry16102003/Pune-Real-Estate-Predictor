import streamlit as st
import joblib
import json
import numpy as np
import os

# --- PATHS TO MODEL FILES ---
# This makes sure the app can find the files from where it's run.
# Assumes your folder structure is:
# PuneRealEstate/
# |-- app/
# |   `-- predictor_app.py
# |-- models/
# |   |-- pune_house_price_model.pkl
# |   `-- model_columns.json

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'pune_house_price_model.pkl')
COLUMNS_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'model_columns.json')


# --- LOAD THE SAVED MODEL AND COLUMNS ---
@st.cache_resource
def load_model():
    """Loads the trained model and column data from disk."""
    try:
        model = joblib.load(MODEL_PATH)
        with open(COLUMNS_PATH, 'r') as f:
            columns_data = json.load(f)
            model_columns = columns_data['columns']
        return model, model_columns
    except FileNotFoundError:
        st.error(f"Error: Model or column file not found. Please ensure '{MODEL_PATH}' and '{COLUMNS_PATH}' exist.")
        return None, None

model, model_columns = load_model()


# --- WEB APP UI ---
st.set_page_config(page_title="Pune House Price Predictor", page_icon="🏠", layout="centered")
st.title("🏠 Pune Real Estate Price Predictor")
st.write(
    "Welcome! This app uses a machine learning model to predict the price of a house "
    "in Pune based on its key features. Please provide the details of the property in the sidebar."
)

# --- SIDEBAR FOR USER INPUT ---
st.sidebar.header("Enter Property Details")

if model_columns:
    # Get all location names from the model columns (they don't contain '_')
    locations = sorted([col for col in model_columns if '_' not in col and col not in ['total_sqft', 'bath', 'bhk', 'balcony']])
    
    # Create input fields
    location = st.sidebar.selectbox("Location", locations)
    total_sqft = st.sidebar.number_input("Total Square Feet", min_value=300, max_value=20000, value=1200, step=50)
    bhk = st.sidebar.slider("Number of BHK (Bedrooms)", 1, 10, 2)
    bath = st.sidebar.slider("Number of Bathrooms", 1, 12, 2)
    balcony = st.sidebar.slider("Number of Balconies", 0, 4, 1)

    # --- PREDICTION LOGIC ---
    if st.sidebar.button("Predict Price", type="primary"):
        if model is not None:
            # Create a numpy array with the correct number of columns, filled with zeros
            input_data = np.zeros(len(model_columns))

            # Find the index of the selected location and set it to 1
            try:
                loc_index = model_columns.index(location.lower())
                if loc_index >= 0:
                    input_data[loc_index] = 1
            except ValueError:
                # This case should ideally not happen if location list is generated from columns
                st.error("Invalid location selected.")
                st.stop()
            
            # Set the values for the other features at their correct indices
            input_data[model_columns.index('total_sqft')] = total_sqft
            input_data[model_columns.index('bath')] = bath
            input_data[model_columns.index('bhk')] = bhk
            input_data[model_columns.index('balcony')] = balcony

            # Reshape for the model and make a prediction
            prediction = model.predict([input_data])
            predicted_price = prediction[0]

            # Display the result
            st.success(f"**Predicted Price: ₹ {predicted_price:,.2f} Lakhs**")
        else:
            st.error("Model could not be loaded. Please check the file paths.")
else:
    st.warning("Could not load model data. The application cannot function.")
