import streamlit as st

from services.load_models import load_model, predict
from services.parse_inputs import get_user_input


model = load_model('svm_model.pkl')
expected_feature_order = [
        'is_tv_subscriber', 
        'is_movie_package_subscriber',
        "reamining_contract",
        'subscription_age',
        'bill_avg',
        'service_failure_count',
        'download_avg',
        'upload_avg',
        'download_over_limit'
         ]


# Title and description
st.title("SVM")
st.write("""
This app uses a trained SVM model to make predictions.
""")

expected_feature_order.remove('service_failure_count')
expected_feature_order.remove('download_over_limit')
# Get user input
user_input = get_user_input()

# Reorder the columns of user_input to match the model's expected order
user_input = user_input[expected_feature_order]

# user_input.remove('service_failure_count', 'download_over_limit')

# Make prediction
if st.button('Predict Churn'):
    predict(model, user_input)