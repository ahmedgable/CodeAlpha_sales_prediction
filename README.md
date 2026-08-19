# 📈 Advertising Sales Prediction App

An end-to-end Machine Learning web application that forecasts future sales based on advertising budgets allocated across TV, Radio, and Newspaper channels. Built with **Streamlit** and an optimized **ExtraTreesRegressor** model.

## 🚀 Live Demo
*(Optional: Insert your deployed Streamlit Cloud link here)*

## 🛠️ Tech Stack & Libraries
- **Language:** Python
- **Web Framework:** Streamlit
- **Machine Learning:** Scikit-Learn, ExtraTreesRegressor
- **Data Manipulation:** Pandas, NumPy
- **Model Serialization:** Joblib

## 📊 Model Performance
Multiple regression models were trained and evaluated using 5-Fold Cross Validation to prevent overfitting:

| Model | Test R² Score | Test MAE | Test MSE |
| :--- | :--- | :--- | :--- |
| **ExtraTreesRegressor** | **0.9885** | **0.4455** | **0.3626** |
| **RandomForestRegressor** | 0.9860 | 0.5520 | 0.4388 |
| **StackingRegressor** | 0.9858 | 0.5529 | 0.4473 |

## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/sales_prediction.git](https://github.com/YOUR_USERNAME/sales_prediction.git)
   cd sales_prediction