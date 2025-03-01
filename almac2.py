import time
import sys
import requests
import pandas as pd
from io import BytesIO
import urllib
from datetime import datetime, timedelta
import streamlit as st
import docx

st.balloons()
st.title('Welcome🙏🏻')
st.header('Simply Ayurveda presents🌿')
st.subheader('Dainika Almanac🗓️')

# Date Selection
selected_date = st.date_input("Select a date")
if selected_date:
    formatted_date = selected_date.strftime("%d/%m/%Y")

st.write(f"Almanac of 📝: {formatted_date}")

# Drik Panchang URL
url1 = f'https://www.drikpanchang.com/panchang/day-panchang.html?geoname-id=1277333&date={formatted_date}'

# Google Sheets URL
url4 = 'https://docs.google.com/spreadsheets/d/1h2rVBV6X2gNg4hRNVFT26DoW-cbOnHEesF2oz9wipDo/edit?gid=1491417857#gid=1491417857'

url2 = 'https://docs.google.com/spreadsheets/d/1W_CG0CD7j7yFBB5W8DDdLSA2dyztyAQ9Pn03RPcAbyY/edit?gid=0#gid=0'

url3 = 'https://docs.google.com/document/d/1xwy3aN2VSTTAw0Z7chr36PELaf8a4Mv0Gy2snZ0YAas/edit?tab=t.0'

# Collapsible Sections
with st.expander("📜 View Drik Panchang"):
    st.components.v1.iframe(url1, width=700, height=500, scrolling=True)
    st.markdown(f"[Click here to open in a new tab]({url1})")
    
with st.expander("📊 View Sudhakala Vishakala Google Sheet"):
    st.components.v1.iframe(url2, width=700, height=500, scrolling=True)
    st.markdown(f"[Click here to open in a new tab]({url2})")

with st.expander("📊 View Body of Kal Purusha By Nakshatra Google Sheet"):
    st.components.v1.iframe(url3, width=700, height=500, scrolling=True)
    st.markdown(f"[Click here to open in a new tab]({url3})")

with st.expander("📊 View or Update Dainika Almanac Google Sheet"):
    st.components.v1.iframe(url4, width=700, height=500, scrolling=True)
    st.markdown(f"[Click here to open in a new tab]({url4})")

with st.expander("💬 View or copy or send Dainika Almanac Message"):
    response = requests.get("https://docs.google.com/spreadsheets/d/1h2rVBV6X2gNg4hRNVFT26DoW-cbOnHEesF2oz9wipDo/export?format=csv")
    df = pd.read_csv(BytesIO(response.content))
    df.to_csv('almanac1.csv', index = False)
    dd = pd.read_csv('almanac1.csv')
    formatted_date1 = selected_date.strftime("%d-%m-%Y")
    res = dd.loc[df['Date'] == formatted_date1]
    Date=res['Date'].values[0]
    Weekday=res['Weekday'].values[0]
    Sunrise=res['Sunrise'].values[0]
    Sunset=res['Sunset'].values[0]
    Moonrise=res['Moonrise'].values[0]
    Moonset=res['Moonset'].values[0]
    Samvatsara=res['Samvatsara'].values[0]
    Ayana=res['Ayana'].values[0]
    Ritu=res['Rtu'].values[0]
    Masa=res['Masa'].values[0]
    Kollamera=res['Kollam era'].values[0]
    Paksha=res['Paksha'].values[0]
    Tithi=res['Tithi'].values[0]
    Vasara=res['Vasara'].values[0]
    Nakshatra=res['Nakshatra'].values[0]
    Sunsign=res['Sunsign'].values[0]
    Moonsign=res['Moonsign'].values[0]
    Brahmamuhurta=res['Brahma muhurta'].values[0]
    Pratahsandhya=res['Pratah sandhya'].values[0]
    Abhijitmuhurta=res['Abhijit muhurta'].values[0]
    Saayamsandhya=res['Saayam sandhya'].values[0]
    Rahukalam=res['Rahu kalam'].values[0]
    Yamaganda=res['Yama ganda'].values[0]
    Gulikaikaalam=res['Gulikai Kaalam'].values[0]
    Significance=res['Significance'].values[0]
    Sudhakalainmen=res['Sudhakala in Purusha'].values[0]
    Vishakalainmen=res['Vishakala in Purusha'].values[0]
    Sudhakalainwomen=res['Sudhakala in Stri'].values[0]
    Vishakalainwomen=res['Vishakala in Stri'].values[0]
    Chakrabasedonvasara=res['Chakra based on vasara'].values[0]
    Bodypartbasedonnakshatra=res['The Body of Kal Purusha by Nakshatra'].values[0]

    message = """
Simply Ayurveda - Dainika Vaidya Almanac

✨ Suprabhatam ✨

{Date}
{Weekday}

☀️ Sunrise – {Sunrise}
🌇 Sunset – {Sunset}
🌒 Moonrise – {Moonrise}
🌃 Moonset – {Moonset}

Samvatsara – {Samvatsara}
Ayana - {Ayana}
Ritu – {Ritu}
Masa - {Masa}
Kollam era – {Kollamera}
Paksha – {Paksha}
Tithi – {Tithi}
Vasara – {Vasara}
Nakshatra – {Nakshatra}
Sunsign – {Sunsign}
Moonsign – {Moonsign}

✨ Auspicious hours -✨
🪷 Brahma muhurta – {Brahmamuhurta}
🌼 Pratah sandhya – {Pratahsandhya}
🌸 Abhijit muhurta – {Abhijitmuhurta}
🌼 Saayam sandhya – {Saayamsandhya}

🛑 Hours to be careful around
❌Rahu kalam – {Rahukalam}
‼️Yama ganda – {Yamaganda}
💊Gulikai Kaalam – {Gulikaikaalam}

Significance – {Significance}

🩺✡️ Medicoastrological significance -
Sudhakala in women – {Sudhakalainwomen}🚺
Sudhakala in men – {Sudhakalainmen}🚹
Vishakala in women – {Vishakalainwomen}🦳
Vishakala in men – {Vishakalainmen}🧔🏻‍♂
Chakra based on vasara – {Chakrabasedonvasara}

🦶 Body of Kala Purusha according to Nakshatra –

{Bodypartbasedonnakshatra}
Have we missed anything important?
Message Simply Ayurveda on WhatsApp. https://wa.me/message/DTX6RK5L6HE3B1
Subscribe to our YouTube channel - https://youtube.com/c/SimplyAyurveda
    """
    msg = message.format(Date=Date, Weekday=Weekday, Sunrise=Sunrise, Sunset=Sunset, Moonrise=Moonrise, Moonset=Moonset, Samvatsara=Samvatsara, Ayana=Ayana, Ritu=Ritu, Masa=Masa, Kollamera=Kollamera, Paksha=Paksha, Tithi=Tithi, Vasara=Vasara, Nakshatra=Nakshatra, Sunsign=Sunsign, Moonsign=Moonsign, Brahmamuhurta=Brahmamuhurta, Pratahsandhya=Pratahsandhya, Abhijitmuhurta=Abhijitmuhurta, Saayamsandhya=Saayamsandhya, Rahukalam=Rahukalam, Yamaganda=Yamaganda, Gulikaikaalam=Gulikaikaalam, Significance=Significance, Sudhakalainwomen=Sudhakalainwomen, Sudhakalainmen=Sudhakalainmen, Vishakalainwomen=Vishakalainwomen, Vishakalainmen=Vishakalainmen, Chakrabasedonvasara=Chakrabasedonvasara, Bodypartbasedonnakshatra=Bodypartbasedonnakshatra)
    st.code(msg)
    if st.button("Send to Telegram"):
        TELEGRAM_BOT_TOKEN = "7965698138:AAHvzdIZbZH9Uu9k8wmBevSev14iLwEgEAo"
        TELEGRAM_CHAT_ID = "-4741545165"

        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "Markdown"}

        response = requests.post(url, json=payload)
        if response.status_code == 200:
            st.success("Message sent to Telegram!")
        else:
            st.error("Failed to send message.")

st.write("📅 Tomorrow's Dainika Almanac is automatically sent in Telegram everyday at 9:20 PM IST")

st.subheader("Thank You!😊")
st.write('©️ VK 2024 onward')
