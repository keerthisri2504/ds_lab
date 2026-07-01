# 🏠 Bengaluru House Price Prediction

A Machine Learning web application that predicts the selling price of houses in Bengaluru based on various property features such as area, BHK, bathrooms, balcony, location, and availability.

---

## 📌 Project Overview

This project uses Machine Learning algorithms to estimate house prices in Bengaluru. The application is built using **Python**, **Scikit-learn**, and **Streamlit**.

The project demonstrates the complete Data Science lifecycle:

- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Building
- Model Evaluation
- Deployment

---

## 🚀 Features

- Predict house prices instantly
- Interactive Streamlit web application
- User-friendly interface
- Data preprocessing
- Feature engineering
- Machine Learning prediction
- Real-time price estimation

---

## 📂 Dataset

**Dataset Name:** Bengaluru House Price Dataset

The dataset contains information such as:

- Area Type
- Availability
- Location
- Total Square Feet
- Number of Bathrooms
- Balcony
- BHK
- Price

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

## 🤖 Machine Learning Models Used

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor ✅ (Best Model)

---

## 📊 Model Performance

| Model | R² Score |
|--------|----------|
| Linear Regression | 0.53 |
| Decision Tree | 0.40 |
| Random Forest | **0.63** |

Random Forest gave the best performance and was selected for deployment.

---

## 📁 Project Structure

```
House-Price-Prediction
│
├── app.py
├── Bengaluru_House_Data.csv
├── House_Price_Prediction.ipynb
├── house_price_model.joblib
├── feature_columns.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run the Project

### Clone the Repository

```bash
git clone https://github.com/keerthisri2504/Data-Science.git
```

Navigate to the project folder:

```bash
cd Data-Science/House-Price-Prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

---

## 📸 Application Preview

*(Add your application screenshot here after deployment.)*

---

## 👩‍💻 Author

**Keerthi Sri**

B.Tech Student

Machine Learning & Data Science Enthusiast

---

## ⭐ Future Improvements

- Improve prediction accuracy
- Hyperparameter tuning
- Deploy using Docker
- Add map-based location selection
- Support multiple cities
