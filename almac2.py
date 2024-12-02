import streamlit as st

# Title of the app
st.title("Streamlit with WhatsApp Web Integration")

# Split the layout into two columns
col1, col2 = st.columns([3, 7])

# Left column for app features
with col1:
    st.subheader("App Features")
    st.write("Here you can add other functionalities or elements of your app.")

# Right column for WhatsApp Web
with col2:
    st.subheader("WhatsApp Web")
    st.info("Note: WhatsApp Web may not load in all browsers due to embedding restrictions.")
    whatsapp_url = "https://web.whatsapp.com"
    st.components.v1.iframe(whatsapp_url, height=600, scrolling=True)
