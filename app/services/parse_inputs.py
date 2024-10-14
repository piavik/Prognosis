import streamlit as st
import pandas as pd


# Function to get user input
def get_user_input():
    # Convert categorical variables to numerical encoding if necessary
    mapper = {'Yes': 1, 'No': 0}

    reamining_contract = st.number_input('reamining_contract', min_value=0.0, max_value=3.0, value=0.0)
    is_contract = 1 if reamining_contract > 0 else 0

    data = {
        'is_tv_subscriber': mapper[st.selectbox('Is TV subscriber', options=['Yes', 'No'])],
        # 'is_movie_package_subscriber': mapper[st.selectbox('Is Movie Pack subscriber', options=['Yes', 'No'])],
        'subscription_age': st.number_input('Age', min_value=0, max_value=100, value=30),
        'bill_avg': st.number_input('Bill Avg', min_value=0.0, max_value=1000.0, value=20.0),
        'reamining_contract': reamining_contract,
        'is_contract': is_contract,
        'service_failure_count': st.number_input('service_failure_count', min_value=0.0, max_value=10000.0, value=0.0),
        'download_avg': st.number_input('download_avg', min_value=0.0, max_value=100000.0, value=20.0),
        # 'upload_avg': st.number_input('upload_avg', min_value=0.0, max_value=100000.0, value=20.0),
        # 'download_over_limit': st.number_input('download_over_limit', min_value=0.0, max_value=100000.0, value=0.0),
    }

    features = pd.DataFrame(data, index=[0])
    return features