import streamlit as st

# Title of the app
st.title("Direct WhatsApp Group Chat Link")

# WhatsApp group link
group_link = "https://chat.whatsapp.com/GrHQES9rLrh1Wc1nPqnDCw"

# Automatically redirect to the group link
st.markdown(
    f'<meta http-equiv="refresh" content="0; url={group_link}">',
    unsafe_allow_html=True,
)
