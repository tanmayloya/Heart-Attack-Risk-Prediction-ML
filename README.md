# ❤️ Heart Attack Risk Prediction System

## 📌 Project Overview

This project is a **Machine Learning-based Heart Attack Risk Prediction System** that analyzes clinical parameters to estimate whether a patient is at risk of a heart attack.

The model uses medical indicators such as **age, heart rate, blood pressure, blood sugar levels, Troponin, and CK-MB** to predict the probability of a heart attack.

To make the system interactive and user-friendly, the trained model is deployed using a **Streamlit web application**, allowing users to enter patient details and receive instant risk predictions.

---

## 🎯 Objectives

* Build a machine learning model to predict heart attack risk.
* Analyze the importance of clinical features in prediction.
* Provide an easy-to-use **web interface for medical risk assessment**.
* Demonstrate a real-world **ML deployment using Streamlit**.

---

## 🧠 Features

* Clinical parameter input interface
* Machine learning prediction model
* Risk probability visualization
* Risk classification (Low Risk / High Risk)
* Analyst summary of patient data
* Interactive Streamlit dashboard

---

## 📊 Input Features

The model considers the following medical parameters:

* Age
* Gender
* Heart Rate (bpm)
* Systolic Blood Pressure (mm Hg)
* Diastolic Blood Pressure (mm Hg)
* Blood Sugar (mg/dL)
* CK-MB Level (ng/mL)
* Troponin Level (ng/mL)

These biomarkers are commonly used in **cardiovascular risk assessment**.

---

## 🏥 Output

The system provides:

* **Risk Prediction**

  * Low Risk / No Immediate Threat
  * High Risk of Heart Attack

* **Prediction Probability**

  * Displays model confidence as a probability score.

* **Risk Visualization**

  * Progress bar showing predicted probability.

---

## ⚙️ Technologies Used

**Programming Language**

* Python

**Libraries**

* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Seaborn

**Deployment**

* Streamlit

---

## 📂 Project Structure

```
Heart-Attack-Risk-Prediction
│
├── app.py                # Streamlit application
├── HeartAttack.ipynb     # Model training notebook
├── model.pkl             # Trained machine learning model
├── dataset.csv           # Dataset used for training
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/Heart-Attack-Risk-Prediction.git
```

### 2️⃣ Navigate to the Project Folder

```
cd Heart-Attack-Risk-Prediction
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit Application

```
streamlit run app.py
```

The application will open in your browser.

---

## 📈 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Selection
4. Model Training
5. Model Evaluation
6. Feature Importance Analysis
7. Deployment using Streamlit

---

## 📷 Application Interface


Summary 
![image.alt](https://github.com/tanmayloya/Heart-Attack-Risk-Prediction-ML/blob/46f02890a021ca8c157f2e0cccaacccf89802067/summary.png)
---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**.
It should not be used as a substitute for professional medical diagnosis.

---

## 👨‍💻 Author

**Tanmay Loya**

Machine Learning & AI Enthusiast
Engineering Student

---
