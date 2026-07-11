# 🧑‍⚕️ Multi-Disease Diagnosis System

A machine learning-powered web app that assesses risk for **heart disease**, **liver disease**, and **kidney disease** from patient clinical data, built with Streamlit.

🔗 **Live demo:** [my-multi-disease-diagnosis-system.streamlit.app](https://my-multi-disease-diagnosis-system.streamlit.app/)

---

## Overview

This app provides a single interface for running predictions across three independently trained classification models. Each model is packaged with its own preprocessing pipeline (via `joblib`), so raw form inputs are cleaned, encoded, and scaled consistently with how the models were trained before inference.

- **Heart Disease** — age, chest pain type, blood pressure, cholesterol, ECG results, and other cardiac indicators
- **Liver Disease** — bilirubin levels, liver enzymes, protein and albumin ratios
- **Kidney Disease** — blood pressure, glucose, urea, creatinine, blood counts, and related symptoms

## Features

- 🩺 Three independent disease prediction modules in one app
- 🎛️ Clean sidebar navigation with icons (`streamlit-option-menu`)
- ⚙️ Pretrained models bundled with their preprocessing pipelines for consistent inference
- ✅ Input validation to catch incomplete forms before prediction
- 🌙 Dark-themed custom UI

## Tech Stack

| Component      | Tool                       |
|-----------------|-----------------------------|
| Frontend/App    | [Streamlit](https://streamlit.io) |
| ML Models       | scikit-learn (serialized with `joblib`) |
| Data Handling   | pandas                     |
| Navigation      | streamlit-option-menu      |

## Project Structure

    Multi-Disease-Diagnosis-System/
    ├── app.py                   # Main Streamlit application
    ├── heart_disease.joblib     # Trained heart disease model + preprocessing pipeline
    ├── liver_disease.joblib     # Trained liver disease model + preprocessing pipeline
    ├── kidney_disease.joblib    # Trained kidney disease model + preprocessing pipeline
    ├── requirements.txt         # Python dependencies
    ├── runtime.txt              # Python runtime version
    └── README.md


## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/Zainab2582/Multi-Disease-Diagnosis-System.git
cd Multi-Disease-Diagnosis-System
pip install -r requirements.txt
```

### Run locally

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## Usage

1. Select a disease category from the sidebar (Heart, Liver, or Kidney)
2. Fill in the required patient details in the form
3. Click **Run Prediction**
4. View the result card showing the model's assessment

## How It Works

Each disease module follows the same pipeline:

1. **Input collection** — form values are gathered via Streamlit widgets
2. **Encoding** — categorical inputs (e.g. sex, chest pain type) are mapped to the numeric encodings the model was trained on
3. **Preprocessing** — the saved `preprocessing` transformer (scaling/encoding) is applied to the input dataframe
4. **Prediction** — the trained `model` outputs a binary classification (disease detected / not detected)

## Disclaimer

⚠️ This tool is intended for **educational and demonstration purposes only**. It is not a certified medical device and should not be used as a substitute for professional medical diagnosis, advice, or treatment. Always consult a qualified healthcare provider for medical concerns.

