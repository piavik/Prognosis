import streamlit as st
import os
import joblib


current_dir = os.path.dirname(os.path.abspath(__file__))
def_model_path = os.path.join(current_dir, '..', '..', 'models')
model_path = os.environ.get('DOCKER_MODEL_PATH', def_model_path)


@st.cache_resource
def load_model(file_path):
    return joblib.load(os.path.join(model_path, file_path))
