import streamlit as st

from services.load_models import load_model, predict
from services.parse_inputs import get_user_input


model = load_model('mlp_model.pkl')
expected_feature_order = model.feature_names_in_


# Title and description
st.title("Multilayer Perceptron (MLP)")
st.write("""
This app uses a trained Neural Network model to make predictions.
""")


# Get user input
user_input = get_user_input()

# Reorder the columns of user_input to match the model's expected order
user_input = user_input[expected_feature_order]

# Make prediction
if st.button('Predict Churn'):
    predict(model, user_input)