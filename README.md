# Credit Card Fraud Detection Pipeline

## 📌 Project Overview
Credit card fraud costs consumers and banks billions of dollars annually. The objective of this project is to build a machine learning pipeline capable of detecting fraudulent transactions from highly imbalanced credit card data. 

Because predicting "Normal" on every transaction yields a 99.8% accuracy but catches zero fraud, this project focuses heavily on **Recall** (minimizing False Negatives) and handles extreme class imbalance using **SMOTE** (Synthetic Minority Over-sampling Technique).

## 🗄️ Data Overview
* **Source:** Kaggle Credit Card Fraud Detection Dataset (Anonymized European cardholders).
* **Class Imbalance:** 284,315 Normal transactions (99.82%) vs. 492 Fraudulent transactions (0.17%).
* **Features:** 28 PCA-transformed features, plus unscaled `Time` and `Amount`.

## ⚙️ Methodology
1. **Data Preprocessing:** Scaled `Time` and `Amount` using `RobustScaler` to handle extreme outliers.
2. **Data Splitting:** Stratified train-test split (80/20) to ensure the rare fraud cases were evenly distributed.
3. **Imbalance Handling:** Applied SMOTE *strictly to the training data* to prevent data leakage and synthesize a balanced 50/50 training set.
4. **Model Training:** Trained a baseline Logistic Regression model and an advanced Random Forest Classifier.

## 📊 Results
The models were evaluated primarily on their ability to catch actual fraud (Recall) on the unseen testing data.

* **Random Forest:** Achieved a Recall of **[Insert your RF recall, e.g., 85%]** and a Precision of **[Insert your RF precision]**. 
* **Logistic Regression:** Achieved a Recall of **[Insert your LR recall]** but struggled with a higher rate of false positives.

*The Random Forest model successfully balanced identifying fraud while minimizing the frustration of false alarms for legitimate customers.*

## 🚀 How to Run the Project
1. Clone the repository:
   `git clone https://github.com/yourusername/fraud-detection-model.git`
2. Install the required dependencies:
   `pip install -r requirements.txt`
3. Download the `creditcard.csv` dataset from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) and place it at the root of the project.
4. Run the Jupyter Notebook `01_fraud_detection.ipynb` from top to bottom.