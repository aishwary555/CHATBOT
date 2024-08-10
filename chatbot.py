import streamlit as st
import google.generativeai as genai

# Configure the API key
llm_api_key = "AIzaSyCL7gDAIyywRtg0jXq9VkV-enf-AyzzcA4"
genai.configure(api_key=llm_api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

# Streamlit app
st.title("Chatbot using Google Generative AI")
st.write("Ask me anything!")

# Input text from the user
user_input = st.text_input("You:", "")

# Generate response using the model
if user_input:
    response = model.generate_content(user_input)
    st.text_area("Chatbot:", value=response.text, height=200)

