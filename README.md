# Pune Real Estate Price Predictor & Analysis Tool

## Overview

This project is an end-to-end data science solution designed to analyze the Pune real estate market. It leverages data cleaning, feature engineering, and machine learning to provide two primary outputs: an interactive analytical dashboard and a live price prediction web application. This repository contains all the necessary code, data, and models to replicate the project.

---

## 🚀 Key Features

* **Interactive Dashboard:** A comprehensive 4-page Power BI dashboard for exploring historical market trends, price distributions, and detailed property feature analysis.
* **Live Prediction App:** A user-friendly web application built with Streamlit that uses a trained XGBoost model to predict property prices in real-time based on user inputs.
* **Data-Driven Analysis:** The entire project is based on a detailed analysis of a real-world housing dataset, performed in a Jupyter Notebook.
* **End-to-End Workflow:** Demonstrates the complete data science lifecycle, from data ingestion and cleaning to model deployment in a web app.

---

## 🔗 Live Demos & Screenshots

* **Live Streamlit App:** [**`<< CLICK HERE  >>`**](https://pune-real-estate-predictor-jh67jg6n2k44xtcrkrqc8z.streamlit.app/)
* **Published Power BI Dashboard:** [**`<< CLICK HERE >>`**](https://app.powerbi.com/groups/me/reports/556060b7-f0c5-4a92-8737-35fc565e8a60/187890696b263581466c?experience=power-bi)

---

## 🛠️ Tech Stack

* **Programming Language:** Python 3.10+
* **Data Analysis & ML:** Pandas, NumPy, Scikit-learn, XGBoost, Jupyter
* **BI & Visualization:** Power BI, Matplotlib, Seaborn
* **Web App Framework:** Streamlit

---

## 📂 Project Structure

A well-organized folder structure is crucial for this project to function correctly, especially for the Streamlit app's relative file paths.


PuneRealEstate/
├── app/
│   └── predictor_app.py         # The Streamlit web application script
├── data/
│   ├── pune_house_data.csv      # Raw, original dataset
│   ├── dashboard_data.csv       # Cleaned data for the Power BI dashboard
│   └── feature_importance.csv   # Data for the feature importance chart
├── models/
│   ├── pune_house_price_model.pkl # Saved, trained XGBoost model
│   └── model_columns.json       # List of feature columns for the model
├── notebooks/
│   └── pune_real_estate_analysis.ipynb # Jupyter Notebook with all analysis
├── Power BI/
│   └── Pune_Real_Estate_Dashboard.pbix # Power BI project file
├── screenshots/
│   ├── 1.png                    # Screenshot of the Home Page
│   └── 2.png                    # Screenshot of the Dashboard
└── requirements.txt             # Required Python libraries for deployment


---

## ⚙️ Setup and Installation

To run this project locally, please follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/Pune-Real-Estate-Predictor.git](https://github.com/your-username/Pune-Real-Estate-Predictor.git)
    cd Pune-Real-Estate-Predictor
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    Create a `requirements.txt` file in the root of your project folder with the following content, and then run the installation command.

    **`requirements.txt`:**
    ```text
    streamlit
    joblib
    numpy
    pandas
    scikit-learn
    xgboost
    ```

    **Installation command:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit App:**
    Navigate to the `app` directory and run the following command in your terminal:
    ```bash
    streamlit run predictor_app.py
    ```
    The application will open in your web browser.

---

## 🔬 Methodology

The project follows a structured data science workflow:

1.  **Data Ingestion & Cleaning:** The raw `pune_house_data.csv` was loaded into a Jupyter Notebook. Missing values were handled, and columns with inconsistent data types (like `total_sqft` containing ranges) were cleaned and standardized.
2.  **Feature Engineering:** A new `bhk` column was extracted from the `size` column, and a `price_per_sqft` feature was created to aid in outlier detection.
3.  **Outlier Removal:** Statistical methods (mean and one standard deviation) were applied on a per-location basis to remove extreme outliers that could negatively impact the model's performance.
4.  **Model Training:** The cleaned data was used to train an **XGBoost Regressor** model. The model was evaluated and achieved an R-squared score of **0.73**, indicating it can explain 73% of the price variance.
5.  **Saving Artifacts:** The trained model, along with the list of feature columns, was saved using `joblib` and `json` for use in the Streamlit application.

---

## 👨‍💻 About Me

Hello! I'm **`<< YOUR NAME >>`**, a passionate data science student with a strong interest in machine learning, data visualization, and building end-to-end data products.

This project showcases my ability to handle the entire data science lifecycle, from initial data cleaning and analysis to model deployment. I am proficient in Python, SQL, and various data analysis libraries, and I enjoy turning complex data into actionable insights.

* **LinkedIn:** [**`<< YOUR LINKEDIN PROFILE URL >>`**](https://www.linkedin.com/in/harsh-bandal-3240912b7/)
* **Email:** [**`<< YOUR EMAIL ADDRESS >>`**](harshbandal.scoe.comp@gmail.com)

