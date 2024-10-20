import streamlit as st
import os
import joblib


current_dir = os.path.dirname(os.path.abspath(__file__))
def_model_path = os.path.join(current_dir, '..', '..', 'models')
model_path = os.environ.get('DOCKER_MODEL_PATH', def_model_path)


@st.cache_resource
def load_model(file_path):
    return joblib.load(os.path.join(model_path, file_path))


def predict(model, user_input):
    # Make prediction
    prediction = model.predict(user_input)
    # If your model predicts probabilities, you can also display them
    prediction_proba = model.predict_proba(user_input)

    # Map prediction to class names if necessary
    class_names = ['Not Churn', 'Churn']  # Replace with your class names

    st.subheader('Prediction:')
    st.write(f"Predicted Class: {class_names[int(prediction[0])]}")

    st.subheader('Prediction Probability:')
    st.write(f"Probability: {prediction_proba[0][int(prediction[0])]*100:.2f}%")
