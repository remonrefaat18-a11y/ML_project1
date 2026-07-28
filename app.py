import joblib
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Liver Disease Prediction",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Liver Disease Prediction System")
st.markdown("### Enter the patient's medical test results")
st.divider()

col1, col2 = st.columns(2)

with col1:
    TotalBilirubin = st.number_input("Total Bilirubin")
    DirectBilirubin = st.number_input("Direct Bilirubin")
    AlkphosAlkalinePhosphotase = st.number_input("Alkaline Phosphotase")
    SgptAlamineAminotransferase = st.number_input("SGPT")

with col2:
    SgotAspartateAminotransferase = st.number_input("SGOT")
    TotalProtiens = st.number_input("Total Proteins")
    ALBAlbumin = st.number_input("Albumin")
    AGRatioAlbuminandGlobulinRatio = st.number_input("A/G Ratio")



model = joblib.load("models/best_model.joblib")


input_data = pd.DataFrame({
    "Total Bilirubin": [TotalBilirubin],
    "Direct Bilirubin": [DirectBilirubin],
    "Alkphos Alkaline Phosphotase": [AlkphosAlkalinePhosphotase],
    "Sgpt Alamine Aminotransferase": [SgptAlamineAminotransferase],
    "Sgot Aspartate Aminotransferase": [SgotAspartateAminotransferase],
    "Total Protiens": [TotalProtiens],
    "ALB Albumin": [ALBAlbumin],
    "A/G Ratio Albumin and Globulin Ratio":[AGRatioAlbuminandGlobulinRatio]
})

predict = st.button(
    "🔍 Predict",
    use_container_width=True
)

if predict:

    with st.spinner("Analyzing patient data..."):
        prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Patient has Liver Disease")
        prob = model.predict_proba(input_data)
        confidence = prob[0][1]
        st.metric(
        label="Prediction Confidence",
        value=f"{confidence*100:.2f}%"
        )   
        st.progress(int(confidence * 100))
        
    else:
        st.success("✅ Patient is Healthy")
        prob = model.predict_proba(input_data)
        confidence = prob[0][0]
        st.metric(
        label="Prediction Confidence",
        value=f"{confidence*100:.2f}%"
        )  
        st.progress(int(confidence * 100))





