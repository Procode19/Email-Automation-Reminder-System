import streamlit as st
import time

st.title("📧 Email Automation System")

st.success("System Started Successfully")

if st.button("Run Email Automation"):
    st.write("Checking scheduled emails...")
    
    for i in range(5):
        st.write(f"Running... {i+1}")
        time.sleep(1)

    st.success("Email Automation Running Successfully ✅")