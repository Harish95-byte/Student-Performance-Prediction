AI-Based Student Performance Prediction System
Project Overview

This project is an AI-powered Student Performance Prediction System developed using Machine Learning techniques. The system analyzes student academic and behavioral data to predict the final academic performance (G3 score) of students.

The project includes:

Data preprocessing
Feature encoding
Machine learning model training
Performance evaluation
Data visualization
Real-time prediction dashboard using Streamlit

This project demonstrates practical implementation of AI and Machine Learning concepts for educational analytics and student performance monitoring.

Features
Student performance prediction using Machine Learning
Real-time prediction dashboard
Academic performance analytics
Visualization of predicted vs actual scores
Interactive user input system
Random Forest Regression model
Model saving and reuse
Educational analytics visualization
Technologies Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib

Project Structure

student-performance-prediction/
│
├── Data/
│   └── student-mat.csv
│
├── models/
│   └── student_performance_model.pkl
│
├── output/
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── train_model.py
│   ├── evaluation.py
│   ├── visualization.py
│   └── save_model.py
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

Dataset Information

Dataset Name:
Student Performance Dataset

Dataset Source:
UCI Machine Learning Repository

Dataset File:student-mat.csv

Note:
Dataset is not included in this repository due to GitHub file management practices. Please download the dataset manually from the official source.

Machine Learning Workflow
1. Data Loading

The dataset is loaded using Pandas.

2. Data Preprocessing

Categorical values are converted into numerical format using Label Encoding.

3. Feature Selection

Relevant student academic and behavioral features are selected for prediction.

4. Model Training

A Random Forest Regressor model is trained using the processed dataset.

5. Model Evaluation

The model performance is evaluated using Mean Absolute Error (MAE).

6. Visualization

Prediction analytics and comparison graphs are generated using Matplotlib.

7. Dashboard Development

A real-time Streamlit dashboard is created for user interaction and prediction.

Model Used
Random Forest Regressor

The Random Forest Regression algorithm is used because:

it handles nonlinear data effectively,
provides strong prediction performance,
reduces overfitting,
works well with mixed feature types.
Performance Result

Example Result:
Mean Absolute Error: 1.10
A lower MAE indicates better prediction accuracy.
Dashboard Features

The Streamlit dashboard includes:

Real-time student input form
Final grade prediction
Academic performance category detection
Interactive performance analytics graph
Easy-to-use interface

Learning Outcomes
Understanding Machine Learning workflow
Data preprocessing techniques
Label encoding implementation
Regression model development
Real-time prediction systems
Dashboard development using Streamlit
Data visualization techniques
Model evaluation and analytics
Future Improvements
Deep Learning integration
Advanced feature engineering
Explainable AI integration
Student recommendation system
Cloud deployment
Multi-student analytics dashboard
Attendance intelligence system
Author

Harish Yuvaraj

AI/ML Project Developer
Seaborn
Streamlit
Joblib
