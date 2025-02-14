import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("placement_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🎓 Student Placement Prediction")
st.write("Enter student details to predict placement outcome.")

# Remove city input
cgpa = st.number_input("Enter CGPA:", min_value=0.0, max_value=10.0, step=0.1)
iq = st.number_input("Enter IQ Score:", min_value=0, max_value=200, step=1)

if st.button("Predict Placement"):
    # Prepare input data without the city
    input_data = np.array([[cgpa, iq]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("🎉 Student is likely to be placed!")
    else:
        st.error("❌ Student is unlikely to be placed.")
