import webbrowser
import time
from datetime import datetime

def open_whatsapp_at(scheduled_time):
    """
    Opens WhatsApp Web at the specified time.
    
    Args:
        scheduled_time (str): Time in HH:MM 24-hour format.
    """
    # Get current time
    now = datetime.now().strftime("%H:%M")
    print(f"Current time: {now}. Scheduled time: {scheduled_time}.")
    
    while now != scheduled_time:
        time.sleep(30)  # Check every 30 seconds
        now = datetime.now().strftime("%H:%M")
    
    print("Opening WhatsApp Web...")
    webbrowser.open("https://web.whatsapp.com")

# Example usage:
# Replace '14:30' with your desired time in HH:MM format
open_whatsapp_at("10:41")
