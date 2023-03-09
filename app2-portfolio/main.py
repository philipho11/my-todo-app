import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    Tour Scraper;A program that checks a music band's website and sends an email when 
    there are new tours.; Helper Chatbot;A chatbot that knows about a specific topic and answers questions
    regarding that topic.
    Tour Scraper;A program that checks a music band's website and sends an email when 
    there are new tours.; Helper Chatbot;A chatbot that knows about a specific topic and answers questions
    regarding that topic.
    """
    st.info(content)

