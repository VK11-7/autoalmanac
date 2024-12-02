import streamlit as st

# Title of the app
st.title("Open WhatsApp Web")

# WhatsApp Web URL
whatsapp_web_url = "https://web.whatsapp.com/"

# Automatically redirect to WhatsApp Web
st.markdown(
    f"""
    <script>
        window.location.href = "{whatsapp_web_url}";
    </script>
    """,
    unsafe_allow_html=True,
)
