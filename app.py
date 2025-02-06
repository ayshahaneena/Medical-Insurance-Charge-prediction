import streamlit as st
import pickle
import pandas as pd
import numpy as np

with open ('insurance_model.pkl', 'rb') as file :
    model = pickle.load(file)

st.title('Medical Insurance Prediction App')
st.write('Enter the details below to predict insurance charges')

age = st.number_input("Age",min_value=18, max_value=100,value=30)
bmi = st.number_input("BMI",min_value=10.0,max_value=100.0,value=25.0)
children = st.number_input("Childern",min_value=0,max_value=10,value=1)
sex = st.selectbox("Sex",['Male','Female'])
smoker = st.selectbox("Smoker",['Yes','No'])
region = st.selectbox("Region",['northeast','northwest','southeast','southwest'])
input_data = pd.DataFrame([[age,bmi,children,sex,smoker,region]],
                          columns=['age','bmi','children','sex','smoker','region'])


if st.button('Predict'):
    prediction = model.predict(input_data)[0]
    st.write(f"Predicted Insurance Charges: {prediction:.2f}")