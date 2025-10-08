# app.py
import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open('iris_model.pkl', 'rb'))

# ----------- Custom CSS with Header & Footer ------------
st.markdown("""
<style>
/* Background Image */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1652706495124-09a29f1eba01?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Top-right Header */
#top-header {
    position: fixed;
    top: 80px;
    right: 20px;
    background-color: rgba(0,0,0,0.5);
    padding: 8px 16px;
    border-radius: 8px;
    color: white;
    font-size: 18px;
    font-weight: bold;
    z-index: 100;
}

/* Bottom-left Footer */
#bottom-footer {
    position: fixed;
    bottom: 10px;
    left: 20px;
    background-color: rgba(0,0,0,0.5);
    padding: 6px 14px;
    border-radius: 6px;
    color: white;
    font-size: 14px;
    z-index: 100;
}
</style>

<div id="top-header">Respected Sir Shahzaib & Sir Ali Hamza</div>
<div id="bottom-footer">Developed by Faraz Hussain</div>
""", unsafe_allow_html=True)

# Page title
st.title("🌸 Iris Flower Classifier")
st.markdown("Enter sepal and petal values to predict flower species.")

# Input sliders
sepal_length = st.slider("Sepal Length (cm)", 0.0, 10.0, 5.1)
sepal_width  = st.slider("Sepal Width (cm)",  0.0, 10.0, 3.5)
petal_length = st.slider("Petal Length (cm)", 0.0, 10.0, 1.4)
petal_width  = st.slider("Petal Width (cm)",  0.0, 10.0, 0.2)

# Predict button
if st.button("🌼 Predict Species"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    st.success(f"🌸 Predicted Species: **{prediction[0]}**")



