import streamlit as st

def main():
    st.title("WhatsApp Web in Streamlit")

    whatsapp_web_url = "https://web.whatsapp.com/"

    st.iframe(whatsapp_web_url, width=600, height=600)

if __name__ == "__main__":
    main()
