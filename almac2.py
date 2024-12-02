import streamlit as st
import pywhatkit as kit
import pyautogui
import time
from datetime import datetime, timedelta

# Streamlit app title
st.title("Automate WhatsApp Messages")

# Inputs for WhatsApp automation
st.header("Send a WhatsApp Message")

# WhatsApp group ID or phone number
recipient_type = st.radio("Send to", options=["Phone Number", "Group ID"])
if recipient_type == "Phone Number":
    recipient = st.text_input("Enter the phone number (with country code)", help="E.g., +11234567890")
else:
    recipient = st.text_input("Enter the WhatsApp Group ID", help="E.g., XYZabc123DEF456")

# Message content
message = st.text_area("Enter your message", help="Type the message you want to send")

# Send time
send_time = st.time_input(
    "Choose the time to send the message (must be in the future)", 
    value=(datetime.now() + timedelta(minutes=1)).time()
)

# Send message button
if st.button("Send Message"):
    try:
        # Parse send time
        now = datetime.now()
        send_hour = send_time.hour
        send_minute = send_time.minute

        # Check if recipient is a phone number or group ID
        if recipient_type == "Phone Number":
            st.info("Scheduling WhatsApp message...")
            kit.sendwhatmsg(recipient, message, send_hour, send_minute)
        else:
            st.info("Scheduling WhatsApp group message...")
            kit.sendwhatmsg_to_group(recipient, message, send_hour, send_minute)
        
        # Notify user after sending
        time.sleep(5)  # Wait for pywhatkit to open WhatsApp and type the message
        pyautogui.press("enter")  # Simulate pressing enter to send the message
        st.success("Message sent successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
