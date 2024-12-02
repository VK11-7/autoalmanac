import streamlit as st
import webbrowser

def open_whatsapp_chat(phone_number):
    """Opens a WhatsApp chat with the given phone number."""
    url = f"https://wa.me/{phone_number}"
    webbrowser.open(url)

# Streamlit app
st.title("WhatsApp Chat Opener")

phone_number = st.text_input("Enter Phone Number (with country code)")

if st.button("Open Chat"):
    open_whatsapp_chat(phone_number)
    st.success("Opening WhatsApp chat...")
