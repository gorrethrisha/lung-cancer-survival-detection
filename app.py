import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("lung_cancer_survival_model.pkl")

# Title
st.title("🫁 Lung Cancer Survival Prediction")
st.write("Enter the patient information below to predict survival outcome.")

# Numerical Inputs
age = st.number_input("Age", min_value=1, max_value=120, value=50)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
cholesterol_level = st.number_input("Cholesterol Level",min_value=50,max_value=500,value=200)

# Categorical Inputs
gender = st.selectbox("Gender", ["Female", "Male"])

country = st.selectbox(
    "Country",
    [
        "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus",
        "Czech Republic", "Denmark", "Estonia", "Finland", "France",
        "Germany", "Greece", "Hungary", "Ireland", "Italy",
        "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands",
        "Poland", "Portugal", "Romania", "Slovakia", "Slovenia",
        "Spain", "Sweden"
    ]
)

cancer_stage = st.selectbox("Cancer Stage",["Stage I", "Stage II", "Stage III", "Stage IV"])

family_history = st.selectbox("Family History",["No", "Yes"])

smoking_status = st.selectbox("Smoking Status",["Current Smoker","Former Smoker","Never Smoked","Passive Smoker"])

hypertension = st.selectbox("Hypertension",[0, 1])

asthma = st.selectbox("Asthma",[0, 1])

cirrhosis = st.selectbox("Cirrhosis",[0, 1])

other_cancer = st.selectbox("Other Cancer",[0, 1])

treatment_type = st.selectbox("Treatment Type",["Chemotherapy","Combined","Radiation","Surgery"])

# Encoding dictionaries
gender_map = {"Female": 0,"Male": 1}

country_map = {"Austria": 0,"Belgium": 1,"Bulgaria": 2,"Croatia": 3,"Cyprus": 4,"Czech Republic": 5,"Denmark": 6,"Estonia": 7,
               "Finland": 8,"France": 9,"Germany": 10,"Greece": 11,"Hungary": 12,"Ireland": 13,"Italy": 14,"Latvia": 15,
               "Lithuania": 16,"Luxembourg": 17,"Malta": 18,"Netherlands": 19,"Poland": 20,"Portugal": 21,"Romania": 22,
               "Slovakia": 23,"Slovenia": 24,"Spain": 25,"Sweden": 26}

cancer_stage_map = {"Stage I": 0,"Stage II": 1,"Stage III": 2,"Stage IV": 3}

family_history_map = {"No": 0,"Yes": 1}

smoking_status_map = {"Current Smoker": 0,"Former Smoker": 1,"Never Smoked": 2,"Passive Smoker": 3}

treatment_type_map = {"Chemotherapy": 0,"Combined": 1,"Radiation": 2,"Surgery": 3}

# Prediction
if st.button("Predict Survival"):

    input_data = pd.DataFrame({
        "age": [age],
        "gender": [gender_map[gender]],
        "country": [country_map[country]],
        "cancer_stage": [cancer_stage_map[cancer_stage]],
        "family_history": [family_history_map[family_history]],
        "smoking_status": [smoking_status_map[smoking_status]],
        "bmi": [bmi],
        "cholesterol_level": [cholesterol_level],
        "hypertension": [hypertension],
        "asthma": [asthma],
        "cirrhosis": [cirrhosis],
        "other_cancer": [other_cancer],
        "treatment_type": [treatment_type_map[treatment_type]]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Prediction: The patient is likely to survive.")
    else:
        st.error("⚠️ Prediction: The patient is unlikely to survive.")