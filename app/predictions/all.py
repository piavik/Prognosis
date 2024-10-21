import streamlit as st

from services.load_models import load_model
from services.parse_inputs import get_user_input


def predict(model, user_input):
    # Make prediction
    prediction = model.predict(user_input)
    # If your model predicts probabilities, you can also display them
    prediction_proba = model.predict_proba(user_input)

    # Map prediction to class names if necessary
    class_names = ['Not Churn', 'Churn']  # Replace with your class names

    # st.subheader('Prediction:')
    st.write(f"Result: **{class_names[int(prediction[0])]}**")

    # st.subheader('Prediction Probability:')
    st.write(f"Probability: {prediction_proba[0][int(prediction[0])]*100:.2f}%")


model = load_model('xgb_model.pkl')
expected_feature_order = model.feature_names_in_


# Title and description
st.title("Models Comparison")
st.write("""
Compare different models predictions on the same input data.
""")


# Get user input
user_input = get_user_input()

# Reorder the columns of user_input to match the model's expected order
user_input = user_input[expected_feature_order]


# Make prediction
if st.button('Predict Churn'):
    # predict(model, user_input)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write(f'**LinearRegression**')
        model = load_model('logistic_regression_model.pkl')
        predict(model, user_input)

    with col2:
        st.write(f'**RandomForest**')
        model = load_model('random_forest_model.pkl')
        predict(model, user_input)

    with col3:
        st.write(f'**NN**')
        model = load_model('mlp_model.pkl')
        predict(model, user_input)

    with col4:
        st.write(f'**XGBoost**')
        model = load_model('xgb_model.pkl')
        predict(model, user_input)


    with col5:
        st.write(f'**SVM**')
        model = load_model('svm_model.pkl')
        # predict(model, user_input)
        prediction = model.predict(user_input)
        # If your model predicts probabilities, you can also display them
        # prediction_proba = model.predict_proba(user_input)

        # Map prediction to class names if necessary
        class_names = ['Not Churn', 'Churn']  # Replace with your class names

        # st.subheader('Prediction:')
        st.write(f"Result: **{class_names[int(prediction[0])]}**")

        # st.subheader('Prediction Probability:')
        # st.write(f"Probability: {prediction_proba[0][int(prediction[0])]*100:.2f}%")