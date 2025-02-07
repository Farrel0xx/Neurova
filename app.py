import streamlit as st
import webbrowser
import plotly.graph_objects as go
import pandas as pd
import random
from utils.pdf_processing import extract_text_from_pdf
from utils.ai_inference import get_response
from utils.search_tools import find_doctors_nearby

# 🎨 Custom CSS untuk tampilan keren
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        html, body, [class*="st-"] {
            font-family: 'Poppins', sans-serif;
        }

        .header {
            text-align: center;
            padding: 15px;
            border-radius: 10px;
            background: linear-gradient(to right, #00c6ff, #0072ff);
            color: white;
        }

        .footer {
            position: relative;
            padding: 10px;
            background: #1e1e1e;
            color: white;
            border-radius: 10px;
            text-align: center;
            font-size: 12px;
            margin-top: 30px;
        }

        .footer a {
            color: #00c6ff;
            text-decoration: none;
        }

        .disclaimer {
            background-color: #C0C0C0;
            padding: 10px;
            color: black;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
        }

        .full-width-text {
            text-align: justify;
            padding: 10px;
            border-radius: 5px;
            background-color: rgba(255, 255, 255, 0.1);
            max-height: 300px;
            overflow-y: auto;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# 🏥 Header
st.markdown('<div class="header"><h1>🩺 PathoPro 🔬</h1><h4>Your AI-Powered Medical Assistant</h4></div>', unsafe_allow_html=True)

# 📂 Upload File PDF
uploaded_file = st.file_uploader("💄 Upload your blood report (PDF)", type="pdf")

if uploaded_file is not None:
    st.success("✅ PDF uploaded successfully!")

# 🎯 Prompts untuk AI
prompt1 = "Analyze this blood test report and provide medical insights."
prompt2 = "Summarize the blood report findings in a table."
prompt3_temp = "Provide a short summary of the alarming factors in this blood report."

# 🔥 Gunakan Columns untuk Tampilan Lebih Rapi
st.markdown("---")
if st.button("🔍 Analyze Report"):
    text = extract_text_from_pdf(uploaded_file)
    response = get_response(text, prompt1)
    st.subheader("📁 Report Analysis")
    st.markdown(f'<div class="full-width-text">{response}</div>', unsafe_allow_html=True)

if st.button("📊 Show Summary"):
    text = extract_text_from_pdf(uploaded_file)
    response = get_response(text, prompt2)
    st.subheader("📋 Summary")
    st.markdown(f'<div class="full-width-text">{response}</div>', unsafe_allow_html=True)

if st.button("🏥 Find Best Doctors"):
    webbrowser.open("https://www.google.com/maps/search/doctors+near+me/")

# 🔥 Health Tips Section
health_tips = [
    "💧 Stay hydrated: Drink at least 8 glasses of water daily!",
    "🍎 Eat more fruits and veggies for a stronger immune system!",
    "🏃‍♂️ Exercise regularly to maintain heart health!",
    "😴 Good sleep helps your immune system stay strong!",
    "🧘‍♂️ Reduce stress for better mental and physical health!",
    "💊 Take your vitamins and minerals as needed!",
    "🚶‍♀️ Walking 30 minutes a day can improve your mood!",
    "🦷 Brush and floss daily for good oral hygiene!"
]
random_tip = random.choice(health_tips)

col1, col2 = st.columns(2)

with col1:
    if st.button("🏥 Find Nearby Hospital / Pharmacy"):
        webbrowser.open("https://www.google.com/maps/search/hospital+near+me/")

with col2:
    st.info(f"📌 Health Tip: {random_tip}")

# 📊 Blood Test Analysis (Bubble Chart & Gauge Chart)
st.subheader("📉 Blood Test Analysis (Advanced Visuals)")

# Data Dummy untuk Chart
data = pd.DataFrame({
    "Parameter": ["Hemoglobin", "RBC", "WBC", "Platelets"],
    "Value": [13.5, 4.8, 6500, 250000],
    "Normal Min": [12, 4.2, 4000, 150000],
    "Normal Max": [16, 5.5, 11000, 400000]
})

# 🎈 Bubble Chart
bubble_chart = go.Figure()
bubble_chart.add_trace(go.Scatter(
    x=data["Parameter"],
    y=data["Value"],
    mode='markers',
    marker=dict(size=[50, 40, 70, 60], color=['blue', 'red', 'green', 'purple']),
    text=data["Value"],
    hoverinfo='text',
))

bubble_chart.update_layout(
    title="Blood Test Bubble Chart",
    xaxis_title="Blood Parameter",
    yaxis_title="Value",
    template="plotly_white"
)

st.plotly_chart(bubble_chart)

# 🎯 Gauge Chart untuk Hemoglobin
gauge_chart = go.Figure(go.Indicator(
    mode="gauge+number",
    value=13.5,  # Dummy value for Hemoglobin
    title={'text': "Hemoglobin Level"},
    gauge={'axis': {'range': [10, 18]},
           'steps': [{'range': [10, 12], 'color': "red"},
                     {'range': [12, 16], 'color': "green"},
                     {'range': [16, 18], 'color': "red"}]}
))

st.plotly_chart(gauge_chart)

st.markdown('<div class="footer">Developed by <a href="#">YourName</a></div>', unsafe_allow_html=True)
