import streamlit as st

random_forest = st.Page("predictions/random_forest.py", title="Random Forest", icon=":material/dashboard:")
logistic_regression = st.Page("predictions/logistic_regression.py", title="Logistic regression", icon=":material/dashboard:")
experiments = st.Page("eda/experiments.py", title="Experiments", icon=":material/add_circle:")
primary_analysis = st.Page("eda/primary_analysis.py", title="Primary analysis", icon=":material/add_circle:")

pg = st.navigation(
    {
        "Make predictions": [random_forest, logistic_regression],
        "EDA": [primary_analysis, experiments],
    }
)

st.set_page_config(page_title="Prognosis project", page_icon=":material/edit:")
pg.run()
