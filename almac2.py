import streamlit as st

# Title of the app
st.title("Streamlit WhatsApp Group Integration")

# Input for group link or ID
group_link = "https://chat.whatsapp.com/GrHQES9rLrh1Wc1nPqnDCw"

# Generate the link and button
if group_link:
    # Validate if the link starts with the proper format
    if group_link.startswith("https://chat.whatsapp.com/"):
        # Button to open the group in a new tab
        if st.button("Open WhatsApp Group"):
            st.markdown(
                f'<a href="{group_link}" target="_blank">Open WhatsApp Group</a>',
                unsafe_allow_html=True,
            )
    else:
        st.error("Please enter a valid WhatsApp group invite link.")
else:
    st.write("Enter a group link above to enable the group chat button.")
