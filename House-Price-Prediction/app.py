import streamlit as st
import pandas as pd
import pickle
import joblib
from pathlib import Path

# --------------------------------------------------
# File Paths
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "house_price_model.joblib"
FEATURE_PATH = BASE_DIR / "feature_columns.pkl"
DATA_PATH = BASE_DIR / "Bengaluru_House_Data.csv"

# --------------------------------------------------
# Load Files
# --------------------------------------------------
model = joblib.load(MODEL_PATH)

with open(FEATURE_PATH, "rb") as f:
    feature_columns = pickle.load(f)

df = pd.read_csv(DATA_PATH)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Bengaluru House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Bengaluru House Price Prediction")

st.write("Predict the estimated selling price of a house using Machine Learning.")

st.markdown("---")

# --------------------------------------------------
# User Inputs
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    total_sqft = st.number_input(
        "Total Square Feet",
        min_value=100.0,
        value=1000.0
    )

    bath = st.number_input(
        "Bathrooms",
        min_value=1,
        value=2
    )

    bhk = st.number_input(
        "BHK",
        min_value=1,
        value=2
    )

with col2:
    balcony = st.number_input(
        "Balcony",
        min_value=0,
        value=1
    )

    area_type = st.selectbox(
        "Area Type",
        sorted(df["area_type"].dropna().unique())
    )

    availability = st.selectbox(
        "Availability",
        sorted(df["availability"].dropna().unique())
    )

location = st.selectbox(
    "Location",
    sorted(df["location"].dropna().unique())
)

st.markdown("---")

# --------------------------------------------------
# Prediction
# --------------------------------------------------
if st.button("Predict Price", use_container_width=True):

    input_df = pd.DataFrame(columns=feature_columns)
    input_df.loc[0] = 0

    input_df.at[0, "total_sqft"] = total_sqft
    input_df.at[0, "bath"] = bath
    input_df.at[0, "balcony"] = balcony
    input_df.at[0, "bhk"] = bhk

    area_col = f"area_type_{area_type}"
    if area_col in input_df.columns:
        input_df.at[0, area_col] = 1

    availability_col = f"availability_{availability}"
    if availability_col in input_df.columns:
        input_df.at[0, availability_col] = 1

    location_col = f"location_{location}"
    if location_col in input_df.columns:
        input_df.at[0, location_col] = 1

    prediction = model.predict(input_df)[0]

    st.success(f"🏠 Estimated House Price: ₹ {prediction:.2f} Lakhs")

st.markdown("---")
st.caption("Developed by Keerthi Sri")
