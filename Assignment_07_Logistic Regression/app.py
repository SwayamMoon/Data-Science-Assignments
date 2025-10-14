import streamlit as st
st.title("Titanic Survival Prediction")
st.write("Test Message - App Working")
import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.title("Titanic Survival Prediction")

# User Inputs
def user_input_features():
    pclass = st.selectbox('Pclass', [1, 2, 3])
    sex = st.selectbox('Sex', ['male', 'female'])
    age = st.number_input('Age', 0.0, 100.0, 25.0)
    sibsp = st.number_input('SibSp', 0, 8, 0)
    parch = st.number_input('Parch', 0, 6, 0)
    fare = st.number_input('Fare', 0.0, 600.0, 32.0)
    embarked = st.selectbox('Embarked', ['C', 'Q', 'S'])
    # Encode categorical
    sex = 1 if sex == 'male' else 0
    embarked_dict = {'C':0, 'Q':1, 'S':2}
    embarked = embarked_dict[embarked]
    data = {
        'Pclass': pclass,
        'Sex': sex,
        'Age': age,
        'SibSp': sibsp,
        'Parch': parch,
        'Fare': fare,
        'Embarked': embarked
    }
    features = pd.DataFrame([data])
    return features

input_df = user_input_features()

# Model Loading
try:
    model = joblib.load('logistic_model.pkl')
    # Prediction
    if st.button('Predict'):
        prediction = model.predict(input_df)[0]
        output = 'Survived' if prediction == 1 else 'Did not survive'
        st.subheader(f'Result: {output}')
        prob = model.predict_proba(input_df)[0][1]
        st.write(f'Survival Probability: {prob:.2f}')
except Exception as e:
    st.error(f"Model loading error: {e}")
