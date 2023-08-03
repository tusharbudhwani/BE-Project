# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 08:31:21 2022

@author: dell
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open(
    'C:/Users/Tusha/OneDrive/Desktop/BE-Project/Saved models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(
    'C:/Users/Tusha/OneDrive/Desktop/BE-Project/Saved models/heart_disease_model.sav', 'rb'))

BC1 = pickle.load(open(
    'C:/Users/Tusha/OneDrive/Desktop/BE-Project/Saved models/BC1.sav', 'rb'))

parkinsons_model = pickle.load(open(
    'C:/Users/Tusha/OneDrive/Desktop/BE-Project/Saved models/parkinsons_model.sav', 'rb'))

ckd_model = pickle.load(open(
    'C:/Users/Tusha/OneDrive/Desktop/BE-Project/Saved models/ckd_model.sav', 'rb'))

liver_model = pickle.load(open(
    'C:/Users/Tusha/OneDrive/Desktop/BE-Project/Saved models/liver_model.sav', 'rb'))

symptoms_to_disease_model = pickle.load(open(
    'C:/Users/Tusha/OneDrive/Desktop/BE-Project/Saved models/symptoms_to_disease_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:

    selected = option_menu('Predictal',

                           ['Home Page',
                            'Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Breast Cancer Disease Prediction',
                            'Parkinsons Disease Prediction',
                            'Kidney Disease Prediction',
                            'Liver Disease Prediction',
                            'Predict Disease Through Symptoms'],
                           icons=['activity', 'heart', 'person',
                                  'bandaid', 'activity', 'bandaid', 'activity'],
                           default_index=0)


# Home Page
if (selected == 'Home Page'):

    # page title
    st.title('Welcome to Predictal')
    st.divider()
    st.text("Are you looking for a way to manage your health and assess your likelihood \nfor certain deadly diseases without seeing a doctor? \n\nIf so, you're in luck! That's what our app Predictal can do. \n'Predictal' analyses your symptoms and medical characteristics using cutting-edge \nalgorithms to determine various diseases you are most likely to contract. \n\nIts a practical and trustworthy approach to keep tabs on \nyour health and take preventative measures against diseases.")
    # st.text("[Diabetes Prediction]('#welcome-to-predictal')")
    # st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")
    # st.markdown('<a href="Diabetes-Prediction" target="_self">Next page</a>', unsafe_allow_html=True)
    st.markdown('<hr><h3>Nagivate through the sidebar to access various Disease Prediction Models</h3>', unsafe_allow_html=True)
    












# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction')
    st.divider()
    st.markdown('<p>According to <b><i>World Health Organization</i></b> - <br>"<i>Diabetes is a chronic disease that occurs either when the pancreas does not produce enough insulin or when the body cannot effectively use the \ninsulin it produces. Insulin is a hormone that regulates blood glucose.</i>"</p> <hr>', unsafe_allow_html=True)
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input(
            'Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            st.error('The person has a higher risk of diabetes')
        else:
            st.success('The person has a lower risk of diabetes')


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction')
    st.divider()
    st.markdown('<p>According to <b><i>MedlinePlus</i></b> - <br>"<i>Heart disease is a general term that includes many types of heart problems. Its also called cardiovascular disease, which means heart and blood vessel disease.</i>" <br> Following are the major types of Heart Diseases. <br> <ul><li>Angina - chest pain from lack of blood flow</li><li>Heart attacks - when part of the heart muscle dies from loss of blood flow</li><li>Heart failure - when your heart can not pump enough blood to meet the needs of your body</li><li>Arrhythmia - a problem with the rate or rhythm of your heartbeat</li></ul></p> <hr>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

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
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input(
            'thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[int(age), int(sex), int(cp), int(trestbps), int(
            chol), int(fbs), int(restecg), int(thalach), int(exang), float(oldpeak), int(slope), int(ca), int(thal)]])

        if (heart_prediction[0] == 1):
            st.error('The person has a higher risk heart disease')
        else:
            st.success('The person has a lower risk of heart disease')
            


# Cancer Disease Prediction Page
if (selected == 'Breast Cancer Disease Prediction'):

    # page title
    st.title('Breast Cancer Disease Prediction')
    st.divider()
    st.markdown('<p>According to <b><i>Centers for Disease Control and Prevention</i></b> - <br>"<i>Breast cancer is a disease in which cells in the breast grow out of control. There are different kinds of breast cancer. The kind of breast cancer depends on which cells in the breast turn into cancer. Breast cancer can begin in different parts of the breast."</i> <br> Kinds of Breast Cancer - <br></p> <ul><li><b>Invasive ductal carcinoma -</b> The cancer cells begin in the ducts and then grow outside the ducts into other parts of the breast tissue. Invasive cancer cells can also spread, or metastasize, to other parts of the body.</li><li><b>Invasive lobular carcinoma -</b> Cancer cells begin in the lobules and then spread from the lobules to the breast tissues that are close by. These invasive cancer cells can also spread to other parts of the body.</li></ul><hr>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        radius_mean = st.text_input('Mean Radius')

    with col2:
        texture_mean = st.text_input('Mean Texture')

    with col3:
        perimeter_mean = st.text_input('Mean Perimeter')

    with col1:
        area_mean = st.text_input('Mean Area')

    with col2:
        smoothness_mean = st.text_input('Mean Smoothness')

    with col3:
        compactness_mean = st.text_input('Mean Compactness')

    with col1:
        concavity_mean = st.text_input('Mean Concavity')

    with col2:
        symmetry_mean = st.text_input('Mean Symmetry ')

    with col3:
        fractal_dimension_mean = st.text_input('Mean Fractal Dim')

    with col1:
        radius_se = st.text_input('Radius Error')

    with col2:
        texture_se = st.text_input('Texture Error')

    with col3:
        perimeter_se = st.text_input('Perimeter Error')

    with col1:
        area_se = st.text_input('Area Error')

    with col2:
        smoothness_se = st.text_input('Smoothness Error')

    with col3:
        compactness_se = st.text_input('Compactness Error')

    with col1:
        concavity_se = st.text_input('Concavity Error')

    with col2:
        symmetry_se = st.text_input('Symmetry Error')

    with col3:
        fractal_dimension_se = st.text_input('Fractal Dim Error')

    with col1:
        radius_worst = st.text_input('Worst Radius')

    with col2:
        texture_worst = st.text_input('Worst Texture')

    with col3:
        perimeter_worst = st.text_input('Worst Perimeter')

    with col1:
        area_worst = st.text_input('Worst Area')

    with col2:
        smoothness_worst = st.text_input('Worst Smoothness')

    with col3:
        compactness_worst = st.text_input('Worst Compactness')

    with col1:
        concavity_worst = st.text_input('Worst Concavity')

    with col2:
        symmetry_worst = st.text_input('Worst Symmetry')

    with col3:
        fractal_dimension_worst = st.text_input('Worst Fractal Dim')

    # code for Prediction
    cancer_diagnosis = ''

    # creating a button for Prediction

    if st.button('Breast Cancer Disease Test Result'):
        cancer_prediction = BC1.predict([[float(radius_mean), float(texture_mean), float(perimeter_mean), float(area_mean), float(smoothness_mean), float(compactness_mean), float(concavity_mean), float(symmetry_mean), float(fractal_dimension_mean), float(radius_se), float(texture_se), float(perimeter_se), float(area_se), float(
            smoothness_se), float(compactness_se), float(concavity_se), float(symmetry_se), float(fractal_dimension_se), float(radius_worst), float(texture_worst), float(perimeter_worst), float(area_worst), float(smoothness_worst), float(compactness_worst), float(concavity_worst), float(symmetry_worst), float(fractal_dimension_worst)]])

        if (cancer_prediction[0] == 1):
            st.error('High Possibilty of Malignancy')
        else:
            st.success('Benign')


# Parkinson's Prediction Page
if (selected == "Parkinsons Disease Prediction"):

    # page title
    st.title("Parkinsons Disease Prediction")
    st.divider()
    st.markdown('<p>According to <b><i>National Institute on Aging</i></b> - <br>"<i>Parkinson’s disease is a brain disorder that causes unintended or uncontrollable movements, such as shaking, stiffness, and difficulty with balance and coordination. Symptoms usually begin gradually and worsen over time. As the disease progresses, people may have difficulty walking and talking. They may also have mental and behavioral changes, sleep problems, depression, memory difficulties, and fatigue.</i>"</p> <hr>', unsafe_allow_html=True)
    

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
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict(
            [[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            st.error('The person has a higher risk of Parkinsons disease')
        else:
            st.success('The person has a lower risk of Parkinsons disease')



# Kidney Disease Prediction Page
if (selected == "Kidney Disease Prediction"):

    # page title
    st.title("Kidney Disease Prediction")
    st.divider()
    st.markdown('<p>According to <b><i>Mayo Clinic</i></b> - <br>"<i>Chronic kidney disease, also called chronic kidney failure, involves a gradual loss of kidney function. Your kidneys filter wastes and excess fluids from your blood, which are then removed in your urine. Advanced chronic kidney disease can cause dangerous levels of fluid, electrolytes and wastes to build up in your body.</i>"</p> <hr>', unsafe_allow_html=True)
    

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        age = st.text_input('Age')

    with col2:
        blood_pressure = st.text_input('Blood Pressure')

    with col3:
        specific_gravity = st.text_input('Specific Gravity')

    with col4:
        albumin = st.text_input('Albumin')

    with col5:
        sugar = st.text_input('Sugar')

    with col1:
        red_blood_cells = st.text_input('RBC')

    with col2:
        pus_cell = st.text_input('Pus Cells')

    with col3:
        pus_cell_clumps = st.text_input('Pus Cell Clumps')

    with col4:
        bacteria = st.text_input('Bacteria')

    with col5:
        blood_glucose_random = st.text_input('Random Sugar')

    with col1:
        blood_urea = st.text_input('Blood Urea')

    with col2:
        serum_creatinine = st.text_input('Creatinine')

    with col3:
        sodium = st.text_input('Sodium')

    with col4:
        potassium = st.text_input('Potassium')

    with col5:
        haemoglobin = st.text_input('Haemoglobin')

    with col1:
        packed_cell_volume = st.text_input('Packed Cell Volume')

    with col2:
        white_blood_cell_count = st.text_input('WBC Count')

    with col3:
        red_blood_cell_count = st.text_input('RBC Count')

    with col4:
        hypertension = st.text_input('Hypertension')

    with col5:
        diabetes_mellitus = st.text_input('Diabetes')

    with col1:
        coronary_artery_disease = st.text_input('Coronary Artery Disease')

    with col2:
        appetite = st.text_input('Appetite')

    with col3:
        peda_edema = st.text_input('Edema')

    with col4:
        aanemia = st.text_input('Anaemia')

    # code for Prediction
    ckd_diagnosis = ''

    # creating a button for Prediction
    if st.button("Kidney Disease Test Result"):
        ckd_prediction = ckd_model.predict([[age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell, pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, serum_creatinine,
                                           sodium, potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus, coronary_artery_disease, appetite, peda_edema, aanemia]])

        if (ckd_prediction[0] == 1):
            st.error('The person has a higher risk of Chronic Kidney disease')
        else:
            st.success('The person has a lower risk of Chronic Kidney disease')


# Liver Disease Prediction Page
if (selected == 'Liver Disease Prediction'):

    # page title
    st.title('Liver Disease Prediction')
    st.divider()
    st.markdown('<p>According to <b><i>Cleveland Clinic</i></b> - <br>"<i>There are many types of liver disease, which can be caused by infections, inherited conditions, obesity and misuse of alcohol. Over time, liver disease may lead to scarring and more serious complications. <br><br>Some types of liver disease can increase your risk of developing liver cancer. Others, if left untreated, continue to damage your liver. Cirrhosis (scarring) develops. Over time, a damaged liver won’t have enough healthy tissue to function. Liver disease that isn’t treated can eventually lead to liver failure.</i>"</p> <hr>', unsafe_allow_html=True)
    

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        gender = st.text_input('Gender')

    with col3:
        Total_Bilirubin = st.text_input('Total Bilirubin')

    with col1:
        Direct_Bilirubin = st.text_input('Direct Bilirubin')

    with col2:
        Alkaline_Phosphotase = st.text_input('Alkaline Phosphotase')

    with col3:
        Alamine_Aminotransferase = st.text_input('Alamine Aminotransferase')

    with col1:
        Aspartate_Aminotransferase = st.text_input(
            'Aspartate Aminotransferase')

    with col2:
        Total_Protiens = st.text_input('Total Protiens')

    with col3:
        Albumin = st.text_input('Albumin')

    with col1:
        Albumin_and_Globulin_Ratio = st.text_input(
            'Albumin and Globulin Ratio')

    # code for Prediction
    liver_diagnosis = ''

    # creating a button for Prediction

    if st.button('Liver Disease Test Result'):
        liver_prediction = liver_model.predict([[age, gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase,
                                               Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])

        if (liver_prediction[0] == 1):
            st.error('The person has a higher risk of liver disease')
        else:
            st.success('The person has a lower risk of liver disease')



# Predict Disease Through Symptoms

if(selected == 'Predict Disease Through Symptoms'):

    # page title
    st.title('Predict Disease Through Symptoms')
    st.divider()
    st.text('This section helps you predict a potential disease you may be having \nbased on the symptoms you are experiencing.')
    st.divider()
    st.text('Please select any symptoms that you are experiencing from the following list.')

    symptoms_list = ['itching',
                     'skin_rash',
                     'nodal_skin_eruptions',
                     'continuous_sneezing',
                     'shivering',
                     'chills',
                     'joint_pain',
                     'stomach_pain',
                     'acidity',
                     'ulcers_on_tongue',
                     'muscle_wasting',
                     'vomiting',
                     'burning_micturition',
                     'spotting_ urination',
                     'fatigue',
                     'weight_gain',
                     'anxiety',
                     'cold_hands_and_feets',
                     'mood_swings',
                     'weight_loss',
                     'restlessness',
                     'lethargy',
                     'patches_in_throat',
                     'irregular_sugar_level',
                     'cough',
                     'high_fever',
                     'sunken_eyes',
                     'breathlessness',
                     'sweating',
                     'dehydration',
                     'indigestion',
                     'headache',
                     'yellowish_skin',
                     'dark_urine',
                     'nausea',
                     'loss_of_appetite',
                     'pain_behind_the_eyes',
                     'back_pain',
                     'constipation',
                     'abdominal_pain',
                     'diarrhoea',
                     'mild_fever',
                     'yellow_urine',
                     'yellowing_of_eyes',
                     'acute_liver_failure',
                     'fluid_overload',
                     'swelling_of_stomach',
                     'swelled_lymph_nodes',
                     'malaise',
                     'blurred_and_distorted_vision',
                     'phlegm',
                     'throat_irritation',
                     'redness_of_eyes',
                     'sinus_pressure',
                     'runny_nose',
                     'congestion',
                     'chest_pain',
                     'weakness_in_limbs',
                     'fast_heart_rate',
                     'pain_during_bowel_movements',
                     'pain_in_anal_region',
                     'bloody_stool',
                     'irritation_in_anus',
                     'neck_pain',
                     'dizziness',
                     'cramps',
                     'bruising',
                     'obesity',
                     'swollen_legs',
                     'swollen_blood_vessels',
                     'puffy_face_and_eyes',
                     'enlarged_thyroid',
                     'brittle_nails',
                     'swollen_extremeties',
                     'excessive_hunger',
                     'extra_marital_contacts',
                     'drying_and_tingling_lips',
                     'slurred_speech',
                     'knee_pain',
                     'hip_joint_pain',
                     'muscle_weakness',
                     'stiff_neck',
                     'swelling_joints',
                     'movement_stiffness',
                     'spinning_movements',
                     'loss_of_balance',
                     'unsteadiness',
                     'weakness_of_one_body_side',
                     'loss_of_smell',
                     'bladder_discomfort',
                     'foul_smell_of urine',
                     'continuous_feel_of_urine',
                     'passage_of_gases',
                     'internal_itching',
                     'toxic_look_(typhos)',
                     'depression',
                     'irritability',
                     'muscle_pain',
                     'altered_sensorium',
                     'red_spots_over_body',
                     'belly_pain',
                     'abnormal_menstruation',
                     'dischromic _patches',
                     'watering_from_eyes',
                     'increased_appetite',
                     'polyuria',
                     'family_history',
                     'mucoid_sputum',
                     'rusty_sputum',
                     'lack_of_concentration',
                     'visual_disturbances',
                     'receiving_blood_transfusion',
                     'receiving_unsterile_injections',
                     'coma',
                     'stomach_bleeding',
                     'distention_of_abdomen',
                     'history_of_alcohol_consumption',
                     'fluid_overload.1',
                     'blood_in_sputum',
                     'prominent_veins_on_calf',
                     'palpitations',
                     'painful_walking',
                     'pus_filled_pimples',
                     'blackheads',
                     'scurring',
                     'skin_peeling',
                     'silver_like_dusting',
                     'small_dents_in_nails',
                     'inflammatory_nails',
                     'blister',
                     'red_sore_around_nose',
                     'yellow_crust_ooze']

    symptoms = st.multiselect("Choose Symptoms - ", symptoms_list)
    
    # Code for prediction
    disease_diagnosis = ""
    
    flag = 0 
    
    if st.button('Predict Disease'):
        
        if len(symptoms) < 3:
            flag = 1
            disease_diagnosis = "Please add more symptoms for accurate prediction."
        else:
            flag = 0
        
            selected_symptoms = [0] * len(symptoms_list)
            
            for i in range(len(symptoms_list)):
                if symptoms_list[i] in symptoms:
                    selected_symptoms[i] = 1 
                else:
                    selected_symptoms[i] = 0
        
            disease_diagnosis = "".join(symptoms_to_disease_model.predict([selected_symptoms]))
            
            
        
    if flag == 0:
        st.error(disease_diagnosis)
    else:
        st.warning(disease_diagnosis)