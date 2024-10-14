import streamlit as st
import pandas as pd

from services.load_models import load_model


model = load_model('logistic_regression_model.pkl')
expected_feature_order = model.feature_names_in_


# Title and description
st.title("Logistic regression")