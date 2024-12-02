import streamlit as st
import pywhatkit as kit
import datetime

def send_whatsapp_message(group_id, message, time_hour, time_minute):
    try:
        kit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute)
        st.success("Message scheduled successfully!")
    except Exception as e:
        st.error(f"Failed to send message: {e}")

st.title("Automate WhatsApp Group Messages")

# Input for group ID
group_id = st.text_input("Enter WhatsApp Group ID", help="Find the group ID in the URL after 'https://chat.whatsapp.com/'")

# Input for the message
message = st.text_area("Enter your message", help="Write the message you want to send to the group")

# Input for time to send
send_time = st.time_input("Choose a time to send the message", value=datetime.time(datetime.datetime.now().hour + 1, 0))

if st.button("Send Message"):
    hour = send_time.hour
    minute = send_time.minute
    send_whatsapp_message(group_id, message, hour, minute)
