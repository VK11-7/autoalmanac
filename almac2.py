import streamlit as st
import schedule
import time
from datetime import datetime

# WhatsApp link format: https://wa.me/<phone_number>?text=<message>
whatsapp_number = "+1234567890"  # Replace with your phone number
message = "Hello, this is a message from Streamlit!"

# Define the function to show the WhatsApp message link
def show_whatsapp_link():
    st.markdown(f"Click [here](https://wa.me/{whatsapp_number}?text={message}) to send a WhatsApp message!")

# Scheduler function to run every day at a specific time (e.g., 10:30 AM)
def schedule_message():
    schedule.every().day.at("10:30").do(show_whatsapp_link)  # Set the desired time here (HH:MM format)

    while True:
        schedule.run_pending()
        time.sleep(1)

# Run the scheduler in the background when the Streamlit app starts
if st.button("Start Scheduler"):
    st.write("Scheduler started. The link will be displayed at 10:30 AM every day.")
    schedule_message()
