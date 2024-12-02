import streamlit as st

# Title of the app
st.title("Streamlit with WhatsApp Integration")

st.write("Click the button below to open WhatsApp Web in a new tab.")

# Button to open WhatsApp Web
if st.button("Open WhatsApp Web"):
    st.markdown(
        '<a href="https://web.whatsapp.com" target="_blank">Open WhatsApp Web</a>',
        unsafe_allow_html=True,
    )
