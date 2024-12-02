# import streamlit as st
# import pywhatkit as kit
# import datetime

# def send_whatsapp_message(group_id, message, time_hour, time_minute):
#     try:
#         kit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute)
#         st.success("Message scheduled successfully!")
#     except Exception as e:
#         st.error(f"Failed to send message: {e}")

# st.title("Automate WhatsApp Group Messages")

# # Input for group ID
# group_id = st.text_input("Enter WhatsApp Group ID", help="Find the group ID in the URL after 'https://chat.whatsapp.com/'")

# # Input for the message
# message = st.text_area("Enter your message", help="Write the message you want to send to the group")

# # Input for time to send
# send_time = st.time_input("Choose a time to send the message", value=datetime.time(datetime.datetime.now().hour + 1, 0))

# if st.button("Send Message"):
#     hour = send_time.hour
#     minute = send_time.minute
#     send_whatsapp_message(group_id, message, hour, minute)
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def send_whatsapp_message(phone_no, message):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://web.whatsapp.com/")

    # Wait for QR code scan
    time.sleep(20)

    # Find the search box
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
    search_box.send_keys(phone_no)
    time.sleep(5)

    # Find the chat and send message
    chat_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
    chat_box.send_keys(message)
    chat_box.send_keys(Keys.ENTER)

    time.sleep(5)
    driver.quit()

# Streamlit app
st.title("WhatsApp Message Sender")

phone_number = st.text_input("Enter Phone Number (with country code)")
message = st.text_input("Enter Message")

if st.button("Send Message"):
    send_whatsapp_message(phone_number, message)
    st.success("Message sent successfully!")
