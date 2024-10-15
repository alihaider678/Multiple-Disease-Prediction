import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health AI Assistant", layout="wide", page_icon="🧑‍⚕️")

# Load the models
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# Sidebar for navigation with new labels
with st.sidebar:
    selected = option_menu(
        'Health AI Assistant: Predict Multiple Diseases',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        menu_icon='hospital',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Custom CSS for improving the UI
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #e6f7ff, #ffffff);
            font-family: 'Arial', sans-serif;
            color: #333;
        }
        .stApp {
            background: #ffffff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        .stButton > button {
            background-color: #004080;
            color: white;
            font-size: 1.2em;
            border-radius: 10px;
            padding: 10px 20px;
            transition: background-color 0.3s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #002d5e;
            transform: scale(1.05);
        }
        .stTextInput > div > div > input {
            background-color: #f0f8ff;
            padding: 12px;
            border-radius: 8px;
            font-size: 1.2em;
            border: 2px solid #ccc;
        }
        .stTextInput > div > div > input:focus {
            border-color: #004080;
            box-shadow: 0 0 8px rgba(0, 64, 128, 0.2);
        }
    </style>
    """, unsafe_allow_html=True)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction with AI')
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Pregnancies Count')

    with col2:
        Glucose = st.text_input('Blood Sugar Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure (mmHg)')

    with col1:
        SkinThickness = st.text_input('Skin Fold Thickness (mm)')

    with col2:
        Insulin = st.text_input('Insulin Level (mu U/ml)')

    with col3:
        BMI = st.text_input('Body Mass Index (BMI)')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Genetic Risk Factor')

    with col2:
        Age = st.text_input('Age')

    diab_diagnosis = ''
    if st.button('Get Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person has diabetes.'
        else:
            diab_diagnosis = 'The person does not have diabetes.'
    st.success(diab_diagnosis)

if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction with AI')
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain Types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Cholesterol Level')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by fluoroscopy')

    with col1:
        thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    heart_diagnosis = ''
    if st.button('Get Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has heart disease.'
        else:
            heart_diagnosis = 'The person does not have heart disease.'
    st.success(heart_diagnosis)

if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction with AI")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('Spread 1')

    with col5:
        spread2 = st.text_input('Spread 2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''
    if st.button("Get Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease."
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease."
    st.success(parkinsons_diagnosis)
