# Liver Disease Classification Project

This project explores a binary classification problem for predicting liver disease using machine learning. The workflow includes data exploration, model training, evaluation, and comparison of multiple classifiers.

## Project Overview

The dataset used in this project is stored in the data folder as Liver.csv. It contains patient health-related features and a target column named Result, where:

- 1 = Liver disease present
- 2 = Liver disease not present

The project trains and evaluates several classification models to compare their performance.

## Project Structure

- data/ - Contains the dataset files used for training and testing
- notebooks/ - Jupyter notebooks for EDA and model development
  - EDA.ipynb - Exploratory data analysis
  - model_1.ipynb - Random Forest model
  - model_2.ipynb - Decision Tree model
  - model_3.ipynb - K-Nearest Neighbors (KNN) model
  - model_4.ipynb - Naive Bayes model
  - model_comparison.ipynb - Comparison of model results
- results/ - CSV files containing model metrics and evaluation results

## Models Used

The following models were implemented and evaluated:

- Random Forest Classifier
- Decision Tree Classifier
- K-Nearest Neighbors (KNN)
- Naive Bayes Classifier

## Metrics Evaluated

The notebooks generate and save evaluation outputs such as:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC AUC
- Classification reports

## Requirements

To run the notebooks locally, install the following Python packages:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- jupyter

You can install them using:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

## How to Run

1. Open the repository folder.
2. Launch Jupyter Notebook:

```bash
jupyter notebook
```

3. Open the notebooks in the notebooks folder in the following order:
   - EDA.ipynb
   - model_1.ipynb / model_2.ipynb / model_3.ipynb / model_4.ipynb
   - model_comparison.ipynb

## Results

The trained models and their evaluation metrics are stored in the results folder as CSV files, including:

- decisiontree_results.csv
- decisiontree_classification_report.csv
- KNN_results.csv
- KNN_classification_report.csv
- randomforest_results.csv
- randomforest_classification_report.csv
- naivebayes_results.csv
- naivebayes_classification_report.csv

## Notes

This project is intended for educational and demonstration purposes, showing how to build, evaluate, and compare machine learning classifiers for a healthcare-related prediction task.
