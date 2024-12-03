import streamlit as st

# Function to generate a WhatsApp message link
def generate_whatsapp_link(phone_number, message):
    """
    Generates a WhatsApp message link for manual sending.
    
    Args:
        phone_number (str): The recipient's phone number (with country code).
        message (str): The message content.
        
    Returns:
        str: The generated WhatsApp link.
    """
    base_url = "https://wa.me/"
    formatted_message = message.replace(" ", "%20").replace("\n", "%0A")
    return f"{base_url}{phone_number}?text={formatted_message}"

# Streamlit App
st.title("WhatsApp Message Generator")

# Input fields
recipient = st.text_input("Recipient Phone Number (with country code)", "+1234567890")
message = st.text_area("Message", "Hello! This is a test message.")

# Generate link button
if st.button("Generate WhatsApp Link"):
    if recipient and message:
        whatsapp_link = generate_whatsapp_link(recipient, message)
        st.success("Your WhatsApp message link has been generated!")
        st.write(f"[Click here to send your message!]({whatsapp_link})")
    else:
        st.error("Please provide both a recipient number and a message!")

# Display Instructions
st.info("""
### Instructions:
1. Enter the recipient's phone number (e.g., +1234567890 for international numbers).
2. Write your message.
3. Click "Generate WhatsApp Link".
4. Click on the generated link to manually send the message via WhatsApp Web.
""")
