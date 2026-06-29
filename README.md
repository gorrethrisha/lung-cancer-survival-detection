# Lung Cancer Survival Detection

## Project Overview

This project develops a machine learning-based Lung Cancer Survival Prediction system to determine whether a patient survives lung cancer treatment using various patient and treatment-related features.

## Objective

The primary objective of this project is to develop a machine learning model that can detect patient survival outcomes while identifying the most effective classification algorithm for the problem.

## Dataset Information

* Total Records: **890,000**
* Total Features: **17**
* Target Variable: **survived**

  * `0` → Did Not Survive
  * `1` → Survived

### Features Used for Training

* age
* gender
* country
* cancer_stage
* family_history
* smoking_status
* bmi
* cholesterol_level
* hypertension
* asthma
* cirrhosis
* other_cancer
* treatment_type

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

## Methodology

The following steps were followed during the development of the project:

1. Data Overview
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature and Target Separation
5. Train-Test Split
6. Feature Scaling
7. Model Training and Evaluation
   ○ Logistic Regression
   ○ Decision Tree
   ○ Random Forest
   ○ Random Forest with Class Weights
8. Model Comparison
9. Final Model Selection

## Model Performance

| Model                            | Accuracy | Precision | Recall   | F1 Score |
| -------------------------------- | -------- | --------- | -------- | -------- |
| Logistic Regression              | 0.779770 | 0.000000  | 0.000000 | 0.000000 |
| Decision Tree                    | 0.642888 | 0.224409  | 0.253055 | 0.237873 |
| Random Forest                    | 0.778421 | 0.227273  | 0.002551 | 0.005045 |
| Random Forest with Class Weights | 0.778685 | 0.221902  | 0.001964 | 0.003894 |

## Final Model Selection

Logistic Regression, Decision Tree, Random Forest, and Random Forest with Class Weights models were trained and evaluated for lung cancer survival detection. Although Logistic Regression and Random Forest achieved higher accuracy, they struggled to identify surviving patients and resulted in very low recall and F1-score values. Additionally, applying class weights to Random Forest did not result in any significant improvement in model performance.

Among all the models, the Decision Tree classifier demonstrated the best overall performance by achieving the highest recall and F1-score while identifying the maximum number of surviving patients.

Since correctly predicting patient survival is important in medical applications, **the Decision Tree classifier was selected as the final model for lung cancer survival Detection.**

## Conclusion

A Lung Cancer Survival Detection system was successfully developed and multiple machine learning algorithms were trained and evaluated for prediction performance. The developed system can assist in identifying patient survival outcomes and support healthcare decision-making processes.
