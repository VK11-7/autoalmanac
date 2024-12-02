import pyautogui
import time
import schedule

# Function to send a WhatsApp message
def send_whatsapp_message():
    # You need to have WhatsApp Web open and the group selected
    # The following keys are specific to the layout of your screen, you may need to adjust.
    time.sleep(2)  # Give some time for WhatsApp Web to be in focus
    pyautogui.write('Hello, this is a scheduled message!')  # Write the message
    pyautogui.press('enter')  # Send the message

# Function to schedule the message
def schedule_message():
    schedule.every().day.at("10:30").do(send_whatsapp_message)  # Schedule for 10:30 AM daily

    while True:
        schedule.run_pending()
        time.sleep(1)

# Start scheduling the message
schedule_message()
