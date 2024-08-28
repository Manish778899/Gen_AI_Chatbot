import openai  # Import the OpenAI library to interact with the API
from config import OPENAI_API_KEY  # Import the API key from the config file

# Set the API key to authenticate your requests to OpenAI
openai.api_key = OPENAI_API_KEY

# Function to get a response from the chatbot using gpt-3.5-turbo
def get_response(prompt):
    # Create a request to the OpenAI API with the user's prompt using gpt-3.5-turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model
        messages=[  # Messages is a list of dictionaries, where each dictionary is a message
            {"role": "system", "content": "You are a helpful assistant."},  # Set the system message
            {"role": "user", "content": prompt}  # Pass the user's input as a message
        ]
    )
    # Return the generated text response from the assistant
    return response.choices[0].message["content"].strip()
