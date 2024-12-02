import streamlit as st

# WhatsApp group link
group_link = "https://chat.whatsapp.com/GrHQES9rLrh1Wc1nPqnDCw"

# Redirect the user to the WhatsApp group chat
st.markdown(
    f"""
    <script>
        window.location.href = "{group_link}";
    </script>
    """,
    unsafe_allow_html=True,
)
