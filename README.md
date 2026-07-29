# Liver Disease Classification Project

This project builds a machine learning system to predict liver disease from patient health indicators. It includes data analysis, model training, evaluation, comparison of multiple classifiers, and an interactive Streamlit web app.

## Dataset

The dataset used in this project is available from Kaggle:
https://www.kaggle.com/datasets/abhi8923shriv/liver-disease-patient-dataset/data

The target column is Result, where:
- 1 = Liver disease present
- 2 = Liver disease not present

## What’s New

This version of the project includes:
- A Streamlit-based GUI for real-time prediction in app.py
- Multiple trained classification models
- A deployed web app on Streamlit Community Cloud

## Features

- Predicts whether a patient is likely to have liver disease
- Provides an easy-to-use web interface for medical input values
- Compares several machine learning models for performance
- Includes saved evaluation results for analysis

## How It Works

1. The dataset is loaded and preprocessed.
2. Multiple classification models are trained and evaluated.
3. The best-performing model is saved for deployment.
4. The Streamlit app accepts patient input and returns a prediction.

## Live Demo

You can try the deployed app here:
https://liver-disease-2026.streamlit.app/

## Project Structure

- app.py - Streamlit web application for prediction
- data/ - Training and testing datasets
- models/ - Trained model files, including best_model.joblib
- notebooks/ - Jupyter notebooks for EDA and model development
- results/ - CSV files with model metrics and classification reports

## Models Used

The following models were implemented and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- Naive Bayes Classifier
- Support Vector Machine (SVM)

## Evaluation Metrics

The notebooks and result files include metrics such as:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC AUC
- Classification report

## Requirements

Install the required Python packages:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib streamlit jupyter
```

## How to Run Locally

1. Open the project folder.
2. Start the Streamlit app:

```bash
streamlit run app.py
```

3. Open the notebook files in the notebooks folder for model training and comparison.

## Results

The trained model results are saved in the results folder, including files such as:

- decisiontree_results.csv
- decisiontree_classification_report.csv
- KNN_results.csv
- KNN_classification_report.csv
- logisticregression_results.csv
- logisticregression_classification_report.csv
- NaiveBayes_results.csv
- NaiveBayes_classification_report.csv
- randomforest_results.csv
- randomforest_classification_report.csv
- svm_results.csv
- svm_classification_report.csv

## Notes

This project is intended for educational and demonstration purposes, showing how to build, evaluate, compare, and deploy a healthcare prediction model using Python and Streamlit.
