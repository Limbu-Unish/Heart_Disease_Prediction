# 🫀 Heart Disease Prediction — CLI Application

A command-line application that predicts the likelihood of heart disease in a patient based on key clinical parameters. Designed to assist healthcare professionals and individuals in making faster, data-driven cardiac health assessments.

---

## 📌 Why This Project Was Built

Heart disease remains one of the leading causes of death globally. Early detection is critical — yet many patients and even clinicians in resource-limited settings lack quick access to diagnostic support tools. Traditional diagnosis requires lab results, ECG readings, and specialist interpretation, which can be time-consuming and expensive.

This project bridges that gap by providing an instant, ML-powered prediction using widely available clinical measurements — all through a simple command-line interface that requires no internet connection or technical expertise to operate.

---

## 🧩 Problems It Solves

| Problem                                  | How This App Helps                                                   |
| ---------------------------------------- | -------------------------------------------------------------------- |
| Late detection of heart disease          | Provides instant risk prediction from routine clinical data          |
| Limited access to specialist diagnosis   | Any healthcare worker can run this tool with basic inputs            |
| Expensive diagnostic procedures          | Uses already-collected clinical measurements — no extra tests needed |
| Inconsistent manual risk assessment      | ML model gives consistent, unbiased predictions every time           |
| Complex tools with steep learning curves | Simple numbered menu — no coding or technical knowledge required     |

---

## 👨‍⚕️ How It Helps Patients

The application accepts 13 standard clinical features that are routinely collected during a cardiac checkup — such as age, blood pressure, cholesterol level, ECG results, and thalassemia type — and immediately outputs whether the patient is likely or unlikely to have heart disease.

This can be used as a **screening support tool** to:

- Flag high-risk patients for further testing or specialist referral.
- Help clinicians prioritize urgent cases in high-volume settings.
- Assist patients in understanding their cardiac risk from their own test reports.
- Support preventive care decisions before symptoms become critical.

> ⚠️ **Disclaimer:** This tool is intended as a decision-support aid only. It does not replace professional medical diagnosis. Always consult a qualified healthcare provider for clinical decisions.

---

## 🔬 How the Model Was Built

### Dataset

The model was trained on a structured heart disease dataset containing patient records with labeled outcomes (0 = No Heart Disease, 1 = Heart Disease Present). The dataset includes 13 clinical features commonly used in cardiac risk assessment.

### Features Used for Training

| Feature                     | Description                                                             |
| --------------------------- | ----------------------------------------------------------------------- |
| Age                         | Patient's age in years                                                  |
| Gender                      | 1 = Male, 0 = Female                                                    |
| Chest Pain Type             | 0 = Typical, 1 = Atypical, 2 = Non-anginal, 3 = Asymptomatic            |
| Resting Blood Pressure      | In mm Hg                                                                |
| Cholesterol                 | Serum cholesterol in mg/dl                                              |
| Fasting Blood Sugar         | 1 = > 120 mg/dl, 0 = Otherwise                                          |
| Resting ECG Results         | 0 = Normal, 1 = ST-T wave abnormality, 2 = Left ventricular hypertrophy |
| Max Heart Rate Achieved     | Numeric value                                                           |
| Exercise Induced Angina     | 1 = Yes, 0 = No                                                         |
| ST Depression (Exercise)    | Float value (e.g., 1.5)                                                 |
| ST Slope Peak Exercise      | 0 = Upsloping, 1 = Flat, 2 = Downsloping                                |
| Major Vessels (Fluoroscopy) | Count of colored vessels (0–3)                                          |
| Thalassemia Type            | 0 = Normal, 1 = Fixed defect, 2 = Reversible defect                     |

### Model Pipeline

1. **Data Preprocessing** — Handled missing values, encoded categorical variables, and ensured correct data types across all 13 features.
2. **Feature Scaling** — Applied `StandardScaler` to normalize all features to a common scale, preventing any single feature from dominating the model.
3. **Model Training** — A classification model was trained on the processed dataset to distinguish between patients with and without heart disease.
4. **Model Serialization** — Both the trained model and the fitted scaler were saved as `.pkl` files using `joblib` so they can be loaded and reused in the CLI application without retraining.

### Saved Artifacts

| File                  | Description                            |
| --------------------- | -------------------------------------- |
| `Model.pkl`           | Trained classification model           |
| `Standard_Scaler.pkl` | StandardScaler fitted on training data |

---

## 🛠️ Tools & Technologies Used

| Tool / Library   | Purpose                                                      |
| ---------------- | ------------------------------------------------------------ |
| **Python**       | Core programming language                                    |
| **pandas**       | Structuring user inputs into a DataFrame for model inference |
| **scikit-learn** | Model training, StandardScaler, and prediction               |
| **joblib**       | Saving and loading the trained model and scaler              |
| **time**         | Adds a brief processing delay for better user experience     |

---

## 🗂️ Project Structure

```
├── app.py                          # Main CLI application
├── PKL_Files/
│   ├── Model.pkl                   # Trained ML model
│   └── Standard_Scaler.pkl         # Fitted StandardScaler
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Ensure Python is installed along with the required libraries:

```bash
pip install pandas scikit-learn joblib
```

### Running the Application

```bash
python app.py
```

### Example Session

```
1. To performing the prediction.
2. To exit

Enter your choice: 1

Enter Age (years): 55
Enter Gender (1 = Male, 0 = Female): 1
Enter Chest Pain Type (0 = Typical, 1 = Atypical, 2 = Non-anginal, 3 = Asymptomatic): 3
Enter Resting Blood Pressure (mm Hg): 140
Enter Serum Cholesterol (mg/dl): 250
Fasting Blood Sugar > 120 mg/dl? (1 = True, 0 = False): 1
Resting ECG Results (0 = Normal, 1 = ST-T wave abnormality, 2 = Left ventricular hypertrophy): 1
Enter Max Heart Rate Achieved: 145
Exercise Induced Angina? (1 = Yes, 0 = No): 1
Enter ST Depression Induced by Exercise (e.g., 1.5): 2.3
Enter ST Slope Peak Exercise (0 = Upsloping, 1 = Flat, 2 = Downsloping): 2
Enter Number of Major Vessels Colored by Fluoroscopy (0-3): 1
Enter Thalassemia Type (0 = Normal, 1 = Fixed defect, 2 = Reversible defect): 2

The patient is likely to have the heart disease.
```

---

## 📝 Notes

- All inputs must be **integers** except ST Depression, which accepts a **decimal value** (e.g., `1.5`).
- The application runs in a continuous loop — enter `2` at any time to exit cleanly.
- The model performs binary classification: `1` indicates likely heart disease, `0` indicates unlikely.
