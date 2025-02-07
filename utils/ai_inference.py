import google.generativeai as genai
from langchain_groq import ChatGroq
from config import GOOGLE_API_KEY, GROQ_API_KEY

# Setup Google Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Setup Llama (Groq)
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama-3.2-1b-preview"
)

def get_response(content, prompt):
    """Menghasilkan respon dari model Gemini"""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        [content, prompt], 
        generation_config={
            "temperature": 0.7, 
            "max_output_tokens": 1024
        }
    )
    return response.text
