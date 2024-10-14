import os
import streamlit as st
import joblib
import pandas as pd


current_dir = os.path.dirname(os.path.abspath(__file__))
def_model_path = os.path.join(current_dir, '..', '..', 'models', 'random_forest_model.pkl')
model_path = os.environ.get('DOCKER_MODEL_PATH', def_model_path)


@st.cache_resource
def load_model(file_path):
    return joblib.load(file_path)


model = load_model(model_path)
expected_feature_order = model.feature_names_in_


# Title and description
st.title("Random Forest Classifier Prediction App")
st.write("""
This app uses a trained Random Forest model to make predictions.
Please input the required features to get a prediction.
""")


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


# Get user input
user_input = get_user_input()

# Reorder the columns of user_input to match the model's expected order
user_input = user_input[expected_feature_order]

# Make prediction
if st.button('Predict'):
    prediction = model.predict(user_input)
    # If your model predicts probabilities, you can also display them
    prediction_proba = model.predict_proba(user_input)

    # Map prediction to class names if necessary
    class_names = ['Not Churn', 'Churn']  # Replace with your class names

    st.subheader('Prediction:')
    st.write(f"Predicted Class: {class_names[int(prediction[0])]}")

    st.subheader('Prediction Probability:')
    st.write(f"Probability: {prediction_proba[0][int(prediction[0])]:.2f}")
