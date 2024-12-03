import pywhatkit as kit

# Send a WhatsApp message
# Parameters: phone number (with country code), message, hour, minute
# It will send the message at the specified time

# Example: send message to +91xxxxxxxxxx at 10:30 AM
kit.sendwhatmsg("+919360871557", "Hello, this is an automated message from Python!", 12, 35)
