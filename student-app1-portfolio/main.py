import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")

company_intro = """
A company profile can show investors and stakeholders the value of a company, 
along with its mission, goals and performance. Discovering what to include in a 
company profile can help you write a profile that engages readers and promotes 
a company's image.
"""
st.header(company_intro)

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv")

st.subheader("Our Team")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image('images/' + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image('images/' + row["image"])

with col3:
    for index, row in df[8:12].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image('images/' + row["image"])
