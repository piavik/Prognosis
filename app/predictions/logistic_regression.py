import os
import streamlit as st
import joblib
import pandas as pd


current_dir = os.path.dirname(os.path.abspath(__file__))
def_model_path = os.path.join(current_dir, '..', '..', 'models', 'logistic_regression_model.pkl')
model_path = os.environ.get('DOCKER_MODEL_PATH', def_model_path)


@st.cache_resource
def load_model(file_path):
    return joblib.load(file_path)


model = load_model(model_path)
expected_feature_order = model.feature_names_in_


# Title and description
st.title("Logistic regression")