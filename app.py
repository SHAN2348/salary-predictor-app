
# Web App: Salary Predictor using Streamlit
# Features: Experience, Education Level, Job Title, Company, Location

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Sample dataset (you can replace with real-world dataset)
data = pd.DataFrame({
    'YearsExperience': [1, 2, 3, 4, 5, 6, 7],
    'Education': ['Bachelors', 'Masters', 'PhD', 'Bachelors', 'Masters', 'PhD', 'Bachelors'],
    'JobTitle': ['Developer', 'Data Scientist', 'Manager', 'Developer', 'Manager', 'Data Scientist', 'Developer'],
    'Company': ['Google', 'Amazon', 'Microsoft', 'Amazon', 'Google', 'Meta', 'Meta'],
    'Location': ['New York', 'San Francisco', 'Seattle', 'Austin', 'Seattle', 'New York', 'Austin'],
    'Salary': [60000, 80000, 120000, 65000, 115000, 130000, 70000]
})

# Separate features and target
X = data.drop('Salary', axis=1)
y = data['Salary']

# Preprocessing for categorical data
categorical_features = ['Education', 'JobTitle', 'Company', 'Location']
numerical_features = ['YearsExperience']

preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(), categorical_features),
    ('num', 'passthrough', numerical_features)
])

# Build the pipeline
model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Train the model
model.fit(X, y)

# Streamlit App
st.title("💼 Salary Predictor")
st.write("Predict salary based on experience, education, job title, company, and location.")

# User inputs
experience = st.slider("Years of Experience", 0, 20, 1)
education = st.selectbox("Education Level", data['Education'].unique())
job_title = st.selectbox("Job Title", data['JobTitle'].unique())
company = st.selectbox("Company", data['Company'].unique())
location = st.selectbox("Location", data['Location'].unique())

# Prediction
if st.button("Predict Salary"):
    input_df = pd.DataFrame({
        'YearsExperience': [experience],
        'Education': [education],
        'JobTitle': [job_title],
        'Company': [company],
        'Location': [location]
    })
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Salary: ₹{int(prediction):,}")
