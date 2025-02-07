import os
import streamlit as st

GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY", "")
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY", "")
SERPER_API_KEY = st.secrets.get("SERPER_API_KEY") or os.getenv("SERPER_API_KEY", "")
