#Import libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#Model loading
import joblib

model = joblib.load(r"./RANDOM_FOREST")

data = pd.read_csv('https://raw.githubusercontent.com/SravaniRVS/DATA-606/main/Telco-Customer-Churn.csv') 


def predict( gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges ):
    #Customer churn prediction

     if gender == 'Male':
          gender = 1
     elif gender == 'Female':
         gender = 0
        
     if SeniorCitizen == 'Yes':
        SeniorCitizen = 1
     elif SeniorCitizen == 'No':
        SeniorCitizen = 0

     if Partner == 'Yes':
        Partner = 1
     elif Partner == 'No':
        Partner = 0

     if Dependents == 'Yes':
        Dependents = 1
     elif Dependents == 'No':
        Dependents = 0

     if PhoneService == 'Yes':
        PhoneService = 1
     elif PhoneService == 'No':
        PhoneService = 0
        
     if MultipleLines == 'Yes':
        MultipleLines = 1
     elif MultipleLines == 'No':
        MultipleLines = 0
     elif MultipleLines == 'No phone service':
        MultipleLines = 2

     if InternetService == 'DSL':
        InternetService = 1
     elif InternetService == 'Fiber optic':
        InternetService = 0
     elif InternetService == 'No':
        InternetService = 2

     if OnlineSecurity == 'Yes':
        OnlineSecurity = 1
     elif OnlineSecurity == 'No':
        OnlineSecurity = 0

     if OnlineBackup == 'Yes':
        OnlineBackup = 1
     elif OnlineBackup == 'No':
        OnlineBackup = 0

     if DeviceProtection == 'Yes':
        DeviceProtection = 1
     elif DeviceProtection == 'No':
        DeviceProtection = 0

     if TechSupport == 'Yes':
        TechSupport = 1
     elif TechSupport == 'No':
        TechSupport = 0        
    
     if StreamingTV == 'Yes':
        StreamingTV = 1
     elif StreamingTV == 'No':
        StreamingTV = 0

     if StreamingMovies == 'Yes':
        StreamingMovies = 1
     elif StreamingMovies == 'No':
        StreamingMovies = 0

     if Contract == 'Month-to-Month':
        Contract = 0
     elif Contract == 'One year':
        Contract = 1
     elif Contract == 'Two Years':
        Contract = 2

     if PaperlessBilling == 'Yes':
        PaperlessBilling = 1
     elif PaperlessBilling == 'No':
        PaperlessBilling = 0

     if PaymentMethod == 'Bank transfer (automatic)':
        PaymentMethod = 1
     elif PaymentMethod == 'Electronic check':
        PaymentMethod = 2
     elif PaymentMethod == 'Mailed check':
        PaymentMethod = 0

     prediction = model.predict(pd.DataFrame([[gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges ]], columns=['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges']))
     return prediction                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       


header_image = Image.open("image.png")
st.image(header_image, width = 750)


title = '<p style="font-family: Copperplate; text-align: center; color:orange; font-size: 40px;">Telco Customer Churn Prediction Web Application</p>'
st.markdown(title, unsafe_allow_html=True)


sub_title = '<p style="font-family: sans-serif; font-size: 22px;">This app predicts the customer churn using the Random Forest Model. </p>'
st.markdown(sub_title, unsafe_allow_html=True)


st.markdown('Input data below:')


st.sidebar.image("image_1.jpeg")
st.sidebar.markdown("This project is completed by the group of: \n 1. Harshini Akkapally \n 2. Sravani Ravulaparthi \n 3. Akhila Amaranayani")


gender = st.selectbox('gender:', ['Male', 'Female'])
SeniorCitizen = st.selectbox('Senior Citizen:', ['Yes', 'No'])
Partner = st.selectbox('Partner:', ['Yes', 'No'])
Dependents = st.selectbox('Dependents:', ['Yes', 'No'])
tenure = st.number_input('tenure', min_value=1, value=1)
PhoneService = st.selectbox('Phone Service:', ['Yes', 'No'])
MultipleLines = st.selectbox('Multiple Lines:', ['Yes', 'No', 'No phone service'])
InternetService = st.selectbox('Internet Service:', ['DSL', 'Fiber optic', 'No'])
OnlineSecurity = st.selectbox('Online Security:', ['Yes', 'No'])
OnlineBackup = st.selectbox('Online Backup:', ['Yes', 'No'])
DeviceProtection = st.selectbox('Device Protection:', ['Yes', 'No'])
TechSupport = st.selectbox('Tech Support:', ['Yes', 'No'])
StreamingTV = st.selectbox('Streaming TV:', ['Yes', 'No'])
StreamingMovies = st.selectbox('Streaming Movies:', ['Yes', 'No'])
Contract = st.selectbox('Contract:', ['Month-to-Month', 'One year', 'Two Years'])
PaperlessBilling = st.selectbox('Paperless Billing:', ['Yes', 'No'])
PaymentMethod = st.selectbox('Payment Method:', ['Bank transfer (automatic)', 'Electronic check', 'Mailed check'])
MonthlyCharges = st.number_input('Monthly Charges:', min_value=1.0, value=1.0)
TotalCharges = st.number_input('Total Charges:', min_value=1.0, value=1.0)

if st.button('Predict'):
    pred = predict( gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges )
    if pred == 1:
        st.warning('Yes, the customer will terminate the service.')
    else:
        st.success('No, the customer is happy with the Services.')



st.markdown('----------------------------------------------------------------------')
st.write("This is the dataset that was used for this project.")
st.markdown('----------------------------------------------------------------------')

st.dataframe(data)

st.markdown('----------------------------------------------------------------------')
feed_options = ["Poor", "Good", "Awesome!", "Excellent", "Fantastic"]
default_value = 'Awesome!'
st.select_slider("What do think about this web page?", options = feed_options, value=default_value)

