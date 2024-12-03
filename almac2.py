import pywhatkit as kit

# Function to send a WhatsApp message
def send_whatsapp_message():
    # Replace with recipient's phone number (including country code)
    phone_number = "+918438039821"  # Example: "+911234567890" for India

    # Replace with your message
    message = "Hello! This is a test message sent using Python."

    # Set the time (24-hour format) to send the message
    hour = 10  # Example: 2 PM
    minute = 46  # Example: 30 minutes past 2 PM

    try:
        # Schedule the message
        kit.sendwhatmsg(phone_number, message, hour, minute)
        print("Message scheduled successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
send_whatsapp_message()
