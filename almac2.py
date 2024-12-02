import streamlit as st

# Title of the app
st.title("Streamlit WhatsApp Chat Integration")

# Input for phone number
phone_number = st.text_input("Enter the phone number (with country code, e.g., +919876543210):")

# Generate the link and button
if phone_number:
    whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}"
    
    # Button to open the specific WhatsApp chat
    if st.button("Open WhatsApp Chat"):
        st.markdown(
            f'<a href="{whatsapp_url}" target="_blank">Open WhatsApp Chat</a>',
            unsafe_allow_html=True,
        )
else:
    st.write("Enter a phone number above to enable the chat button.")
