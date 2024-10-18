import streamlit as st

from services.load_models import load_model, predict
from services.parse_inputs import get_user_input


model = load_model('random_forest_model.pkl')
expected_feature_order = model.feature_names_in_


# Title and description
st.title("Random Forest Classifier")
st.write("""
This app uses a trained Random Forest model to make predictions.
""")

# Get user input
user_input = get_user_input()

# Reorder the columns of user_input to match the model's expected order
user_input = user_input[expected_feature_order]

# Make prediction
if st.button('Predict Churn'):
    predict(model, user_input)
