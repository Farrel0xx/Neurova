import streamlit as st
import webbrowser
import plotly.graph_objects as go
import pandas as pd
import random
import os
import streamlit.components.v1 as components
from utils.pdf_processing import extract_text_from_pdf
from utils.ai_inference import get_response

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", st.secrets.get("GEMINI_API_KEY"))
SERPER_API_KEY = os.getenv("SERPER_API_KEY", st.secrets.get("SERPER_API_KEY"))
GROQ_API_KEY = os.getenv("GROQ_API_KEY", st.secrets.get("GROQ_API_KEY"))

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
            padding: 15px;
            background: #1e1e1e;
            color: white;
            border-radius: 10px;
            text-align: center;
            font-size: 14px;
            margin-top: 30px;
        }
        .footer a {
            color: #00c6ff;
            text-decoration: none;
            font-weight: bold;
        }
        .footer-icons {
            margin-top: 10px;
        }
        .footer-icons img {
            width: 30px;
            margin: 0 10px;
            transition: transform 0.3s ease;
        }
        .footer-icons img:hover {
            transform: scale(1.2);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header"><h1>🩺 ​🅽🅴🆄🆁🅾🆅🅰 🔬</h1><h4>"Revolutionizing Healthcare, One Diagnosis at a Time." 🚀</h4></div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("📄 Upload your blood report (PDF)", type="pdf")

if uploaded_file is not None:
    st.success("✅ PDF uploaded successfully!")

prompt1 = "Analyze this blood test report and provide medical insights."
prompt2 = "Summarize the blood report findings in a table."

st.markdown("---")
if st.button("🔍 Analyze Report"):
    text = extract_text_from_pdf(uploaded_file)
    response = get_response(text, prompt1)
    st.subheader("📁 Report Analysis")
    st.markdown(response, unsafe_allow_html=True)

if st.button("📊 Show Summary"):
    text = extract_text_from_pdf(uploaded_file)
    response = get_response(text, prompt2)
    st.subheader("📋 Summary")
    st.markdown(response, unsafe_allow_html=True)
   
if st.button("🏥 Find Best Doctors"):
    maps_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3952.605993567362!2d110.36949037401476!3d-7.829479377190809!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e7a5791f5d5d5d5%3A0x8e3c3d5d5d5d5d5!2sDoctor+Near+Me!5e0!3m2!1sen!2sid!4v1649457392485!5m2!1sen!2sid"
    st.markdown(f'<iframe src="{maps_url}" width="700" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>', unsafe_allow_html=True)


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
st.info(f"📌 Health Tip: {random.choice(health_tips)}")

st.subheader("📉 Blood Test Analysis (Advanced Visuals)")
data = pd.DataFrame({
    "Parameter": ["Hemoglobin", "RBC", "WBC", "Platelets"],
    "Value": [13.5, 4.8, 6500, 250000],
    "Normal Min": [12, 4.2, 4000, 150000],
    "Normal Max": [16, 5.5, 11000, 400000]
})

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

st.markdown("---")
st.subheader("💬 AI Medical Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask about your health...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    ai_response = get_response(user_input, "Medical Assistant AI Response")
    st.session_state.messages.append({"role": "assistant", "content": ai_response})

    with st.chat_message("assistant"):
        st.markdown(ai_response)

st.markdown("""
    <div class="footer">
        Developed by <a href="https://github.com/Farrel0xx" target="_blank">Farrel0xx</a> 🚀  
        <div class="footer-icons">
            <a href="https://www.youtube.com/@yourchannel" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/1384/1384060.png" alt="YouTube">
            </a>
            <a href="https://www.instagram.com/yourinstagram" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" alt="Instagram">
            </a>
            <a href="https://github.com/Farrel0xx" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/2111/2111432.png" alt="GitHub">
            </a>
        </div>
    </div>
""", unsafe_allow_html=True)
