import streamlit as st  # Import Streamlit for creating the web app
from chatbot import get_response  # Import the function to get responses from the chatbot

# Set the title of the web app
st.title("Simple Chatbot")

# Initialize chat history in session state if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to add messages to the chat history
def add_message_to_history(user_input, bot_response):
    st.session_state.chat_history.append({"user": user_input, "bot": bot_response})

# Get the user's input from a text box
user_input = st.text_input("You:", key="input")

# When the "Send" button is clicked
if st.button("Send"):
    # If the user has entered something
    if user_input:
        # Get the chatbot's response
        bot_response = get_response(user_input)
        # Add the conversation to the chat history
        add_message_to_history(user_input, bot_response)

# Display the chat history
if st.session_state.chat_history:
    for message in st.session_state.chat_history:
        # Show the user's message
        st.text_area("User", value=message["user"], height=50, max_chars=None)
        # Show the bot's response
        st.text_area("Bot", value=message["bot"], height=50, max_chars=None)
