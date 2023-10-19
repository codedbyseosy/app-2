import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Ypur message") #this allows us to enter multiple lines of text as opposed to a single line
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}"""
    
    button = st.form_submit_button("Submit") #special button design to submit its assigned form
    print(button)
    if button:
       send_email(message)
       st.info("Your email was sent successfully.")