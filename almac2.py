import streamlit as st
import pywhatkit as kit
from datetime import datetime, timedelta

# Streamlit UI
st.title("Send WhatsApp Message at a Specific Time")

# Input for phone number, message, and time
phone_number = "+918438039821"
message = "Moonji"
time_input = "23:59"

# Function to schedule and send the message
def schedule_message(phone_number, message, send_time):
    # Get the current time and compare
    now = datetime.now()
    selected_time = datetime.combine(now.date(), send_time)

    # If the selected time is already passed today, schedule it for the next day
    if selected_time < now:
        selected_time += timedelta(days=1)

    # Send WhatsApp message automatically
    kit.sendwhatmsg(phone_number, message, selected_time.hour, selected_time.minute)

    return f"Message scheduled to be sent at {selected_time.strftime('%H:%M:%S')}."

# Button to schedule the message
if st.button("Schedule Message"):
    if phone_number and message and time_input:
        try:
            # Validate the time input format (HH:MM)
            send_time = datetime.strptime(time_input, "%H:%M").time()

            # Call the function to schedule the message
            result = schedule_message(phone_number, message, send_time)
            st.write(result)
            st.success("WhatsApp message will be sent automatically at the scheduled time!")
        except ValueError:
            st.error("Invalid time format. Please enter the time in HH:MM format.")
    else:
        st.error("Please fill in all the fields.")
