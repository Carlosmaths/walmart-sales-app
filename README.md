# 🛒 Walmart Sales Predictor App

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-ff4b4b.svg)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange.svg)
![Status](https://img.shields.io/badge/Status-Deployed-success.svg)

## 🚀 Live Demo
Check out the live application here! 👇
**[🔗 Access Walmart Sales Predictor](https://carlosmaths-walmart-sales-app-app-gw2a5u.streamlit.app/)**

---

## 📖 Project Overview

This project is an **End-to-End Data Science solution** designed to forecast weekly sales for specific Walmart departments.

Beyond mathematical accuracy, the goal was to build a user-friendly **Decision Support Tool** for store managers. It allows non-technical stakeholders to simulate different scenarios (e.g., holiday seasons, store size impact) to optimize inventory and staffing decisions.

### 🎯 Key Features
* **Interactive Interface:** Built with **Streamlit** for a seamless, real-time user experience.
* **Predictive Power:** Powered by a **Random Forest Regressor**, capturing complex non-linear relationships and seasonality in sales data.
* **Web Optimization:** Implemented a "Lite" model architecture (pruned and compressed) to reduce load times by 99% without significant performance loss.

---

## 🛠️ Tech Stack & Architecture

* **Language:** Python
* **Machine Learning:** Scikit-Learn (Random Forest)
* **Data Processing:** Pandas, NumPy
* **Frontend:** Streamlit
* **Deployment:** Streamlit Cloud (CI/CD via GitHub)
* **Serialization:** Joblib (LZMA Compression)

---

## 📊 Model Performance & Optimization

The development process involved two distinct modeling stages to balance accuracy with engineering constraints:

1.  **Research Model (Development Phase):**
    * *Algorithm:* Random Forest (50 Estimators, Max Depth 20).
    * *Accuracy ($R^2$):* **97.2%**
    * *Purpose:* In-depth analysis and Feature Importance extraction.
    * *Issue:* High file size (>140 MB) causing latency in cloud deployment.

2.  **Production Model (Deployment Phase):**
    * *Optimization:* Pruning trees and reducing depth to optimize I/O operations.
    * *File Size:* Reduced from **142 MB** to **0.75 MB**.
    * *Accuracy ($R^2$):* **~88.5%**
    * *Result:* Instant web loading with reliable trend forecasting.

---

## 📂 Repository Structure

```text
├── app.py                     # Streamlit Application source code (Frontend & Backend logic)
├── walmart_sales_model.pkl    # Serialized Trained Model (Lite/Compressed version)
├── requirements.txt           # Dependency list for production environment
└── README.md                  # Project Documentation

💻 Local Installation
To run this project on your local machine:

1. Clone the repository: Bash
git clone [https://github.com/Carlosmaths/walmart-sales-app.git](https://github.com/Carlosmaths/walmart-sales-app.git)
cd walmart-sales-app

2. Install dependencies: Bash
pip install -r requirements.txt

3. Run the application: Bash
streamlit run app.py

Author:
Carlos Barrios: Mathematician | University Professor | Data Scientist

LinkedIn: https://www.linkedin.com/in/carlos-barrios-matematicas-fisica-machinelearning/
GitHub: https://github.com/Carlosmaths
