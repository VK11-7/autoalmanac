import streamlit as st
import webbrowser

# Title of the app
st.title("Direct WhatsApp Group Link")

# WhatsApp group link
group_link = "https://chat.whatsapp.com/GrHQES9rLrh1Wc1nPqnDCw"

# Open the link in the default web browser
st.write("Redirecting you to the WhatsApp group chat...")
webbrowser.open_new_tab(group_link)

# Informational fallback for users
st.markdown(
    f"If the page does not open automatically, click [here]({group_link}) to join the group.",
    unsafe_allow_html=True,
)
