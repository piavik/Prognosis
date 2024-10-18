import streamlit as st
import pandas as pd


# Function to get user input
def get_user_input():
    # Convert categorical variables to numerical encoding if necessary
    # mapper = {'Yes': 1, 'No': 0}

    reamining_contract = st.slider('reamining_contract', min_value=0.0, max_value=3.0, value=0.0)
    # is_contract = 1 if reamining_contract > 0 else 0

    data = {
        # 'is_tv_subscriber': mapper[st.selectbox('Is TV subscriber', options=['Yes', 'No'])],
        'is_tv_subscriber': int(st.toggle('Is TV subscriber', value=True)),
        # 'is_movie_package_subscriber': mapper[st.selectbox('Is Movie Pack subscriber', options=['Yes', 'No'])],
        'is_movie_package_subscriber': int(st.toggle('Is Movie Pack subscriber', value=True)),
        'subscription_age': st.slider('Contract Age', min_value=0, max_value=15, value=3),
        'bill_avg': st.slider('Bill Avg', min_value=0.0, max_value=500.0, value=20.0),
        'reamining_contract': reamining_contract,
        # 'is_contract': is_contract,
        'service_failure_count': st.slider('service_failure_count', min_value=0, max_value=20, value=0),
        'download_avg': st.slider('download_avg', min_value=0.0, max_value=5000.0, value=20.0),
        'upload_avg': st.slider('upload_avg', min_value=0.0, max_value=500.0, value=20.0),
        'download_over_limit': st.slider('download_over_limit', min_value=0.0, max_value=100.0, value=0.0),
    }
    print(data)
    features = pd.DataFrame(data, index=[0])
    features.drop(columns=['service_failure_count', 'download_over_limit'], inplace=True)
    return features