# importing the necessary libraries
import pandas as pd
import joblib
import time

# Importing the model and the standard scaler
model = joblib.load('../PKL_Files/Model.pkl')
std_scale = joblib.load('../PKL_Files/Standard_Scaler.pkl')

# Creating the function to performing the prediction by taking the inputs from the user itself
def prediction():
    # Numerical Features
    age = int(input("Enter Age (years): "))
    gender = int(input("Enter Gender (1 = Male, 0 = Female): "))
    chest_pain = int(input("Enter Chest Pain Type (0 = Typical, 1 = Atypical, 2 = Non-anginal, 3 = Asymptomatic): "))
    resting_bp = int(input("Enter Resting Blood Pressure (mm Hg): "))
    cholesterol = int(input("Enter Serum Cholesterol (mg/dl): "))
    
    # Binary / Categorical Features
    fbs = int(input("Fasting Blood Sugar > 120 mg/dl? (1 = True, 0 = False): "))
    rest_ecg = int(input("Resting ECG Results (0 = Normal, 1 = ST-T wave abnormality, 2 = Left ventricular hypertrophy): "))
    max_hr = int(input("Enter Max Heart Rate Achieved: "))
    ex_angina = int(input("Exercise Induced Angina? (1 = Yes, 0 = No): "))
    
    # Continuous / Float Features
    st_depression = float(input("Enter ST Depression Induced by Exercise (e.g., 1.5): "))
    st_slope = int(input("Enter ST Slope Peak Exercise (0 = Upsloping, 1 = Flat, 2 = Downsloping): "))
    major_vessels = int(input("Enter Number of Major Vessels Colored by Fluoroscopy (0-3): "))
    thalassemia = int(input("Enter Thalassemia Type (0 = Normal, 1 = Fixed defect, 2 = Reversible defect): "))

    # Store inputs in a dictionary matching exact column names
    input_data = {
        'Age': age,
        'Gender': gender,
        'Chest_Pain_Type': chest_pain,
        'Resting_Blood_Pressure': resting_bp,
        'Cholesterol': cholesterol,
        'Fasting_Blood_Sugar': fbs,
        'Resting_ECG_Results': rest_ecg,
        'Max_Heart_Rate_Achieved': max_hr,
        'Exercise_Induced_Angina': ex_angina,
        'ST_Depression_Exercise': st_depression,
        'ST_Slope_Peak_Exercise': st_slope,
        'Major_Vessels_Colored_Fluoroscopy': major_vessels,
        'Thalassemia_Type': thalassemia
    }

    # Creating the dataframe for testing the model
    X_t = pd.DataFrame([input_data])

    # Scaling the dataframe using standarad scaler
    X_t_scaled = std_scale.transform(X_t)

    model_prediction = model.predict(X_t_scaled)

    if model_prediction[0] == 1:
        print('The patient is likey to have the heart disease.')
    elif model_prediction[0] == 0:
        print('The patient is likey to not have the heart disease.')
    else:
        print('Invalid model prediction.')

    
# Creating the function to interact with the user
def application():

    while True:
        print('1. To performing the prediction.\n2. To exit\n')

        # Getting the choice from the user
        choice = input('Enter your choice: ')
        print(' ')

        # Using the is else for performing the prediction or exiting the cli application
        if choice in ['1', '2']:
            if choice == '1':
                time.sleep(3)
                prediction()
            else:
                print('Successfully exited the application.\n')
                break
        else:
            print('Enter the valid choice.')

    
# Run this function to run the application
application()
