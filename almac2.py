import streamlit as st
from whatsapp_chatbot import WhatsappBot

def main():
    st.title("WhatsApp Message Sender")

    phone_number = st.text_input("Phone Number")
    message = st.text_area("Message")

    if st.button("Send Message"):
        bot = WhatsappBot()
        bot.send_message(phone_number, message)

if __name__ == "__main__":
    main()
