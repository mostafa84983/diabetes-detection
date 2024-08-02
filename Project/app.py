import pandas as pd
import numpy as np
import pickle
import streamlit as st

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


def welcome():
    return 'welcome all'


def prediction(cholesterol, glucose, hdl_chol, chol_hdl_ratio, age, gender, height, weight, bmi, systolic_bp, diastolic_bp, waist, hip, waist_hip_ratio):

    prediction = classifier.predict(
        [[cholesterol, glucose, hdl_chol, chol_hdl_ratio, age, gender, height, weight, bmi, systolic_bp, diastolic_bp, waist, hip, waist_hip_ratio]])
    print(prediction)
    return prediction


def main():
    st.title("ML Model using KNN")
    html_temp = """
	<div style ="background-color:#E8F1F5;padding:13px">
	<h1 style ="color:black;text-align:center;">Diabetes Prediction App </h1>
	</div>
	"""
    st.markdown(html_temp, unsafe_allow_html=True)

    gender = st.selectbox("gender ", ['Male', 'Female'])
    if gender == "Male":
        gender = 1
    else:
        gender = 0
    age = st.number_input("age ", min_value=0)
    height = st.number_input("height in inches", min_value=0)
    weight = st.number_input("weight in lbs ", min_value=0)
    bmi = st.number_input("bmi", min_value=0.0)
    waist = st.number_input("waist in inches", min_value=0)
    hip = st.number_input("hip in inches", min_value=1)
    waist_hip_ratio = float(waist)/hip
    cholesterol = st.number_input("cholesterol level", min_value=0)
    glucose = st.number_input("glucose level", min_value=0)
    hdl_chol = st.number_input("hdl cholesterol ", min_value=1)
    chol_hdl_ratio = float(cholesterol) / hdl_chol
    systolic_bp = st.number_input("systolic blood pressure", min_value=0)
    diastolic_bp = st.number_input("diastolic blood pressure", min_value=0)
    result = ""

    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result

    if st.button("Predict"):
        result = prediction(cholesterol, glucose, hdl_chol, chol_hdl_ratio, age, gender,
                            height, weight, bmi, systolic_bp, diastolic_bp, waist, hip, waist_hip_ratio)

        if result == 0:
            result = "Diabetes"
        elif result == 1:
            result = "No Diabetes"

        st.success('{}'.format(result))


if __name__ == '__main__':
    main()
