import streamlit as st

# WhatsApp link format: https://wa.me/<phone_number>?text=<message>
whatsapp_number = "+918438039821"  # Replace with your phone number
message = "Hello, this is a message from Streamlit!"

# Create a clickable link
st.markdown(f"Click [here](https://wa.me/{whatsapp_number}?text={message}) to send a WhatsApp message!")
