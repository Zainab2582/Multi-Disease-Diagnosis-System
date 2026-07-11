import sys
import streamlit as st

st.write(sys.version)
st.write(sys.executable)

import joblib

st.write("Joblib imported successfully")


import os
import joblib
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Health Assistant",
    layout="wide",
    page_icon="🧑‍⚕️"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.block-container {
    padding-top: 2rem;
}
.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-weight: 600;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: ;
    margin-bottom: 15px;
}
.title {
    font-size: 28px;
    font-weight: 700;
}
.subtitle {
    color: #8b949e;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- LOAD MODELS --------------------
script_directory = os.path.dirname(os.path.abspath(__file__))

artifact_2 = joblib.load(os.path.join(script_directory, 'heart_disease.joblib'))
artifact_3 = joblib.load(os.path.join(script_directory, 'liver_disease.joblib'))
artifact_4 = joblib.load(os.path.join(script_directory, 'kidney_disease.joblib'))

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.markdown("## 🧑‍⚕️ Health Assistant")
    #st.caption("ML-powered disease prediction")
    st.caption("Assess risk for heart, liver, and kidney diseases using patient details.")

    selected = option_menu(
        menu_title=None,
        options=[
            "Heart Disease",
            "Liver Disease",
            "Kidney Disease"
        ],
        icons=["heart", "activity", "droplet"],
        default_index=0
    )

# -------------------- COMMON FUNCTIONS --------------------
def check_missing_inputs(data):
    return any(value == '' for value in data.values())

def show_result(result):
    st.markdown(f"""
    <div class="card">
        <h3>🧾 Result</h3>
        <p>{result}</p>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# HEART DISEASE
# =========================================================
if selected == "Heart Disease":

    st.markdown('<div class="title">Heart Disease Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Enter patient details below</div>', unsafe_allow_html=True)

    with st.container():
        col1, col2, col3 = st.columns(3)

        age = col1.number_input('Age')
        sex = col2.selectbox("Sex", ['', 'Male', 'Female'])
        cp = col3.selectbox("Chest Pain", ['', 'Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic'])

        trestbps = col1.number_input('Blood Pressure')
        chol = col2.number_input('Cholesterol')
        fbs = col3.selectbox("FBS > 120", ['', 'True', 'False'])

        restecg = col1.selectbox("ECG Result", ['', 'Normal',
        'Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)',
        'showing probable or definite left ventricular hypertrophy by Estes criteria'])

        thalach = col2.number_input('Max Heart Rate')
        exang = col3.selectbox('Exercise Angina', ['', 'Yes', 'No'])

        oldpeak = col1.number_input('ST Depression')
        slope = col2.selectbox('Slope', ['', 'Upsloping', 'Flat', 'Downsloping'])
        ca = col3.selectbox('Vessels', ['', 0,1,2,3,4])

        thal = col1.selectbox('Thal', ['', 'Fixed defect', 'Normal', 'Reversable defect'])

    # MAPPINGS (UNCHANGED)
    sex_mapping = {'Male':1,'Female':0}
    fbs_mapping = {'True':1,'False':0}
    restecg_mapping = {
        'Normal':0,
        'Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)':1,
        'showing probable or definite left ventricular hypertrophy by Estes criteria':2
    }
    exang_mapping = {'Yes':1,'No':0}
    slope_mapping = {'Upsloping':0,'Flat':1,'Downsloping':2}
    thal_mapping = {'Normal':2,'Fixed defect':1,'Reversable defect':3}
    cp_mapping = {'Typical angina':0,'Atypical angina':1,'Non-anginal pain':2,'Asymptomatic':3}

    user_input = {
        'age': age,
        'sex': sex_mapping.get(sex, ''),
        'cp': cp_mapping.get(cp, ''),
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs_mapping.get(fbs, ''),
        'restecg': restecg_mapping.get(restecg, ''),
        'thalach': thalach,
        'exang': exang_mapping.get(exang, ''),
        'oldpeak': oldpeak,
        'slope': slope_mapping.get(slope, ''),
        'ca': ca,
        'thal': thal_mapping.get(thal, '')
    }

    def make_prediction(data):
        df = pd.DataFrame([data])
        X = pd.DataFrame(
            artifact_2['preprocessing'].transform(df),
            columns=artifact_2['preprocessing'].get_feature_names_out()
        )
        prediction = artifact_2['model'].predict(X)[0]
        return 'Heart Disease Detected' if prediction == 1 else 'No Heart Disease'

    if st.button("Run Prediction"):
        if check_missing_inputs(user_input):
            st.error("Please complete all fields")
        else:
            show_result(make_prediction(user_input))


# =========================================================
# LIVER
# =========================================================
elif selected == "Liver Disease":

    st.markdown('<div class="title">Liver Disease Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Enter patient details below</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    age = col1.number_input('Age')
    gender = col2.selectbox("Gender", ['','Male','Female'])
    total_bilirubin = col3.number_input('Total Bilirubin')

    direct_bilirubin = col1.number_input('Direct Bilirubin')
    alkaline_phosphotase = col2.number_input('Alkaline Phosphotase')
    alamine_aminotransferase = col3.number_input('Alamine Aminotransferase')

    aspartate_aminotransferase = col1.number_input('Aspartate Aminotransferase')
    total_protiens = col2.number_input('Total Proteins')
    albumin = col3.number_input('Albumin')

    albumin_and_globulin_ratio = col1.number_input('A/G Ratio')

    gender_mapping = {'Male':1,'Female':0}

    user_input = {
        'Age': age,
        'Gender': gender_mapping.get(gender, ''),
        'Total_Bilirubin': total_bilirubin,
        'Direct_Bilirubin': direct_bilirubin,
        'Alkaline_Phosphotase': alkaline_phosphotase,
        'Alamine_Aminotransferase': alamine_aminotransferase,
        'Aspartate_Aminotransferase': aspartate_aminotransferase,
        'Total_Protiens': total_protiens,
        'Albumin': albumin,
        'Albumin_and_Globulin_Ratio': albumin_and_globulin_ratio
    }

    def make_prediction(data):
        df = pd.DataFrame([data])
        X = pd.DataFrame(
            artifact_3['preprocessing'].transform(df),
            columns=artifact_3['preprocessing'].get_feature_names_out()
        )
        prediction = artifact_3['model'].predict(X)[0]
        return 'Liver Disease Detected' if prediction == 1 else 'No Liver Disease'

    if st.button("Run Prediction"):
        if check_missing_inputs(user_input):
            st.error("Please complete all fields")
        else:
            show_result(make_prediction(user_input))


# =========================================================
# KIDNEY
# =========================================================
elif selected == "Kidney Disease":

    st.markdown('<div class="title">Kidney Disease Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Enter patient details below</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    age = col1.number_input('Age')
    blood_pressure = col2.number_input('Blood Pressure')
    specific_gravity = col3.number_input('Specific Gravity')

    albumin = col1.number_input('Albumin')
    sugar = col2.number_input('Sugar')
    red_blood_cells = col3.selectbox("RBC", ['','Normal','Abnormal'])

    pus_cell = col1.selectbox("Pus Cell", ['','Normal','Abnormal'])
    pus_cell_clumps = col2.selectbox("Pus Clumps", ['','Present','Not present'])
    bacteria = col3.selectbox("Bacteria", ['','Present','Not present'])

    blood_glucose_random = col1.number_input('Glucose')
    blood_urea = col2.number_input('Urea')
    serum_creatinine = col3.number_input('Creatinine')

    sodium = col1.number_input('Sodium')
    potassium = col2.number_input('Potassium')
    haemoglobin = col3.number_input('Hemoglobin')

    packed_cell_volume = col1.number_input('PCV')
    white_blood_cell_count = col2.number_input('WBC Count')
    red_blood_cell_count = col3.number_input('RBC Count')

    hypertension = col1.selectbox("Hypertension", ['','Yes','No'])
    diabetes_mellitus = col2.selectbox("Diabetes", ['','Yes','No'])
    coronary_artery_disease = col3.selectbox("CAD", ['','Yes','No'])

    appetite = col1.selectbox("Appetite", ['','Good','Poor'])
    peda_edema = col2.selectbox("Edema", ['','Yes','No'])
    aanemia = col3.selectbox("Anemia", ['','Yes','No'])

    # mappings unchanged...
    red_blood_cells_mapping = {'Normal':1,'Abnormal':0}
    pus_cell_mapping = {'Normal':1,'Abnormal':0}
    pus_cell_clumps_mapping = {'Present':1,'Not present':0}
    bacteria_mapping = {'Present':1,'Not present':0}
    hypertension_mapping = {'Yes':1,'No':0}
    diabetes_mellitus_mapping = {'Yes':1,'No':0}
    coronary_artery_disease_mapping = {'Yes':1,'No':0}
    appetite_mapping = {'Good':1,'Poor':0}
    peda_edema_mapping = {'Yes':1,'No':0}
    aanemia_mapping = {'Yes':1,'No':0}

    user_input = {
        'age': age,
        'blood_pressure': blood_pressure,
        'specific_gravity': specific_gravity,
        'albumin': albumin,
        'sugar': sugar,
        'blood_glucose_random': blood_glucose_random,
        'blood_urea': blood_urea,
        'serum_creatinine': serum_creatinine,
        'sodium': sodium,
        'potassium': potassium,
        'haemoglobin': haemoglobin,
        'packed_cell_volume': packed_cell_volume,
        'white_blood_cell_count': white_blood_cell_count,
        'red_blood_cell_count': red_blood_cell_count,
        'red_blood_cells': red_blood_cells_mapping.get(red_blood_cells, ''),
        'pus_cell': pus_cell_mapping.get(pus_cell, ''),
        'pus_cell_clumps': pus_cell_clumps_mapping.get(pus_cell_clumps, ''),
        'bacteria': bacteria_mapping.get(bacteria, ''),
        'hypertension': hypertension_mapping.get(hypertension, ''),
        'diabetes_mellitus': diabetes_mellitus_mapping.get(diabetes_mellitus, ''),
        'coronary_artery_disease': coronary_artery_disease_mapping.get(coronary_artery_disease, ''),
        'appetite': appetite_mapping.get(appetite, ''),
        'peda_edema': peda_edema_mapping.get(peda_edema, ''),
        'aanemia': aanemia_mapping.get(aanemia, '')
    }

    def make_prediction(data):
        df = pd.DataFrame([data])
        X = pd.DataFrame(
            artifact_4['preprocessing'].transform(df),
            columns=artifact_4['preprocessing'].get_feature_names_out()
        )
        prediction = artifact_4['model'].predict(X)[0]
        return 'Kidney Disease Detected' if prediction == 1 else 'No Kidney Disease'

    if st.button("Run Prediction"):
        if check_missing_inputs(user_input):
            st.error("Please complete all fields")
        else:
            show_result(make_prediction(user_input))
